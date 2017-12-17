from rest_framework import serializers
from . models import Movie
from . models import User
from . models import Rent
from . models import RentMovies

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Movie
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields='__all__'


class RentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Rent
        fields='__all__'
        depth = 1


class RentMoviesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=RentMovies
        fields='__all__'
        depth = 2

