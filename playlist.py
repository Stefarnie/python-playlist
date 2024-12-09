playlist = {}  # Dictionary to store the playlist

# Function to add song to the playlist
def add_song(title, artist, genre):
    playlist[title] = {"artist": artist, "genre": genre}

# Function to view the playlist
def view_playlist():
    print("Current Playlist:", playlist)

# Function to delete a song from the playlist
def delete_song():
    song_to_delete = input("Enter the song you want to delete: ")
    if song_to_delete in playlist:
        del playlist[song_to_delete]
        print(f"The song '{song_to_delete}' has been deleted")
    else:
        print(f"The song '{song_to_delete}' is not found in the playlist")

# Main function to ask for song details
def ask_for_song():
    while True:
        title = input("Enter the song title (or type 'x' to stop): ")
        if title.lower() == 'x':  # If 'x' is entered, stop the loop
            break
        
        artist = input("Enter the artist's name: ")
        genre = input("Enter the genre of this song: ")
        
        # Adding the song to the playlist
        add_song(title, artist, genre)
        print(f"Song added: {title} by {artist}, Genre: {genre}")
        view_playlist()  # Display the current playlist

    # Ask if the user wants to delete a song
    get_song = input("To stop adding songs to the playlist type 'stop' or 'd' to delete a song: ")
    if get_song.lower() == "stop":
        print("Your playlist is complete, here it is:")
        view_playlist()
    elif get_song.lower() == "d":
        delete_song()
        ask_for_song()  # Ask for songs again after deletion
    else:
        ask_for_song()  # Continue if user does not type 'stop' or 'd'

# Start the function to add songs
ask_for_song()
