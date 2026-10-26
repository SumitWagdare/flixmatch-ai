"""
Unit Tests for CineLogic AI Engine
Verifies forward chaining, working memory assertion, priority conflict resolution, and explanation facility.
"""

import unittest
from engine.knowledge_base import CATALOG_ITEMS, PRODUCTION_RULES, PRESETS
from engine.inference_engine import InferenceEngine
from engine.rule_manager import RuleManager

class TestInferenceEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InferenceEngine(PRODUCTION_RULES, CATALOG_ITEMS)

    def test_forward_chaining_mind_bender(self):
        facts = {
            "domain": "both",
            "mood": "reflective",
            "companion": "solo",
            "cognitive_load": "deeply_philosophical",
            "tempo": "slow_burn",
            "preferred_era": "contemporary",
            "genre_preferences": ["Sci-Fi"]
        }
        result = self.engine.run_forward_chaining(facts)

        self.assertIn("working_memory", result)
        self.assertIn("recommendations", result)
        self.assertGreater(len(result["recommendations"]), 0)
        
        # Verify cognitive rule fired
        fired_ids = [r["rule_id"] for r in result["fired_rules"]]
        self.assertIn("RULE-COG-01", fired_ids)
        self.assertIn("RULE-SOC-02", fired_ids)

        # Working memory should have deduced facts
        self.assertEqual(result["working_memory"].get("inferred_need"), "intellectual_transcendence")
        self.assertEqual(result["working_memory"].get("accessibility"), "deep_personal_immersion")

        # Top recommendations should be Interstellar, Blade Runner 2049, or Dune
        top_titles = [item["title"] for item in result["recommendations"][:3]]
        self.assertTrue(any(t in ["Interstellar", "Blade Runner 2049", "Dune"] for t in top_titles))

    def test_forward_chaining_wholesome_comfort(self):
        facts = {
            "domain": "both",
            "mood": "exhausted",
            "companion": "solo",
            "cognitive_load": "light_easy",
            "tempo": "moderate",
            "preferred_era": "contemporary",
            "genre_preferences": ["Animation", "Comedy"]
        }
        result = self.engine.run_forward_chaining(facts)
        fired_ids = [r["rule_id"] for r in result["fired_rules"]]
        self.assertIn("RULE-COG-02", fired_ids)
        self.assertEqual(result["working_memory"].get("inferred_need"), "cognitive_restoration")

        # Paddington 2, Spirited Away, or Midnight Library should rank at the top
        top_titles = [item["title"] for item in result["recommendations"][:4]]
        self.assertTrue(any(t in ["Paddington 2", "Spirited Away", "The Midnight Library"] for t in top_titles))

    def test_backward_chaining_explanation(self):
        facts = {
            "domain": "both",
            "mood": "reflective",
            "companion": "solo",
            "cognitive_load": "deeply_philosophical",
            "tempo": "slow_burn",
            "preferred_era": "contemporary",
            "genre_preferences": ["Sci-Fi"]
        }
        explanation = self.engine.explain_item_goal("mov_01", facts) # Interstellar
        self.assertTrue(explanation["success"])
        self.assertEqual(explanation["proof_status"], "SATISFIED")
        self.assertGreaterEqual(explanation["confidence"], 70)
        self.assertGreater(len(explanation["supporting_facts"]), 0)

    def test_rule_manager_custom_rule(self):
        rm = RuleManager()
        self.assertEqual(len(rm.get_all_rules()), len(PRODUCTION_RULES))

        custom = {
            "name": "Vintage Noir Mystery Rule",
            "level": 3,
            "priority": 72,
            "conditions": {
                "mood_in": ["reflective"],
                "preferred_era_in": ["classic"]
            },
            "explanation": "Vintage noir classics match reflective moods seeking classic era cinematography.",
            "boost_weight": 25
        }
        res = rm.add_custom_rule(custom)
        self.assertTrue(res["success"])
        self.assertEqual(len(rm.get_all_rules()), len(PRODUCTION_RULES) + 1)

if __name__ == "__main__":
    unittest.main()
