from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Movie
from . models import User
from . models import Rent
from . models import RentMovies
from . serializers import MovieSerializer
from . serializers import UserSerializer
from . serializers import RentSerializer
from . serializers import RentMoviesSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.db.models import Prefetch

class MovieService(APIView):

    def get(self,request):
        movies = Movie.objects.all().filter(active=True).order_by('-year')
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    

class UserService(APIView):
    
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def get_one(request,usernameparam,passwordparam):
        users = User.objects.get(username = usernameparam,password = passwordparam)
        serializer = UserSerializer(users)
        return HttpResponse(JSONRenderer().render(serializer.data), content_type="application/json")

class RentService(APIView):

    def get(self,request):
        rents = Rent.objects.all()
        serializer = RentSerializer(rents,many=True)
        return Response(serializer.data)


    @csrf_exempt
    def post(request):

        if(Rent.objects.count()>0):
            objrent = Rent.objects.latest('rentid')
            objrent = objrent.rentid
        else:
            objrent = 0

        data = JSONParser().parse(request)
        userregister = User.objects.get(userid = data['userid'])
        
        newrent = Rent(rentid=(objrent+1),user = userregister,renteddate = datetime.now(),totalamount = data['totalamount'],haspenalty=False,inprocess=True)
        newrent.save()

        for movieidtemp in data['movieids']:
            if(RentMovies.objects.count()>0):
                objrentmovies = RentMovies.objects.latest('rentmoviesid')
                objrentmovies = objrentmovies.rentmoviesid 
            else:
                objrentmovies = 0

            movietemp = Movie.objects.get(movieid = movieidtemp)
            newrentmovie = RentMovies(rentmoviesid = (objrentmovies + 1),rent = newrent, movie = movietemp)
            newrentmovie.save()

        return HttpResponse(JSONRenderer().render({'rentid':(newrent.rentid)}), content_type="application/json")

    @csrf_exempt

    def put(request):
        data = JSONParser().parse(request)
        renttemp = Rent.objects.get(rentid=data['rentid'])
        renttemp.delivereddate = datetime.now()
        renttemp.totalamount = data['totalamount']
        renttemp.haspenalty=data['haspenalty']
        renttemp.inprocess=False
        renttemp.save()
        return HttpResponse(JSONRenderer().render({'rentid':(renttemp.rentid)}), content_type="application/json")



class RentMoviesService(APIView):

    def get(self,request):
        rentmovie = RentMovies.objects.all()
        serializer = RentMoviesSerializer(rentmovie,many=True)
            
        return Response(serializer.data)

    def get_by_userid(request,useridparam):
        rentmovies_records=[]
        rents = Rent.objects.filter(user = useridparam).filter(active = True).values('rentid').order_by('-renteddate')
        serializerrentobj = RentSerializer(rents,many=True)
        
        for data in serializerrentobj.data:
            rentmovie = RentMovies.objects.filter(rent = data['rentid'])
            rentmovies_records.append(RentMoviesSerializer(rentmovie,many=True).data)

        return HttpResponse(JSONRenderer().render(rentmovies_records), content_type="application/json")
    
    def get_all_inprocess(request):
        rentmovies_records=[]
        rents = Rent.objects.filter(inprocess = True).filter(active = True).values('rentid').order_by('-renteddate')
        serializerrentobj = RentSerializer(rents,many=True)
        
        for data in serializerrentobj.data:
            rentmovie = RentMovies.objects.filter(rent = data['rentid'])
            rentmovies_records.append(RentMoviesSerializer(rentmovie,many=True).data)

        return HttpResponse(JSONRenderer().render(rentmovies_records), content_type="application/json")

    def get_all_processed(request):
        rentmovies_records=[]
        rents = Rent.objects.filter(inprocess = False).filter(active = True).values('rentid').order_by('-delivereddate')
        serializerrentobj = RentSerializer(rents,many=True)
        
        for data in serializerrentobj.data:
            rentmovie = RentMovies.objects.filter(rent = data['rentid'])
            rentmovies_records.append(RentMoviesSerializer(rentmovie,many=True).data)

        return HttpResponse(JSONRenderer().render(rentmovies_records), content_type="application/json")