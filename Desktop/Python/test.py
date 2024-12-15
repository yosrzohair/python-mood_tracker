from collections import Counter

def get_mood_for_week():
    # A list to store moods for each day
    moods = []

    # Loop for 7 days (a week)
    for day in range(1, 8):  # Days 1 to 7
        mood = input(f"Enter your mood for day {day}: ").lower()  # Take user input and convert it to lowercase
        moods.append(mood)  # Append the input mood to the list
    
    return moods

def calculate_mood_percentage(moods):
    # Create a dictionary to count the occurrences of each mood
    mood_counts = {}

    for mood in moods:
        if mood in mood_counts:
            mood_counts[mood] += 1
        else:
            mood_counts[mood] = 1
    
    total_days = len(moods)  # Total number of days (7 in this case)
    mood_percentages = {mood: (count / total_days) * 100 for mood, count in mood_counts.items()}  # Calculate percentage
    
    return mood_percentages

def mood_summary(mood_percentages):
    # Display the summary of mood percentages
    print("\nWeekly Mood Summary:")
    for mood, percentage in mood_percentages.items():
        print(f"{mood.capitalize()}: {percentage:.2f}%")

def main():
    # Step 1: Get mood input for each day of the week
    moods = get_mood_for_week()
    
    # Step 2:Calculate the percentage of each mood
    mood_percentages = calculate_mood_percentage(moods)
    
    # Step 3 : Display the mood summary
    mood_summary(mood_percentages)

if __name__ == "__main__":
    main()
