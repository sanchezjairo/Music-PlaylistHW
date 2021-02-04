from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  #  creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song



  #  searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    present_song = self.__first_song
    index = 0

    while present_song != None:
      if present_song.get_title == title:
        index += 1
        return index
      
      if present_song.get_title() != title:
        index += 1
        present_song = present_song.get_next_song()
  



  #  removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    present_song = self.__first_song
    previous_song = self.__first_song


    if present_song.get_title() == title:
        self.__first_song = self.__first_song.get_next_song()
        return f"{present_song.get_title} has been deleted from playlist!"

    while present_song.get_title() != title:
      previous_song = present_song
      present_song = present_song.get_next_song()

      if present_song ==  None:
        return f'Sorry song not found.'


      
      # returns the number of songs in the playlist.

  def length(self):
    present_song = self.__first_song
    counter = 0

    while present_song != None:
      present_song = present_song.get_next_song
      counter += 1
      return counter


  #  prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    present_song = self.__first_song
    counter = 1

    while present_song != present_song:
      print(f'{counter}. {present_song} {counter}')
      counter += 1
      present_song = present_song
