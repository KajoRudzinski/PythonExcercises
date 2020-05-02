# doc string example >>> documentation method

class Song
    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist obejct representing the songs creator
        duration (int): the duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): An Artist objectL
            duration will default to 0 if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration
    