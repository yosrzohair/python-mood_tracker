import csv

def read_songs(file_path):
    try:
        with open("songs.csv", mode="r")as file:
            reader = csv.DictReader(file)
            return list(reader) 
    except  FileNotFoundError:
        print ("file not found.")
        return []
    
def filter_by_genere(songs, genere):
    """Filters the list of songs by genre."""
    return [song for song in songs if song['Genre'].lower() == genere.lower()]

def filter_by_duration(songs, max_duration):
    """Filters songs by a maximum duration in minutes."""
    filtered_songs = []
    for song in songs:
        try:
            minutes, seconds = map(int, song["Duration"].split(":"))
            total_seconds = minutes * 60 + seconds
            if total_seconds <= max_duration * 60:  # Compare with max duration
                filtered_songs.append(song)
        except ValueError:
            print("Error: Invalid duration format in song . Skipping.")
    return filtered_songs

def display_songs(songs):
    """Displays the list of songs."""
    if not songs:
        print("No songs found.")
    else:
        for song in songs:
            print(f"Title: {song['Title']}, Artist: {song['Artist']}, Genre: {song['Genre']}, Duration: {song['Duration']} min")

##############

def main():
    file_path = "songs.csv"
    songs = read_songs(file_path)

    
    if not songs :
        return
    
    print("Welcome to the Song Filter!")
    while True:
        print("\nMenu:")
        print("1. Filter by Genre")
        print("2. Filter by Duration")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            genere = input("Enter the genre to filter by: ").strip()
            filtered_songs = filter_by_genere(songs, genere)
            display_songs(filtered_songs)

        elif choice == "2":
            try:
                max_duration = float(input("Enter maximum duration (in minutes): "))
                filtered_songs = filter_by_duration(songs, max_duration)
                display_songs(filtered_songs)
            except ValueError:
                print("Invalid input. Please enter a numeric value for duration.")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()