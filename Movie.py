import random

# Movie dictionary
movies = {
    "The Shawshank Redemption": 9.5,
    "Pulp Fiction": 8.8,
    "The Room": 3.6,
    "The Godfather": 9.2,
}


# Function to list all movies
def list_of_movies(movies):
    if not movies:
        print("\n📌 No movies in the list.")
        return

    print(f"\n🎬 {len(movies)} movies in total:")
    for title, rating in movies.items():
        print(f"{title}: {rating}")


# Function to add or update a movie
def add_movie(movies):
    movie_name = input("\nEnter the movie name: ")
    while True:
        try:
            rating = float(input("Enter a rating (1-10): "))
            if 1 <= rating <= 10:
                break
            else:
                print("❌ Rating must be between 1 and 10. Try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    if movie_name in movies:
        print(f"⚠️ Movie '{movie_name}' already exists! Updating the rating.")
    else:
        print(f"✅ Adding new movie: {movie_name}")

    movies[movie_name] = rating
    print(f"📌 Movie '{movie_name}' is now rated {rating}.")


# Function to delete a movie
def delete_movie(movies):
    movie_name = input("\nEnter the movie name to delete: ")

    if movie_name in movies:
        del movies[movie_name]
        print(f"🗑️ Movie '{movie_name}' has been deleted.")
    else:
        print(f"❌ Movie '{movie_name}' not found.")


# Function to calculate and display movie statistics
def update_stats(movies):
    if not movies:
        print("\n📌 No movies in the list.")
        return

    total_movies = len(movies)
    ratings = list(movies.values())
    sorted_ratings = sorted(ratings)

    # Average rating
    average_rating = sum(ratings) / total_movies

    # Median rating
    mid = total_movies // 2
    if total_movies % 2 == 0:  # Even number of movies
        median_rating = (sorted_ratings[mid - 1] + sorted_ratings[mid]) / 2
    else:  # Odd number of movies
        median_rating = sorted_ratings[mid]

    # Best movie(s) by rating
    max_rating = max(ratings)
    best_movies = [title for title, rating in movies.items() if rating == max_rating]

    # Worst movie(s) by rating
    min_rating = min(ratings)
    worst_movies = [title for title, rating in movies.items() if rating == min_rating]

    # Display stats
    print("\n📊 Movie Statistics:")
    print(f"Total movies: {total_movies}")
    print(f"Average rating: {average_rating:.2f}")
    print(f"Median rating: {median_rating:.2f}")
    print(f"Best movie(s) by rating ({max_rating}): {', '.join(best_movies)}")
    print(f"Worst movie(s) by rating ({min_rating}): {', '.join(worst_movies)}")


# Function to pick a random movie
def random_movie(movies):
    if not movies:
        print("\n📌 No movies in the list.")
        return

    movie = random.choice(list(movies.keys()))
    print(f"\n🎲 Randomly picked movie: {movie} ({movies[movie]})")


# Function to search for a movie (case-insensitive)
def search_movie(movies):
    search_term = input("\nEnter the movie name to search: ").lower()
    found_movies = [title for title in movies.keys() if search_term in title.lower()]

    if found_movies:
        print("\n🔍 Search Results:")
        for title in found_movies:
            print(f"{title}: {movies[title]}")
    else:
        print(f"❌ No movies found with '{search_term}' in the name.")


# Function to sort movies by rating
def sort_movies_by_rating(movies):
    if not movies:
        print("\n📌 No movies in the list.")
        return

    # Sort movies by rating in descending order
    sorted_movies = sorted(movies.items(), key=lambda x: x[1], reverse=True)

    print("\n🎬 Movies sorted by rating (highest to lowest):")
    for title, rating in sorted_movies:
        print(f"{title}: {rating}")


# Function to display menu and get user choice
def menu():
    while True:
        print("\n📽️ Movie Menu")
        print("1️⃣ View movie list")
        print("2️⃣ Add or update a movie")
        print("3️⃣ Delete a movie")
        print("4️⃣ Update movie stats")
        print("5️⃣ Pick a random movie")
        print("6️⃣ Search for a movie")
        print("7️⃣ Sort movies by rating")
        print("8️⃣ Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            list_of_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            update_stats(movies)
        elif choice == "5":
            random_movie(movies)
        elif choice == "6":
            search_movie(movies)
        elif choice == "7":
            sort_movies_by_rating(movies)
        elif choice == "8":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1-8.")


# Run the menu function
if __name__ == "__main__":
    menu()
