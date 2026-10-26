"""
Rule Manager for CineLogic AI
Allows live inspection, creation, and deletion of custom production rules in the Knowledge Base.
"""

from typing import Dict, List, Any
import copy
from .knowledge_base import PRODUCTION_RULES, CATALOG_ITEMS

class RuleManager:
    def __init__(self):
        # In-memory working rules (starts with the default static knowledge base)
        self.rules: List[Dict[str, Any]] = copy.deepcopy(PRODUCTION_RULES)
        self.catalog: List[Dict[str, Any]] = copy.deepcopy(CATALOG_ITEMS)

    def get_all_rules(self) -> List[Dict[str, Any]]:
        return self.rules

    def get_all_catalog_items(self) -> List[Dict[str, Any]]:
        return self.catalog

    def add_custom_rule(self, rule_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates and appends a new rule to the knowledge base.
        """
        required_fields = ["name", "conditions", "explanation"]
        for field in required_fields:
            if field not in rule_data:
                return {"success": False, "error": f"Missing required rule field: {field}"}

        # Generate a unique Rule ID
        rule_num = len(self.rules) + 1
        rule_id = f"RULE-USR-{rule_num:02d}"

        new_rule = {
            "rule_id": rule_id,
            "name": rule_data["name"],
            "level": rule_data.get("level", 2),
            "priority": int(rule_data.get("priority", 50)),
            "conditions": rule_data["conditions"],
            "consequences": rule_data.get("consequences", {
                "boost_criteria": {
                    "boost_weight": int(rule_data.get("boost_weight", 20))
                }
            }),
            "explanation": rule_data["explanation"],
            "is_custom": True
        }

        self.rules.append(new_rule)
        return {"success": True, "rule": new_rule}

    def reset_rules(self):
        """Reset to initial default knowledge base"""
        self.rules = copy.deepcopy(PRODUCTION_RULES)
        return {"success": True, "message": "Knowledge base reset to original default rules."}
