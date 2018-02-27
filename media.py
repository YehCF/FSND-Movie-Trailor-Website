
class Movie(object):
    '''
    A class to hold the information about a movie, including the title, storyline, poster image and its trailer
    '''

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        # title, storyline, poster_image_url and trailer_youtube_url are needed for instantiation
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
