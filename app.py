"""
FlixMatch AI: Intelligent Streaming & Reading Recommendation Platform
Consumer-grade AI recommendation engine for Movies & Books.
"""

from flask import Flask, render_template, request, jsonify
import os
from engine.knowledge_base import CATALOG_ITEMS, PRODUCTION_RULES, PRESETS
from engine.inference_engine import InferenceEngine
from engine.rule_manager import RuleManager

app = Flask(__name__, static_folder="static", template_folder="templates")

# Initialize global rule manager
rule_manager = RuleManager()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/presets", methods=["GET"])
def get_presets():
    return jsonify({
        "success": True,
        "presets": PRESETS
    })

@app.route("/api/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json() or {}
        
        user_facts = {
            "domain": data.get("domain", "both"),
            "mood": data.get("mood", "reflective"),
            "companion": data.get("companion", "solo"),
            "cognitive_load": data.get("cognitive_load", "deeply_philosophical"),
            "tempo": data.get("tempo", "slow_burn"),
            "preferred_era": data.get("preferred_era", "contemporary"),
            "genre_preferences": data.get("genre_preferences", ["Sci-Fi"])
        }

        engine = InferenceEngine(rule_manager.get_all_rules(), rule_manager.get_all_catalog_items())
        result = engine.run_forward_chaining(user_facts)
        items = result["recommendations"]

        # Build categorized Netflix-style rows
        rows = []
        
        # Row 1: Top AI Matches for You (Highest Confidence)
        rows.append({
            "id": "row_top_matches",
            "title": "Top AI Matches For You",
            "subtitle": f"Personalized for your {user_facts['mood']} vibe & {user_facts['companion']} setting",
            "badge": "Top Picks",
            "items": items[:8]
        })

        # Row 2: Mind-Bending Sci-Fi & Speculative Masterpieces
        scifi_items = [i for i in items if "Sci-Fi" in i.get("genres", []) or i.get("cognitive_load") in ["mind_bending", "deeply_philosophical"]]
        if scifi_items:
            rows.append({
                "id": "row_scifi",
                "title": "Cerebral Sci-Fi & Mind-Benders",
                "subtitle": "High-concept cinema and literature that questions reality",
                "badge": "Mind-Bending",
                "items": scifi_items
            })

        # Row 3: Comfort & Feel-Good Cinema
        comfort_items = [i for i in items if i.get("cognitive_load") == "light_easy" or any(t in i.get("tones", []) for t in ["wholesome", "comforting", "uplifting", "witty"])]
        if comfort_items:
            rows.append({
                "id": "row_comfort",
                "title": "Cozy Night In & Comfort Stories",
                "subtitle": "Restorative, humorous, and heartwarming selections",
                "badge": "Comfort",
                "items": comfort_items
            })

        # Row 4: High-Stakes Thrills & Tension
        thrill_items = [i for i in items if any(g in i.get("genres", []) for g in ["Thriller", "Action", "Mystery"])]
        if thrill_items:
            rows.append({
                "id": "row_thrillers",
                "title": "High-Octane Suspense & Mystery",
                "subtitle": "Gripping, edge-of-your-seat narratives",
                "badge": "Trending",
                "items": thrill_items
            })

        # Row 5: Books & Literary Gems
        book_items = [i for i in items if i.get("type") == "book"]
        if book_items:
            rows.append({
                "id": "row_books",
                "title": "Page-Turners & Modern Classics",
                "subtitle": "Award-winning speculative fiction, philosophy, and memoirs",
                "badge": "Reading",
                "items": book_items
            })

        return jsonify({
            "success": True,
            "data": {
                "top_match": items[0] if items else None,
                "recommendations": items,
                "rows": rows,
                "working_memory": result["working_memory"],
                "fired_rules": result["fired_rules"],
                "trace_steps": result["trace_steps"],
                "total_rules": result["total_rules_in_kb"]
            }
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/explain", methods=["POST"])
def explain_item():
    try:
        data = request.get_json() or {}
        item_id = data.get("item_id")
        user_facts = data.get("user_facts", {})

        if not item_id:
            return jsonify({"success": False, "error": "Item ID is required."}), 400

        engine = InferenceEngine(rule_manager.get_all_rules(), rule_manager.get_all_catalog_items())
        explanation = engine.explain_item_goal(item_id, user_facts)
        
        # Attach cross media item if present
        cross_id = explanation.get("item", {}).get("cross_media_rec")
        if cross_id:
            cross_item = next((i for i in rule_manager.get_all_catalog_items() if i["id"] == cross_id), None)
            explanation["cross_media_item"] = cross_item

        return jsonify({"success": True, "data": explanation})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/search", methods=["GET"])
def search():
    query = request.args.get("q", "").strip().lower()
    if not query:
        return jsonify({"success": True, "results": []})
    
    catalog = rule_manager.get_all_catalog_items()
    results = []
    for item in catalog:
        title = item.get("title", "").lower()
        creator = item.get("director_or_author", "").lower()
        genres = " ".join(item.get("genres", [])).lower()
        tags = " ".join(item.get("tags", [])).lower()
        cast = " ".join(item.get("cast", [])).lower()

        if query in title or query in creator or query in genres or query in tags or query in cast:
            results.append(item)

    return jsonify({"success": True, "results": results, "total": len(results)})

@app.route("/api/rules", methods=["GET"])
def list_rules():
    return jsonify({
        "success": True,
        "rules": rule_manager.get_all_rules(),
        "total": len(rule_manager.get_all_rules())
    })

@app.route("/api/rules/add", methods=["POST"])
def add_rule():
    try:
        data = request.get_json() or {}
        res = rule_manager.add_custom_rule(data)
        return jsonify(res), (201 if res["success"] else 400)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/rules/reset", methods=["POST"])
def reset_rules():
    res = rule_manager.reset_rules()
    return jsonify(res)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
