# Netlifer

The name of the project is Netlifer

## Description

The project is about showing the latest movies and tv-series, giving details about them and showing their trailers through the youtube api. Search for any movie or tv series available in the moviedb database no matter the year or country. 

## Technologies Used

- Django
- Python3
- YouTube Data API-v3
- MovieDb Api
- Javascript

## User Stories

- Get the latest movies
- Get the latest series
- Search for any movie or tv-series 
- Get trailer for all movies and tv series
- Get details of any movie or tv series 

## Installation

- First go to Google Developers page login and create a new project.
    [Google developer](https://console.developers.google.com/)

- Then go to Enable Api and Services and find YouTube Data API-v3, enable it, then create credentials then you will get the youtube api key.

- Go to The Movie Database (TMDB) sign up and request for an api key
    [Movie Database](https://developers.themoviedb.org/3/getting-started/introduction)

- Git clone the project in your repository
    ```
    git clone https://github.com/Mash14/Netlifer.git
    ```

- Create an .env file in the root of the project 
    ```
    API_KEY='<your-movie-db-api-key>'
    YOUTUBE_API_KEY='<your-youtube-api-key>'
    ```

- Create a virtual environment and run it
    ```
    sudo apt install python3-virtualenv

    virtualenv virtual
    
    source virtual/bin/activate
    ```

- Install python package dependencies in the requirements.txt file
    ```
    pip install -r requirements.txt
    ```

- Run the application
    ```
    python3 manage.py runserver
    ```

## Screenshots

 Home Page
![Home Page](/static/img/home.png)

 Single Movie
![Single Movie](/static/img/single_movie.png)

 Search Movies Page
![Search Movies](/static/img/search.png)

## Developer's Details

The author of this project was Alan Macharia

## Contact information

You can reach the developer by:
- Email: mashalonzo741@gmail.com
- Tel: 0704485919 

## Known Bugs

There are no known bugs 

## License and Copyright information

The license information can be found here: [MIT-Lisence](https://opensource.org/licenses/MIT)

Copyright (c)_18/12/2022__Alan Macharia_
