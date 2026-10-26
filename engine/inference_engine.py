"""
Inference Engine for CineLogic AI Recommendation System
SPPU TE Computer Engineering - Artificial Intelligence Laboratory
Implements:
1. Forward Chaining (Data-Driven Reasoning Engine)
2. Conflict Resolution (Priority + Specificity)
3. Working Memory & Dynamic Fact Assertion
4. Step-by-step Trace Generation (For Live Animated Visualizer & Viva Defense)
5. Backward Chaining Explanation Facility
"""

from typing import Dict, List, Any, Optional
import copy


class InferenceEngine:
    def __init__(self, rules: List[Dict[str, Any]], catalog: List[Dict[str, Any]]):
        self.rules = sorted(rules, key=lambda r: (r.get("priority", 0), len(r.get("conditions", {}))), reverse=True)
        self.catalog = catalog

    def run_forward_chaining(self, initial_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes Forward Chaining inference starting from initial user facts.
        Returns:
            - working_memory: Final set of known and deduced facts
            - trace_steps: Detailed step-by-step animation and diagnostic log
            - fired_rules: List of rules that fired
            - recommendations: Ranked list of suggested items with confidence scores & explanations
        """
        # 1. Initialize Working Memory
        working_memory = copy.deepcopy(initial_facts)
        trace_steps: List[Dict[str, Any]] = []
        fired_rules: List[Dict[str, Any]] = []
        
        # Working memory log event
        trace_steps.append({
            "step_number": 1,
            "type": "INITIALIZATION",
            "title": "Working Memory Initialized",
            "description": f"Loaded {len(initial_facts)} user input facts into Working Memory.",
            "data": copy.deepcopy(working_memory)
        })

        # 2. Forward Chaining Loop (Multi-pass with Conflict Resolution)
        evaluated_rule_ids = set()
        has_new_deductions = True
        pass_number = 1

        while has_new_deductions:
            has_new_deductions = False
            agenda: List[Dict[str, Any]] = []

            # Find all activated rules that haven't fired yet
            for rule in self.rules:
                rule_id = rule["rule_id"]
                if rule_id in evaluated_rule_ids:
                    continue

                is_active, condition_evals = self._evaluate_rule_conditions(rule["conditions"], working_memory)

                if is_active:
                    agenda.append({
                        "rule": rule,
                        "condition_evals": condition_evals
                    })

            # Conflict Resolution: Sort agenda by priority descending, then specificity
            agenda.sort(
                key=lambda x: (
                    x["rule"].get("priority", 0),
                    len(x["rule"].get("conditions", {}))
                ),
                reverse=True
            )

            # Fire the activated rules in priority order
            for item in agenda:
                rule = item["rule"]
                rule_id = rule["rule_id"]
                evaluated_rule_ids.add(rule_id)

                # Check if this rule deduces new facts into Working Memory
                consequences = rule.get("consequences", {})
                new_facts = consequences.get("deduce_facts", {})
                new_deductions_found = False

                for k, v in new_facts.items():
                    if k not in working_memory or working_memory[k] != v:
                        working_memory[k] = v
                        new_deductions_found = True
                        has_new_deductions = True

                fired_rule_record = {
                    "rule_id": rule_id,
                    "name": rule["name"],
                    "priority": rule.get("priority", 0),
                    "level": rule.get("level", 1),
                    "explanation": rule.get("explanation", ""),
                    "deduced_facts": new_facts,
                    "boost_criteria": consequences.get("boost_criteria", {})
                }
                fired_rules.append(fired_rule_record)

                trace_steps.append({
                    "step_number": len(trace_steps) + 1,
                    "type": "RULE_FIRED",
                    "title": f"Fired: {rule_id} ({rule['name']})",
                    "description": rule.get("explanation", ""),
                    "rule_id": rule_id,
                    "priority": rule.get("priority", 0),
                    "conditions": item["condition_evals"],
                    "newly_asserted_facts": new_facts if new_deductions_found else None,
                    "pass_number": pass_number
                })

            pass_number += 1
            if pass_number > 10:  # Safeguard against potential infinite cycles
                break

        # 3. Recommend & Score Items using Working Memory & Fired Rules
        recommendations = self._score_catalog_items(working_memory, fired_rules)

        trace_steps.append({
            "step_number": len(trace_steps) + 1,
            "type": "RECOMMENDATION_RANKING",
            "title": "Conflict Resolution & Final Scoring Complete",
            "description": f"Successfully evaluated {len(self.catalog)} items. Generated {len(recommendations)} ranked suggestions.",
            "top_match": recommendations[0]["title"] if recommendations else None
        })

        return {
            "working_memory": working_memory,
            "trace_steps": trace_steps,
            "fired_rules": fired_rules,
            "recommendations": recommendations,
            "total_rules_in_kb": len(self.rules),
            "rules_fired_count": len(fired_rules)
        }

    def _evaluate_rule_conditions(self, conditions: Dict[str, Any], memory: Dict[str, Any]) -> (bool, List[Dict[str, Any]]):
        """
        Evaluates rule preconditions against current working memory.
        Supports:
        - `key_in`: memory[key] is in expected list
        - `key_contains`: substring or element inside memory[key] list
        - `key_equals`: exact match
        """
        all_satisfied = True
        condition_evals: List[Dict[str, Any]] = []

        for cond_key, expected_val in conditions.items():
            satisfied = False
            detail = ""

            if cond_key.endswith("_in"):
                fact_key = cond_key[:-3]
                actual_val = memory.get(fact_key)
                if actual_val in expected_val:
                    satisfied = True
                    detail = f"Fact '{fact_key}' = '{actual_val}' is in {expected_val}"
                else:
                    detail = f"Fact '{fact_key}' = '{actual_val}' is NOT in {expected_val}"

            elif cond_key.endswith("_contains"):
                fact_key = cond_key[:-9]
                actual_val = memory.get(fact_key, [])
                if isinstance(actual_val, list):
                    satisfied = expected_val in actual_val
                    detail = f"'{expected_val}' {'found' if satisfied else 'not found'} in {fact_key} list"
                elif isinstance(actual_val, str):
                    satisfied = expected_val.lower() in actual_val.lower()
                    detail = f"'{expected_val}' {'found' if satisfied else 'not found'} in {fact_key} string"

            elif cond_key.endswith("_equals"):
                fact_key = cond_key[:-7]
                actual_val = memory.get(fact_key)
                satisfied = actual_val == expected_val
                detail = f"Fact '{fact_key}' ({actual_val}) == {expected_val}: {satisfied}"

            else:
                # Default direct equality
                actual_val = memory.get(cond_key)
                satisfied = actual_val == expected_val
                detail = f"Fact '{cond_key}' ({actual_val}) == {expected_val}: {satisfied}"

            condition_evals.append({
                "predicate": cond_key,
                "expected": expected_val,
                "satisfied": satisfied,
                "detail": detail
            })

            if not satisfied:
                all_satisfied = False

        return all_satisfied, condition_evals

    def _score_catalog_items(self, memory: Dict[str, Any], fired_rules: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Calculates match score (0 - 100%) for each candidate item.
        Applies direct attribute synergy and additive boosts from fired production rules.
        """
        domain_filter = memory.get("domain", "both")
        user_mood = memory.get("mood")
        user_tempo = memory.get("tempo")
        user_cog = memory.get("cognitive_load")
        user_companion = memory.get("companion")
        user_era = memory.get("preferred_era")
        user_genres = memory.get("genre_preferences", [])

        scored_items = []

        for item in self.catalog:
            # Check domain filter
            if domain_filter != "both" and item["type"] != domain_filter:
                continue

            score = 30.0  # Base prior
            matched_rules_for_item = []
            score_breakdown = []

            # 1. Direct Attribute Synergies (Primary Heuristic Matches)
            if user_mood and user_mood in item.get("moods", []):
                score += 18.0
                score_breakdown.append(f"+18% Perfect Mood Synergy ({user_mood.capitalize()})")

            if user_tempo and user_tempo == item.get("tempo"):
                score += 12.0
                score_breakdown.append(f"+12% Tempo Harmony ({user_tempo.replace('_', ' ').capitalize()})")

            if user_cog and user_cog == item.get("cognitive_load"):
                score += 14.0
                score_breakdown.append(f"+14% Cognitive Depth Alignment ({user_cog.replace('_', ' ').capitalize()})")

            if user_companion and user_companion in item.get("companions", []):
                score += 10.0
                score_breakdown.append(f"+10% Social Context Fit ({user_companion.capitalize()})")

            if user_era and user_era in item.get("eras", []):
                score += 8.0
                score_breakdown.append(f"+8% Era Preference Match ({user_era.capitalize()})")

            # Genre overlap
            common_genres = set(user_genres).intersection(set(item.get("genres", [])))
            if common_genres:
                genre_pts = min(15.0, len(common_genres) * 7.5)
                score += genre_pts
                score_breakdown.append(f"+{genre_pts}% Genre Overlap ({', '.join(common_genres)})")

            # 2. Production Rule Consequence Boosts
            for fired in fired_rules:
                boost_crit = fired.get("boost_criteria", {})
                rule_boost = boost_crit.get("boost_weight", 0)
                rule_matched_this_item = False

                # Check tags overlap
                rule_tags = boost_crit.get("tags", [])
                if rule_tags and set(rule_tags).intersection(set(item.get("tags", []))):
                    rule_matched_this_item = True

                # Check tones overlap
                rule_tones = boost_crit.get("tones", [])
                if rule_tones and set(rule_tones).intersection(set(item.get("tones", []))):
                    rule_matched_this_item = True

                # Check genres
                rule_genres = boost_crit.get("genres", [])
                if rule_genres and set(rule_genres).intersection(set(item.get("genres", []))):
                    rule_matched_this_item = True

                # Check cognitive load
                rule_cogs = boost_crit.get("cognitive_load", [])
                if rule_cogs and item.get("cognitive_load") in rule_cogs:
                    rule_matched_this_item = True

                # Check companions
                rule_comps = boost_crit.get("companions", [])
                if rule_comps and set(rule_comps).intersection(set(item.get("companions", []))):
                    rule_matched_this_item = True

                # Check rating threshold
                min_r = boost_crit.get("min_rating")
                if min_r and item.get("rating", 0) >= min_r:
                    rule_matched_this_item = True

                if rule_matched_this_item:
                    applied_boost = min(15.0, rule_boost * 0.4)
                    score += applied_boost
                    matched_rules_for_item.append({
                        "rule_id": fired["rule_id"],
                        "rule_name": fired["name"],
                        "explanation": fired["explanation"],
                        "boost_applied": applied_boost
                    })
                    score_breakdown.append(f"+{applied_boost:.1f}% Boost via {fired['rule_id']}")

            # Normalize final confidence score to [45% - 99%]
            final_confidence = min(99, max(45, int(round(score))))

            item_copy = copy.deepcopy(item)
            item_copy["confidence"] = final_confidence
            item_copy["matched_rules"] = matched_rules_for_item
            item_copy["score_breakdown"] = score_breakdown
            scored_items.append(item_copy)

        # Sort descending by confidence, then rating
        scored_items.sort(key=lambda x: (x["confidence"], x.get("rating", 0)), reverse=True)
        return scored_items

    def explain_item_goal(self, item_id: str, user_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        Backward Chaining / Goal-Driven Explanation Facility:
        Given an item_id as the goal hypothesis (e.g., 'Interstellar' or 'Dune'),
        determines if and how user facts support this goal.
        """
        target_item = next((item for item in self.catalog if item["id"] == item_id), None)
        if not target_item:
            return {"success": False, "error": f"Item {item_id} not found in catalog."}

        # Run forward reasoning to obtain current working memory & fired rules
        result = self.run_forward_chaining(user_facts)
        working_memory = result["working_memory"]
        fired_rules = result["fired_rules"]

        supporting_facts = []
        contradicting_facts = []

        # Analyze User Facts vs Target Item attributes
        if user_facts.get("mood") in target_item.get("moods", []):
            supporting_facts.append(f"Mood alignment: User is '{user_facts.get('mood')}', matching item's moods {target_item.get('moods')}.")
        else:
            contradicting_facts.append(f"Mood variance: User is '{user_facts.get('mood')}', whereas item is tagged with {target_item.get('moods')}.")

        if user_facts.get("cognitive_load") == target_item.get("cognitive_load"):
            supporting_facts.append(f"Cognitive load match: Both specify '{user_facts.get('cognitive_load')}'.")

        if user_facts.get("tempo") == target_item.get("tempo"):
            supporting_facts.append(f"Tempo sync: Both match '{user_facts.get('tempo')}'.")

        # Find rules directly supporting this item
        supporting_rules = []
        for fired in fired_rules:
            boost_crit = fired.get("boost_criteria", {})
            rule_tags = boost_crit.get("tags", [])
            rule_genres = boost_crit.get("genres", [])
            rule_tones = boost_crit.get("tones", [])

            if (set(rule_tags).intersection(set(target_item.get("tags", []))) or
                set(rule_genres).intersection(set(target_item.get("genres", []))) or
                set(rule_tones).intersection(set(target_item.get("tones", [])))):
                supporting_rules.append({
                    "rule_id": fired["rule_id"],
                    "name": fired["name"],
                    "explanation": fired["explanation"]
                })

        # Match confidence from the forward chaining results
        matched_item = next((r for r in result["recommendations"] if r["id"] == item_id), None)
        confidence = matched_item["confidence"] if matched_item else 50

        return {
            "success": True,
            "item": target_item,
            "confidence": confidence,
            "goal_hypothesis": f"Recommend({target_item['title']})",
            "proof_status": "SATISFIED" if confidence >= 70 else "PARTIALLY_SATISFIED",
            "supporting_facts": supporting_facts,
            "contradicting_facts": contradicting_facts,
            "supporting_rules": supporting_rules,
            "working_memory_state": working_memory
        }
