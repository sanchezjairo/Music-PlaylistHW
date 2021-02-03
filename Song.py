class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  # TODO: Create a getter method for the title attribute, called get_title
  def get_title(self):
    return print(self.__title)
  
  
  # TODO: Create a setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    self.__title = title


  # TODO: Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return print(self.__next_song)


  # TODO: Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    self.__next_song = next_title


  # TODO: Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return print(f"Here's the song! {self.__title}" .format(self=self))


  # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    rep = print(self.__title + '->' + self.__next_song)
    return rep


rap = Song("Rockstar")
rap.set_title("Test1")
rap.set_next_song('Test2')
rap.get_next_song()
rap.__str__()
rap.__repr__()
