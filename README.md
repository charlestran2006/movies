<div align="center">

# 🎬🎮 Pickflix

**A Flask web app that gives you instant movie or game recommendations based on your mood, genre, and time period — no scrolling, no decision fatigue.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-black?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

</div>

---

## Overview

Pickflix solves a simple problem: choosing what to watch or play takes too long. Enter your mood, set a few optional filters, and get a recommendation instantly. Click again to re-roll. That's it.

Built with Flask and a local JSON dataset — no external API keys, no database setup required.

---

## Features

| Feature | Description |
|---|---|
| Instant recommendations | One click returns a random movie or game |
| Flexible filters | Filter by type, genre, mood, and year range |
| Smart re-rolls | Avoids repeating the same recommendation back-to-back |
| Local dataset | All data lives in a single JSON file — no database needed |
| Easy to extend | Simple structure for adding more data, filters, or external APIs |

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git (optional)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/pickflix.git
cd pickflix
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
```

```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

### Running the App

```bash
python app.py
```

Then open your browser and go to **http://127.0.0.1:5000**

---

## How It Works

1. **Dataset Loading** — Movies and games are stored in `data/items.json` and loaded at app startup
2. **Filter Selection** — Users optionally filter by type, genre, mood, and year range
3. **Recommendation Engine** — Matching items are filtered and one is selected at random
4. **Repeat Protection** — The previous result is excluded from the next roll when possible
5. **Rendering** — Results are displayed via Flask + Jinja2 templates

---

## Mood Guide

| Mood | What to Expect |
|---|---|
| **Hype** | Action-packed movies or high-intensity games |
| **Chill** | Relaxing, low-stakes experiences |
| **Cozy** | Comfort watches or slow-paced games |
| **Thoughtful** | Story-driven or emotionally rich picks |
| **Challenging** | Skill-testing games or heavy films |

---

## Project Structure

```
pickflix/
├── app.py                 # Flask app — routes and recommendation logic
├── requirements.txt       # Python dependencies
├── README.md
├── data/
│   └── items.json         # Movies and games dataset
├── templates/
│   └── index.html         # Jinja2 HTML template
└── static/
    └── style.css          # Stylesheet
```

---

## Tech Stack

- **Backend** — Flask (Python)
- **Frontend** — HTML, CSS, Jinja2 templates
- **Data** — JSON
- **Randomization** — Python standard library (`random`)

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <sub>Built with Flask · No API keys required</sub>
</div>
