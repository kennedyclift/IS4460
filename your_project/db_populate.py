import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from movie.models import Movie, User

# Empty all existing rows from the tables
Movie.objects.all().delete()
User.objects.all().delete()

# Add 10 movie rows
for i in range(1, 11):
    Movie.objects.create(
        title=f'Movie {i}',
        description=f'Description for Movie {i}',
        director=f'Director {i}',
        release_year=2000 + i,
        budget=1000000 * i,
        runtime=120 + i,
        rating=5.0,
        genre='Action'
    )

# Add 3 user rows
for i in range(1, 4):
    User.objects.create(
        username=f'user{i}',
        password=f'password{i}',
        first_name=f'User{i}',
        last_name=f'Lastname{i}',
        email=f'user{i}@example.com'
    )
