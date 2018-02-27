
class Movie(object):
    '''
    A class to hold the information about a movie, including the title, storyline, poster image and its trailor
    '''

    def __init__(self, title, storyline, poster_image_url, trailor_youtube_url):

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailor_youtube_url
