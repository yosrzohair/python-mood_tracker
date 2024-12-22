from collections import Counter

def predict_next_week_moods(previous_week_moods):
    """
    Predicts the user's mood for the next week based on the previous week's data.
    :param previous_week_moods: List of moods for the past week (e.g., ['happy', 'sad', 'happy', ...])
    :return: Predicted moods for the next week
    """
    # Count the frequency of each mood
    mood_counts = Counter(previous_week_moods)
    
    # Find the most common mood
    most_common_mood = mood_counts.most_common(1)[0][0]
    
    # Predict the same mood for all days of the next week
    next_week_moods = [most_common_mood] * 7
    
    return next_week_moods

# Example Usage
previous_week = ['happy', 'happy', 'sad', 'happy', 'neutral', 'happy', 'sad']
next_week_prediction = predict_next_week_moods(previous_week)

print("Previous Week Moods:", previous_week)
print("Predicted Next Week Moods:", next_week_prediction)
