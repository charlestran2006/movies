🎬🎮 Pickflix
A Flask-based web application that gives you instant movie or game recommendations based on your mood, genre, and time period. Click a button, get something worth watching or playing — no scrolling, no decision fatigue.

✨ Features
Instant Recommendations: One click gives you a random movie or game

Flexible Filters: Filter by type (movie or game), genre, mood, and year range

Smart Re-rolls: Avoids repeating the same recommendation back-to-back

Local Dataset: Uses a simple JSON file (no database required)

Clean, Minimal UI: Focused on speed and usability

Easy to Extend: Simple structure for adding more data, features, or APIs later

🚀 Getting Started
Prerequisites
Python 3.9 or higher

Git (optional, but recommended)

Installation
Clone the repository

bash
git clone https://github.com/yourusername/pickflix.git
cd pickflix
Or download the project folder and navigate into it.

Set up Python virtual environment (recommended)

bash
python -m venv .venv
Windows

bash
.venv\Scripts\activate
macOS / Linux

bash
source .venv/bin/activate
Install Python dependencies

bash
pip install -r requirements.txt
▶️ Running the Application
Start the Flask app

bash
python app.py
Open your browser

Go to http://127.0.0.1:5000

You’re ready to start getting recommendations.

🔧 How It Works
Dataset Loading: Movies and games are stored in a local JSON file (data/items.json) and loaded at app startup.

Filter Selection: Users can optionally filter by type, genre, mood, and year range.

Recommendation Engine: The app filters matching items and randomly selects one.

Repeat Protection: The previous recommendation is avoided when possible to keep results fresh.

Rendering: Results are displayed using Flask + Jinja templates.

🎭 Mood Examples
Hype – Action-packed movies or intense games

Chill – Relaxing, low-stress experiences

Cozy – Comfort movies or slow-paced games

Thoughtful – Story-driven or emotionally rich picks

Challenging – Skill-testing games or heavy films

🛠️ Technologies Used
Backend: Flask (Python)

Frontend: HTML, CSS (Jinja templates)

Data Storage: JSON

Randomization: Python standard library

Dependency: Flask 3.0.3

📝 Project Structure
text
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
🤝 Contributing
Fork the repository

Create a feature branch: git checkout -b feature/cool-feature

Commit your changes: git commit -m "Add cool feature"

Push to the branch: git push origin feature/cool-feature

Open a Pull Request

📄 License
This project is licensed under the MIT License — feel free to use, modify, and share it.
