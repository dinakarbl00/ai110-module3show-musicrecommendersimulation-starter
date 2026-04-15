# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This model generates music recommendations from a small dataset based on a user’s preferences. It assumes that users have consistent preferences in genre, mood, and audio features such as energy and tempo.

The system is designed for **classroom exploration and learning purposes**, not for real-world deployment.

---

## 3. How the Model Works  

The recommender compares user preferences with song attributes and assigns a score to each song.

It considers:
- Genre and mood (exact matches)
- Energy, tempo, valence, danceability, and acousticness (similarity)

Each feature contributes to the total score using weighted importance. Songs with higher similarity to user preferences receive higher scores.

The system also includes:
- Multiple ranking modes that change feature importance
- A diversity penalty to reduce repeated artists and genres

---

## 4. Data  

- Dataset contains **20 songs**
- Includes genres such as pop, rock, lofi, jazz, ambient
- Includes moods such as happy, chill, intense, relaxed
- Dataset is manually created and relatively small

This dataset does not capture the full diversity of real-world music or listener preferences.

---

## 5. Strengths  

- Produces intuitive and explainable recommendations
- Works well for clearly defined user profiles
- Captures important audio characteristics like energy and tempo
- Transparent scoring logic makes it easy to understand
- Diversity penalty improves variety in results

---

## 6. Limitations and Bias 

- Small dataset limits coverage and diversity
- Numeric similarity can override genre preferences
- Manual weighting introduces design bias
- Does not use real user behavior or feedback
- May favor certain genres due to dataset imbalance

This could lead to unfair exposure of some genres in a real-world system.

---

## 7. Evaluation  

The system was evaluated using multiple user profiles:

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock

Results were compared across:
- Different profiles
- Different ranking modes

Observations:
- Genre-first mode prioritizes exact genre matches
- Energy-first mode prioritizes vibe similarity over category
- Diversity penalty reduces repeated artists and genres

These tests helped confirm that the system responds logically to changes in preferences.

---

## 8. Future Work  

- Expand dataset to include more songs and genres
- Incorporate user listening history
- Implement collaborative filtering
- Improve fairness and diversity mechanisms
- Add advanced features like lyrics or genre hierarchies

---

## 9. Personal Reflection  

This project demonstrated how simple algorithms can produce meaningful recommendations. One surprising insight was how sensitive the system is to feature weights — small adjustments can significantly change results.

It also highlighted that recommendation systems are not neutral; they reflect the assumptions and biases of their design. Human judgment remains important to ensure fairness, diversity, and meaningful user experiences.