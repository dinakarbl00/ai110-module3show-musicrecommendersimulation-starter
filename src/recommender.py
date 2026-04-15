import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict, mode: str = "balanced") -> Tuple[float, str]:
    """
    Score a single song based on user preferences.
    Returns a numeric score and a text explanation.
    """

    if mode == "genre_first":
        genre_weight = 3.0
        mood_weight = 2.0
        energy_weight = 1.5
        tempo_weight = 0.8
        valence_weight = 0.8
        dance_weight = 0.8
        acoustic_weight = 0.8
    elif mode == "energy_first":
        genre_weight = 1.0
        mood_weight = 1.0
        energy_weight = 3.0
        tempo_weight = 1.5
        valence_weight = 0.8
        dance_weight = 0.8
        acoustic_weight = 0.8
    else:  # balanced
        genre_weight = 2.0
        mood_weight = 1.5
        energy_weight = 2.0
        tempo_weight = 1.0
        valence_weight = 1.0
        dance_weight = 1.0
        acoustic_weight = 1.0

    score = 0.0
    reasons = [f"mode={mode}"]

    # Genre match
    if song["genre"].lower() == user_prefs["genre"].lower():
        score += genre_weight
        reasons.append(f"genre match (+{genre_weight})")

    # Mood match
    if song["mood"].lower() == user_prefs["mood"].lower():
        score += mood_weight
        reasons.append(f"mood match (+{mood_weight})")

    # Energy similarity
    energy_difference = abs(song["energy"] - user_prefs["energy"])
    energy_similarity = max(0.0, 1.0 - energy_difference)
    energy_points = energy_similarity * energy_weight
    score += energy_points
    reasons.append(f"close energy (+{energy_points:.2f})")

    # Tempo similarity
    tempo_difference = abs(song["tempo_bpm"] - user_prefs["tempo_bpm"])
    tempo_similarity = max(0.0, 1.0 - (tempo_difference / 100.0))
    tempo_points = tempo_similarity * tempo_weight
    score += tempo_points
    reasons.append(f"close tempo (+{tempo_points:.2f})")

    # Valence similarity
    valence_difference = abs(song["valence"] - user_prefs["valence"])
    valence_similarity = max(0.0, 1.0 - valence_difference)
    valence_points = valence_similarity * valence_weight
    score += valence_points
    reasons.append(f"close valence (+{valence_points:.2f})")

    # Danceability similarity
    dance_difference = abs(song["danceability"] - user_prefs["danceability"])
    dance_similarity = max(0.0, 1.0 - dance_difference)
    dance_points = dance_similarity * dance_weight
    score += dance_points
    reasons.append(f"close danceability (+{dance_points:.2f})")

    # Acousticness similarity
    acoustic_difference = abs(song["acousticness"] - user_prefs["acousticness"])
    acoustic_similarity = max(0.0, 1.0 - acoustic_difference)
    acoustic_points = acoustic_similarity * acoustic_weight
    score += acoustic_points
    reasons.append(f"close acousticness (+{acoustic_points:.2f})")

    explanation = ", ".join(reasons)
    return score, explanation

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    mode: str = "balanced"
) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Returns a list of tuples:
    (song_dict, score, explanation)
    Includes a simple diversity penalty to reduce repetition.
    """
    remaining_songs = []

    for song in songs:
        score, explanation = score_song(user_prefs, song, mode=mode)
        remaining_songs.append((song, score, explanation))

    selected = []
    used_artists = set()
    genre_counts = {}

    while remaining_songs and len(selected) < k:
        best_choice = None
        best_adjusted_score = -1

        for song, base_score, explanation in remaining_songs:
            adjusted_score = base_score
            penalty_reasons = []

            if song["artist"] in used_artists:
                adjusted_score -= 0.75
                penalty_reasons.append("artist repeat penalty (-0.75)")

            current_genre_count = genre_counts.get(song["genre"], 0)
            if current_genre_count >= 2:
                adjusted_score -= 0.50
                penalty_reasons.append("genre repeat penalty (-0.50)")

            if adjusted_score > best_adjusted_score:
                new_explanation = explanation
                if penalty_reasons:
                    new_explanation += ", " + ", ".join(penalty_reasons)

                best_adjusted_score = adjusted_score
                best_choice = (song, adjusted_score, new_explanation)

        selected.append(best_choice)

        chosen_song = best_choice[0]
        used_artists.add(chosen_song["artist"])
        genre_counts[chosen_song["genre"]] = genre_counts.get(chosen_song["genre"], 0) + 1

        remaining_songs = [item for item in remaining_songs if item[0]["id"] != chosen_song["id"]]

    return selected