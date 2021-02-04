class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  # Created a getter method for the title attribute to print current song title, called get_title
  def get_title(self):
    return self.__title
  
  
  # Create a setter method for the next_song attribute stes new value for self.__title, called set_title.
  def set_title(self, title):
    self.__title = title


  # Created a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self.__next_song


  # Created a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    self.__next_song = next_title


  # Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return str(self.__title)


  # Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    return f'{self.__title} -> {self.__next_song}'


# rap = Song("Rockstar")
# rap.set_title("Test1")
# rap.set_next_song('Test2')
# rap.get_next_song()
# rap.__str__()
# rap.__repr__()
# rap.get_title()
