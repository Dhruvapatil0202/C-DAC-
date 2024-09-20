import sys
movie_vote_dict = {}

options = """
1. Add New Movie:
2. Vote for Movie:
3. Remove a movie:
4. Display voting results:
5. Find the top movie:
6. Exit
"""

def add_new_movie():
    new_movie_name = input("\nEnter the movie name: ")
    if new_movie_name in movie_vote_dict:
        print("The movie is already present in voting system.")
        return
    movie_vote_dict[new_movie_name] = 0

def vote_for_movie():
    # Displaying movies:
    for index, movie in enumerate(movie_vote_dict.keys(), start = 1):
        print(f"{index}. {movie}")

    voted_movie_name = input("\nEnter name of movie you want to vote: ")
    if voted_movie_name not in movie_vote_dict:
        print("Movie not in List, voting failed")
    else:
        movie_vote_dict[voted_movie_name] += 1
        print("Vote added successfully.")

def remove_a_movie():
    for index, movie in enumerate(movie_vote_dict.keys(), start = 1):
        print(f"{index}. {movie}")
    movie_name = input("\nEnter name of movie you want to remove.\n")
    if movie_name not in movie_vote_dict:
        print(f"{movie_name} is not present in current roster of movies.")
        return
    movie_vote_dict.pop(movie_name)
    print("\nMovie deleted successfully.")

def display_voting_results():
    print("\nCurrent movie vote status: ")
    for index, movie in enumerate(movie_vote_dict.keys(), 1):
        print(f"{index}. {movie} -> {movie_vote_dict[movie]} votes" )

def find_top_movie():
    print("\nThe current top movie is: ")
    best_movie = max(movie_vote_dict, key = movie_vote_dict.get)
    best_votes = movie_vote_dict[best_movie]
    print(f"{best_movie} with {best_votes} votes. ")

if __name__ == "__main__":
    while True:
        try:
            user_choice = int(input(f"\n{options} \nEnter your choice from above : ",))
            match user_choice:
                case 1:
                    add_new_movie()
                case 2:
                    vote_for_movie()
                case 3:
                    remove_a_movie()
                case 4:
                    display_voting_results()
                case 5:
                    find_top_movie()
                case 6:
                    sys.exit()
                case _:
                    print("Invalid Input Try again.\n")

        except Exception as error:
            print(f"The input is invalid, please try again.")

    pass
