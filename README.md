# Movie Trailer Website Maker

This is a project to generate an HTML file containing your favorite movie trailers.



## Get Started

1. Clone this repo

2. Make sure you've installed python 3 in your environment

3. `cd ../[path_for_this_project]`

4. Generate and open an HTML file by `$ python entertainment_center.py`

    * Note:

        *an HTML file called `fresh_tomatoes.html` can be found in the folder

        *you can revisit the website by just opening this html

5. Click the poster of the movie and the trailer shows up




## Make Your Own

1. Add your own movie trailers in **_movie_trailers.json_**

    * Data Format:

        * `title`: the object name
        * `storyline`: the object's property
        * `poster_image_url`: the object's property
        * `trailer_youtube_url`: the object's property

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

2. Follow the instructions (2 to 5) from `Get Started` part.




