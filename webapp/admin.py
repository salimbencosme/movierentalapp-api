from django.contrib import admin

from . models import Movie
from . models import User
from . models import Rent
from . models import RentMovies

admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Rent)
admin.site.register(RentMovies)
