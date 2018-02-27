# Movie Trailer Website Maker

This is a project to generate an HTML file containing your favorite movie trailers.

## Get Started

1. Clone this repo

2. `cd ../[path_for_this_project]`

3. Generate an HTML file by `$ python fresh_tomatoes.py`

4. Open the file **_fresh_tomatoes.html_**

5. Click the poster of the movie and the trailer shows up

## Make Your Own

1. Add your own moview trailers in **_movie_trailers.json_**

    * Data Format:

        * _title_: the object name
        * _storyline_: the object's property
        * _poster_image_url_: the object's property
        * _trailer_youtube_url_: the object's property

            ```sh
            "(title of the movie)": {
                "storyline": "(the storyline of the movie)",
                "poster_image_url": "(the url for the poster image)",
                "trailer_youtube_url": "(the url for the movie trailer)"
            }
            ```
        * Example:
    
            ```sh
             "Avatar": {
                "storyline": "AVATAR takes us to a spectacular world",
                "poster_image_url": "https://goo.gl/NPEcNJ",
                "trailer_youtube_url": "https://www.youtube.com/watch?v=5PSNL1qE6VY"
              }
            ```

2. Follow the instructions from `Get Started` part.