from __future__ import annotations

import json
import os
import random
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Set, Tuple

from flask import Flask, render_template, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "items.json")

app = Flask(__name__)


@dataclass(frozen=True)
class Item:
    id: str
    title: str
    kind: str          # "movie" or "game"
    year: int
    genres: List[str]
    moods: List[str]
    platforms: List[str]
    duration: str
    description: str


def load_items() -> List[Item]:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)

    items: List[Item] = []
    for obj in raw:
        items.append(
            Item(
                id=str(obj["id"]),
                title=str(obj["title"]),
                kind=str(obj["kind"]).lower(),
                year=int(obj["year"]),
                genres=[str(g) for g in obj.get("genres", [])],
                moods=[str(m) for m in obj.get("moods", [])],
                platforms=[str(p) for p in obj.get("platforms", [])],
                duration=str(obj.get("duration", "")),
                description=str(obj.get("description", "")),
            )
        )
    return items


ITEMS: List[Item] = load_items()


def unique_sorted(values: Set[str]) -> List[str]:
    # Sort case-insensitively but preserve original capitalization
    return sorted(values, key=lambda s: s.lower())


def build_filter_options(items: List[Item]) -> Dict[str, List[str]]:
    genres: Set[str] = set()
    moods: Set[str] = set()
    kinds: Set[str] = set()

    for it in items:
        kinds.add(it.kind)
        for g in it.genres:
            genres.add(g)
        for m in it.moods:
            moods.add(m)

    return {
        "kinds": unique_sorted(kinds),
        "genres": unique_sorted(genres),
        "moods": unique_sorted(moods),
    }


FILTER_OPTIONS = build_filter_options(ITEMS)


def parse_int(value: str, default: int) -> int:
    try:
        return int(value)
    except Exception:
        return default


def passes_filters(
    item: Item,
    kind: str,
    genre: str,
    mood: str,
    year_min: int,
    year_max: int,
) -> bool:
    if kind and kind != "any" and item.kind != kind:
        return False

    if genre and genre != "any":
        if genre not in item.genres:
            return False

    if mood and mood != "any":
        if mood not in item.moods:
            return False

    if item.year < year_min or item.year > year_max:
        return False

    return True


def pick_recommendation(
    items: List[Item],
    kind: str,
    genre: str,
    mood: str,
    year_min: int,
    year_max: int,
    avoid_id: Optional[str] = None,
) -> Tuple[Optional[Item], int]:
    pool = [
        it for it in items
        if passes_filters(it, kind, genre, mood, year_min, year_max)
    ]

    total_matches = len(pool)
    if total_matches == 0:
        return None, 0

    # Try to avoid repeating the same rec if possible
    if avoid_id and total_matches > 1:
        pool_no_repeat = [it for it in pool if it.id != avoid_id]
        if pool_no_repeat:
            pool = pool_no_repeat

    return random.choice(pool), total_matches


@app.route("/", methods=["GET", "POST"])
def index():
    # Defaults
    years = [it.year for it in ITEMS]
    default_min = min(years) if years else 1980
    default_max = max(years) if years else 2025

    # Form state (use request values so the form stays filled in)
    kind = request.values.get("kind", "any").lower()
    genre = request.values.get("genre", "any")
    mood = request.values.get("mood", "any")
    year_min = parse_int(request.values.get("year_min", str(default_min)), default_min)
    year_max = parse_int(request.values.get("year_max", str(default_max)), default_max)
    last_id = request.values.get("last_id", "").strip() or None

    recommendation = None
    matches = None
    error = None

    if request.method == "POST":
        # Fix inverted ranges gracefully
        if year_min > year_max:
            year_min, year_max = year_max, year_min

        recommendation, matches = pick_recommendation(
            ITEMS, kind, genre, mood, year_min, year_max, avoid_id=last_id
        )
        if recommendation is None:
            error = "No matches for those filters. Try loosening genre/mood or expanding the year range."

    return render_template(
        "index.html",
        options=FILTER_OPTIONS,
        form_state={
            "kind": kind,
            "genre": genre,
            "mood": mood,
            "year_min": year_min,
            "year_max": year_max,
            "last_id": last_id or "",
        },
        recommendation=recommendation,
        matches=matches,
        error=error,
        year_bounds={"min": default_min, "max": default_max},
    )


if __name__ == "__main__":
    # Debug on for local dev
    app.run(debug=True, host="127.0.0.1", port=5000)
