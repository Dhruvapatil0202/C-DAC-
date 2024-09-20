import sys
playlist = []
user_options = """
1. Add Song
2. Remove Song
3. View all snogs
4. Slice playlist
5. exit
"""

def add_songs():
    user_input = input("\nEnter songs (comma separated): ").strip()
    playlist.extend([song.strip() for song in user_input.split(",")])
    print("Your songs are added successfully! ")

def remove_song():
    for ind, song in enumerate(playlist, 1):
        print(f"{ind}. {song}")
    song_to_remove = input("\nEnter song you want to remove:").strip()
    if song_to_remove in playlist:
        playlist.remove(song_to_remove)
    print('Song Removed successfully!')
def view_all_songs():

    print(f"\nYour playlist is : \n{', '.join(playlist)}")

def slice_playlist():
    input_indices = input("\nEnter starting and ending indices of your playlist (comma separated): ").strip()
    if input_indices.count(",") != 1:
        print("Invalid Input")
        return

    start, end = input_indices.split(',')
    if not start.isdigit() or not end.isdigit():
        print("Inputted values are not valid")

    start, end = start.strip(), end.strip()
    start, end = int(start), int(end)

    if not 0 <= start < len(playlist) or not 0 <= end < len(playlist)  or start >= end:
        print("Inputted values are out of range. ")
        return

    print("Your portion of playlist: ")
    for ind, song in enumerate(playlist[start - 1: end], start):
        print(f"{ind}. {song}")

if __name__ == "__main__":
    while True:
        user_input = input(f"\n{user_options}\nEnter you Choice: ").strip()
        match user_input:
            case '1':
                add_songs()
            case '2':
                remove_song()
            case '3':
                view_all_songs()
            case '4':
                slice_playlist()
            case '5':
                sys.exit()
            case _:
                print("Invalid input, Try again")

    pass