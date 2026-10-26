# FlixMatch AI - Intelligent Streaming & Reading Recommendation Platform
> A consumer-grade streaming app interface (Netflix / Prime Video style) powered by an intelligent rule-based AI recommendation engine in Python.

![FlixMatch AI Banner](static/assets/cinelogic_hero_banner.jpg)

## 📌 Overview
**FlixMatch AI** is a modern streaming and reading recommendation platform that matches users with curated **Movies & Books** in real time. Built with a sleek Netflix-grade dark UI, dynamic hero billboard, horizontal carousel rows, and instant mood filtering, it combines streaming aesthetics with an explainable AI rule engine.

### Key Highlights:
- **Clean Streaming UI (Netflix / Prime Video Style)**:
  - Signature dark theme (`#141414`), red accents, full-bleed hero billboard with vignette lighting.
  - Horizontal carousel rows (`Top AI Matches`, `Cerebral Sci-Fi`, `Cozy Night In`, `High-Octane Thrills`, `Page-Turners`).
  - Netflix-style hover expansions with quick action buttons (`▶ Play`, `➕ My List`, `ℹ More Info`).
  - Interactive detailed item modal with synopsis, cast, audio/video specs, and companion cross-media recommendations.
- **Smart AI Recommendation Engine**:
  - Multi-pass Forward Chaining inference evaluating situational mood, social companion setting, cognitive bandwidth, tempo, and eras.
  - Transparent rule derivation trace explaining exactly *why* each item was recommended.
- **Instant Vibe Bar & Fine-Tuning Drawer**:
  - One-click mood pills (`🧠 Mind-Bending`, `☕ Cozy & Chill`, `🍿 Party Night`, `⚡ Adrenaline Rush`, `🌌 Deep Philosophical`).
  - Fine-tune companion settings, pacing, and cognitive energy.
- **Watchlist & Search**:
  - Real-time catalog search and local storage watchlist persistence.

---

## 🚀 Quickstart Guide

### 1. Requirements
- Python 3.10+
- Flask

### 2. Setup & Run
```bash
# Navigate to the project directory
cd "/Users/sumitwagdare/ai mini project"

# Activate the virtual environment
source .venv/bin/activate

# Start the application server
python app.py
```

Open your browser at:  
👉 **`http://127.0.0.1:5050`**

---

## 📂 Architecture

```
ai mini project/
├── .venv/                   # Python virtual environment
├── app.py                   # Flask REST API & Streaming Server
├── engine/
│   ├── __init__.py          # Engine package init
│   ├── knowledge_base.py    # Movie & Book catalog with streaming metadata & rules
│   ├── inference_engine.py  # Forward Chaining & Backward Chaining engine
│   └── rule_manager.py      # Runtime rule manager
├── static/
│   ├── css/
│   │   ├── style.css        # Netflix-inspired design system, cards, modal, rows
│   │   └── animations.css   # Shimmers, pulses, and transitions
│   └── js/
│       └── app.js           # Client controller for carousel rows, hero, watchlist, modal
├── templates/
│   └── index.html           # Single Page Application
├── test_engine.py           # Automated unit tests
└── README.md                # Project documentation
```
