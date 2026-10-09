"""Offline tests: no GitHub, Gemini, keys or credits required."""
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scripts import engine

CFG = {
    "owner": "merrypranxter", "pack_size": 2, "hybrid_pack_size": 2,
    "model": "not-called",
    "solo": [{"repo": "Mathgasm", "preset": "dingbat", "focus": "math"}],
    "hybrids": [{
        "sources": [
            {"repo": "slime_molds", "role": "adaptive branching networks"},
            {"repo": "klein-fluid-sim", "role": "non-orientable path surfaces"}],
        "focus": "Non-Euclidean living maze", "preset": "dingbat"
    }]
}
SIMPLE = {"title": "Strange Mathematics", "items": [
    {"title": "Thing " + str(n), "basis": "Boundaries",
     "prompt": "Create nine completely distinct bold flat mathematical ornaments with thick solid black paths, large white cut-outs, vector-friendly design, separated forms, a strong negative-space hierarchy and clear contours.",
     "why_weird": "It flips connectivity."} for n in range(2)]}
HYBRID = {"title": "Moldy Klein Worlds", "thesis": "Adaptive networks inhabit surfaces with twisted continuity.",
    "items": [dict(x, source_dna={
        "slime_molds": "Adaptive branching selects unconventional trajectories",
        "klein-fluid-sim": "Non-orientable paths invert geometry across seams"},
        fusion_logic=("A growing network finds efficient paths through a topology "
                      "that flips local orientation, producing reversed branches "
                      "and hollow corridors as a visual, speculative mutation."))
              for x in SIMPLE["items"]]}

class EngineTests(unittest.TestCase):
    def write(self, folder):
        (folder / "config.json").write_text(json.dumps(CFG))
    def test_rotation(self):
        self.assertEqual(engine.choose(CFG, {"volumes": 0})[0], "single")
        self.assertEqual(engine.choose(CFG, {"volumes": 1})[0], "hybrid")
        self.assertEqual(engine.choose(CFG, {"volumes": 2})[0], "single")
    def test_legacy_solo_cursor_is_migrated_and_advances(self):
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {"GEMINI_API_KEY": "fake"}):
            root = Path(tmp)
            cfg = dict(CFG, solo=[
                {"repo": "Mathgasm", "preset": "dingbat"},
                {"repo": "fractals", "preset": "dingbat"}])
            (root / "config.json").write_text(json.dumps(cfg))
            # First successful archive in production used this wrong cursor name.
            (root / "state.json").write_text(json.dumps({
                "volumes": 2, "solo_cursor": 0, "single_cursor": 1,
                "hybrid_cursor": 0}))
            lane, recipe = engine.choose(cfg, engine.get_json(root / "state.json"))
            self.assertEqual((lane, recipe["repo"]), ("single", "fractals"))
            engine.run(root=root, mode="single",
                       fetcher=lambda *args: "Verified source README",
                       writer=lambda *args: SIMPLE)
            state = engine.get_json(root / "state.json")
            self.assertEqual(state["solo_cursor"], 0)
            self.assertNotIn("single_cursor", state)

    def test_hybrid_json_schema_restricts_parent_dna_and_item_count(self):
        schema = engine.response_schema("hybrid", CFG["hybrids"][0], 2)
        entries = schema["properties"]["items"]
        self.assertEqual((entries["minItems"], entries["maxItems"]), (2, 2))
        item = entries["items"]
        self.assertIn("source_dna", item["required"])
        dna = item["properties"]["source_dna"]
        self.assertEqual(set(dna["required"]), {"slime_molds", "klein-fluid-sim"})
        self.assertFalse(dna["additionalProperties"])

    def test_gemini_payload_requests_structured_json(self):
        fake_response = {"candidates": [{"content": {
            "parts": [{"text": json.dumps(SIMPLE)}]}}]}
        with patch.object(engine, "http_json", return_value=fake_response) as api:
            result = engine.generate_gemini("prompt", "fake-key", "fake-model",
                                            "single", CFG["solo"][0], 2)
        self.assertEqual(result["title"], SIMPLE["title"])
        payload = api.call_args.args[2]
        generation = payload["generationConfig"]
        self.assertEqual(generation["responseMimeType"], "application/json")
        self.assertEqual(generation["responseJsonSchema"]["properties"]
                         ["items"]["minItems"], 2)

    def test_invalid_first_model_result_gets_one_repair_attempt(self):
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {"GEMINI_API_KEY": "fake"}):
            root = Path(tmp); self.write(root)
            calls = []
            def flaky_writer(prompt, *args):
                calls.append(prompt)
                return {"title": "Short", "items": []} if len(calls) == 1 else SIMPLE
            result = engine.run(root=root, mode="single",
                fetcher=lambda *args: "Verified source README",
                writer=flaky_writer)
            self.assertIn("Saved volume-001", result)
            self.assertEqual(len(calls), 2)
            self.assertIn("REPAIR REQUIRED", calls[1])

    def test_require_two_or_three_different_parents(self):
        with self.assertRaises(ValueError):
            engine.parents({"sources": ["A", "A"]})
        with self.assertRaises(ValueError):
            engine.parents({"sources": ["../../foo", "A"]})
        with self.assertRaises(ValueError):
            engine.parents({"sources": ["A"]})
    def test_prompt_mentions_each_parent_and_black_white_constraints(self):
        recipe = CFG["hybrids"][0]
        p = engine.prompt_for(CFG, "hybrid", recipe, ["Slime source", "Klein source"], [])
        for s in ["Slime source", "Klein source", "source_dna", "#000000", "#FFFFFF", "EXACTLY 2"]:
            self.assertIn(s, p)
    def test_reject_weak_hybrids(self):
        good = json.loads(json.dumps(HYBRID))
        self.assertIs(engine.validate(good, "hybrid", CFG["hybrids"][0], 2), good)
        good["items"][0]["source_dna"].pop("klein-fluid-sim")
        with self.assertRaises(ValueError):
            engine.validate(good, "hybrid", CFG["hybrids"][0], 2)
    def test_dry_run_offline(self):
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True):
            root = Path(tmp); self.write(root)
            result = engine.run(root=root, mode="hybrid", dry_run=True)
            self.assertIn("no model calls", result)
            self.assertIn("source_dna", (root / "PREVIEW.md").read_text())
            self.assertFalse((root / "state.json").exists())
    def test_real_hybrid_archive_with_fake_model(self):
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {"GEMINI_API_KEY": "fake"}):
            root = Path(tmp); self.write(root)
            result = engine.run(
                root=root, mode="hybrid",
                fetcher=lambda *args: "Verified source README",
                writer=lambda *args: HYBRID)
            self.assertIn("Saved volume-001", result)
            self.assertEqual(json.loads((root / "state.json").read_text())["volumes"], 1)
            folder = next((root / "harvest").iterdir())
            self.assertIn("FUSION LOGIC", (folder / "PROMPTS.md").read_text())
            self.assertTrue((folder / "MANIFEST.json").is_file())
            self.assertIn("HYBRID", (root / "HARVEST.md").read_text())
    def test_real_solo_archive_with_fake_model(self):
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {"GEMINI_API_KEY": "fake"}):
            root = Path(tmp); self.write(root)
            result = engine.run(
                root=root, mode="single",
                fetcher=lambda *args: "Verified source README",
                writer=lambda *args: SIMPLE)
            self.assertIn("Saved volume-001", result)
            self.assertEqual(json.loads((root / "state.json").read_text())["solo_cursor"], 0)
    def test_failure_never_advances_state(self):
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {"GEMINI_API_KEY": "fake"}):
            root = Path(tmp); self.write(root)
            bad = json.loads(json.dumps(HYBRID))
            bad["items"][0]["fusion_logic"] = "bad"
            with self.assertRaises(ValueError):
                engine.run(root=root, mode="hybrid", fetcher=lambda *args: "source",
                           writer=lambda *args: bad)
            self.assertFalse((root / "state.json").exists())
            self.assertFalse((root / "harvest").exists())

if __name__ == "__main__":
    unittest.main()
