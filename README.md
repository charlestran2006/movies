🎬🎮 Pickflix

A Flask-based web application that gives you instant movie or game recommendations based on your mood, genre, and time period. Click a button, get something worth watching or playing — no scrolling, no decision fatigue.

✨ Features

Instant Recommendations: One click gives you a random movie or game

Flexible Filters:

Type (Movie or Game)
# 🎬🎮 Pickflix

A Flask-based web application that gives you instant movie or game recommendations based on your mood, genre, and year range. Simply choose your preferences (or none at all), click a button, and Pickflix suggests something worth watching or playing.

---

## ✨ Features

- **Instant Recommendations**: One click gives you a random movie or game
- **Flexible Filtering**:
  - Type (Movie or Game)
  - Genre
  - Mood
  - Year range
- **Smart Re-rolls**: Avoids repeating the same recommendation back-to-back
- **Local Dataset**: Uses a JSON file for data (no database required)
- **Clean, Minimal UI**: Simple, fast, and distraction-free
- **Easy to Extend**: Add more items, filters, or external APIs later

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Git (optional, but recommended)

---

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pickflix.git
   cd pickflix

Genre

Mood

Year range

Smart Re-rolls: Avoids repeating the same recommendation back-to-back

Local Dataset: Uses a simple JSON file (no database required)

Clean, Minimal UI: Focused on speed and usability

Easy to Extend: Add more data, features, or APIs later

🚀 Getting Started
Prerequisites

Python 3.9 or higher

Git (optional, but recommended)

Installation
Clone the repository
git clone https://github.com/yourusername/pickflix.git
cd pickflix


Or download the project folder and navigate into it.

Set up Python virtual environment (recommended)
python -m venv .venv


Windows

.venv\Scripts\activate


macOS / Linux

source .venv/bin/activate

Install Python dependencies
pip install -r requirements.txt

▶️ Running the Application

Start the Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000


That’s it. You’re ready to start getting recommendations.

🔧 How It Works

Dataset Loading
Movies and games are stored in a local JSON file (data/items.json) and loaded at app startup.

Filter Selection
Users can optionally filter by type, genre, mood, and year range.

Recommendation Engine
The app filters matching items and randomly selects one.

Repeat Protection
The previous recommendation is avoided when possible to keep results fresh.

Rendering
Results are displayed using Flask + Jinja templates.

🎭 Mood Examples

You can define any moods you want in the dataset, but common ones include:

Hype – Action-packed movies or intense games

Chill – Relaxing, low-stress experiences

Cozy – Comfort movies or slow-paced games

Thoughtful – Story-driven or emotionally rich picks

Challenging – Skill-testing games or heavy films

Moods are fully customizable via the JSON file.

🛠️ Technologies Used

Backend: Flask (Python)

Frontend: HTML, CSS (Jinja templates)

Data Storage: JSON

Randomization: Python standard library

Dependencies

Flask 3.0.3

📝 Project Structure
pickflix/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── items.json
├── templates/
│   └── index.html
└── static/
    └── style.css

🧠 Customization Ideas

Easy upgrades if you want to keep building:

Add a form to submit new movies/games

Track favorites or likes

Add exclude filters (e.g., “no horror”)

Switch JSON → SQLite

Integrate external APIs:

TMDB (movies)

RAWG / Steam (games)

Deploy to Render, Fly.io, or Railway

🤝 Contributing

Contributions are welcome.

Fork the repository

Create a feature branch

git checkout -b feature/cool-feature


Commit your changes

git commit -m "Add cool feature"


Push to the branch

git push origin feature/cool-feature


Open a Pull Request

📄 License

MIT License — do whatever you want with it.
