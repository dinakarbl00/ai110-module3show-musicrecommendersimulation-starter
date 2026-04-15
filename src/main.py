from recommender import load_songs, recommend_songs


def print_recommendations(profile_name, user_prefs, songs, k=5, mode="balanced"):
    print("=" * 70)
    print(f"PROFILE: {profile_name}")
    print(f"MODE: {mode}")
    print(f"Preferences: {user_prefs}")
    print("=" * 70)

    recommendations = recommend_songs(user_prefs, songs, k=k, mode=mode)

    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{rank}. {song['title']} by {song['artist']}")
        print(f"   Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']}")
        print(f"   Score: {score:.2f}")
        print(f"   Because: {explanation}")
        print()

    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 122,
            "valence": 0.85,
            "danceability": 0.85,
            "acousticness": 0.15
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.4,
            "tempo_bpm": 78,
            "valence": 0.58,
            "danceability": 0.60,
            "acousticness": 0.80
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
            "tempo_bpm": 145,
            "valence": 0.45,
            "danceability": 0.60,
            "acousticness": 0.10
        }
    }

    print(f"Loaded songs: {len(songs)}\n")

    # Show recommendations for each profile using balanced mode
    for profile_name, user_prefs in profiles.items():
        print_recommendations(profile_name, user_prefs, songs, k=5, mode="balanced")

    # Compare ranking modes for one profile
    demo_profile_name = "High-Energy Pop"
    demo_profile = profiles[demo_profile_name]

    print("\n" + "#" * 70)
    print("COMPARING RANKING MODES FOR HIGH-ENERGY POP")
    print("#" * 70 + "\n")

    for mode in ["balanced", "genre_first", "energy_first"]:
        print_recommendations(demo_profile_name, demo_profile, songs, k=5, mode=mode)


if __name__ == "__main__":
    main()