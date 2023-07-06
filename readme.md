# IMDb API Clone

This is a clone of the IMDb (Internet Movie Database) API built using Django and Django REST Framework. It allows users to access movie and TV show information, including details about cast, crew, ratings, and more.

# Routes

![image](https://github.com/piyush310/imdb-api/assets/39629176/8dc71436-ab9d-4789-95ce-26d011e54640)





## Features

- **Search**: Users can search for movies and TV shows using various criteria such as title, genre, year, etc.
- **Movie Details**: Users can retrieve detailed information about a specific movie or TV show, including cast, crew, ratings, plot summary, and more.
- **Top Rated**: Users can view the top-rated movies and TV shows based on user ratings.
- **User Ratings**: Registered users can rate movies and TV shows, and their ratings will contribute to the overall rating for each title.
- **Authentication**: User registration and authentication system is implemented to allow secure access to certain features such as rating movies.
- **swaggerUI**: Swagger UI integrated to use API routes easily

## Technologies Used

- Python 3.x
- Django 3.x
- Django REST Framework 3.x
- MySQL (or any other database supported by Django)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/piyush310/imdb-api-clone.git
   ```

2. Create a virtual environment:

   ```shell
    python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```shell
    source venv/bin/activate
   ```

4. Install the dependencies:

   ```shell
    pip install -r requirements.txt
   ```

5. Setup the database:

- Update the database settings in imdb/settings.py to match your database configuration.

- Apply migrations:

  ```shell
   python manage.py migrate
  ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. Access the API at

   ```shell
   http://localhost:8000/docs
   or
   http://localhost:8000/redoc
   ```
## or 

1. Clone the repository:

   ```shell
   git clone https://github.com/piyush310/imdb-api-clone.git
   ```

2. Docker build
   ```shell
   docker build --no-cache -t imdb-app .
   ```

3. Run docker image
   ```
   docker run -p 8000:8000 imdb-app
   ```

4. Access the API at

   ```shell
   http://localhost:8000/docs
   or
   http://localhost:8000/redoc
   ```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request detailing your changes.

## Acknowledgements

This project was inspired by the IMDb website and API.

## Contact

If you have any questions or suggestions, feel free to contact
