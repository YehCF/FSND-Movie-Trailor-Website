import json
import media
import fresh_tomatoes

def extract_movie_trailers_from_json(movies_josn_file):
    '''
    Extract info about movie trailers from a json file (movie_trailers.json in this case)
    :param movies_josn_file: the path to open the json file (.json)
    :return:
        a list of movie trailers, which are dictionaires
    '''

    movie_list = []

    with open(movies_josn_file) as f:

        movie_trailers = json.load(f)

        for movie_title, movie_trailer in movie_trailers.items():
            movie = {
                'title': movie_title,
                'storyline': movie_trailer['storyline'],
                'poster_image_url': movie_trailer['poster_image_url'],
                'trailer_youtube_url': movie_trailer['trailer_youtube_url']
            }
            movie_list.append(movie)

    return movie_list

def create_movies(movie_list):
    '''
    Create a list of movie objects from a list of movie dictionaries
    :param movie_list: a list of movie dictionaries, containing the info about movies
        including title, storyline, poster_image_url and youtube_trailer_url
    :return:
        a list of Movie objects
    '''
    movie_objects = []
    for movie in movie_list:
        movie_object = media.Movie(title=movie['title'],
                                   storyline=movie['storyline'],
                                   poster_image_url=movie['poster_image_url'],
                                   trailer_youtube_url=movie['trailer_youtube_url'])
        movie_objects.append(movie_object)

    return movie_objects

if __name__ == '__main__':

    # extract infos from movie_trailers.json
    json_path = "movie_trailers.json"
    movie_list = extract_movie_trailers_from_json(json_path)

    # create movie objects
    movie_objects = create_movies(movie_list)

    # generate and open the movie trailer HTML
    fresh_tomatoes.open_movies_page(movie_objects)