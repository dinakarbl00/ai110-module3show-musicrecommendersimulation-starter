# 🎵 Music Recommender Simulation

## Project Summary

This project builds a content-based music recommender system that suggests songs based on a user’s taste profile. Each song is represented using features such as genre, mood, energy, tempo, valence, danceability, and acousticness. The system compares these features with a user’s preferences and computes a weighted score to rank songs. It also includes multiple ranking modes and a diversity penalty to improve recommendation quality and reduce repetition.

---

## How The System Works

This recommender system works by comparing song features with user preferences and assigning a score to each song.

### Song Features Used

Each song includes:
- Genre (e.g., pop, rock, lofi)
- Mood (e.g., happy, chill, intense)
- Energy (0 to 1 scale)
- Tempo (beats per minute)
- Valence (how positive or happy a song feels)
- Danceability (how suitable it is for dancing)
- Acousticness (how acoustic vs electronic the song is)

### User Profile

The user profile stores:
- Preferred genre
- Preferred mood
- Target energy level
- Preferred tempo
- Preferred valence
- Preferred danceability
- Preferred acousticness

### Scoring Logic

Each song is scored based on:
- Genre match (bonus points)
- Mood match (bonus points)
- Similarity between song and user preferences for:
  - Energy
  - Tempo
  - Valence
  - Danceability
  - Acousticness

Similarity is calculated by checking how close the song’s value is to the user’s target value.

### Ranking

- All songs are scored
- Songs are sorted from highest score to lowest
- Top 5 songs are recommended

### Additional Features

- **Multiple ranking modes**:
  - Balanced
  - Genre-first
  - Energy-first

- **Diversity penalty**:
  - Reduces score if the same artist or genre appears repeatedly
  - Helps prevent repetitive recommendations.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

- Increasing the weight of **genre** caused same-genre songs to dominate.
- Increasing **energy and tempo** allowed cross-genre recommendations with similar vibe.
- Adding features like **valence, danceability, and acousticness** improved realism.
- Adding a **diversity penalty** reduced repetition of artists and genres.

### Key Observations  

- In **energy-first mode**, songs from different genres but similar energy appeared.
- In **genre-first mode**, songs strictly matching genre dominated results.
---

## Limitations and Risks

- Small dataset (20 songs) limits diversity  
- Does not consider lyrics or user listening history  
- Numeric features may overpower genre identity  
- Manually chosen weights may introduce bias  
- May create a filter bubble with similar recommendations

---

## Reflection

This project showed how recommendation systems convert structured data into meaningful predictions. Even simple scoring rules can produce realistic results when features are well chosen.

A key takeaway is that recommendation systems are highly sensitive to weight design. Small changes in feature importance can significantly alter results. This highlights how real-world systems are influenced by design decisions and can unintentionally introduce bias.

[**Model Card**](model_card.md)