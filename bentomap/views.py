from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
from foodevent.models import FoodEvent


def home(request):

	if "create_event" in request.POST:
		place = request.POST['food_place']
		resource = request.POST['food_object']
		description = request.POST['food_description']
		amount = request.POST['food_amount']
		time = datetime.now()
		lon = request.POST['lon']
		lat = request.POST['lat']
		FoodEvent.objects.create(place=place, resource=resource, amount= amount, description=description, time=time,lon=lon,lat=lat)
		
	return render(request, 'home.html', locals())

def food(request):
	foodevents = FoodEvent.objects.all().order_by('id')
	print(request.POST)
	if "pai" in request.POST:
		foodid = request.POST['pai']
		foodamount = int(request.POST['amount'])
		FoodEvent.objects.filter(id = foodid).update(amount = foodamount - 1)

	return render(request, 'food.html', locals())

def index(request):
    # from haversine import haversine
    points_all = FoodEvent.objects.all()
    points = []
    points.extend(points_all)
    # result_list = []
    # # your_location = (YOUR_LATITUDE,YOUR_LONGITUDE)
    # for point in all_points:
    #     point_loc = (FoodEvent.lat,FoodEvent.lon)
    #     if(haversine(you,point_loc)<1):
    #         #print point
    #         result_list.append(point)
    # custom_list = [rec.id for rec in result_list]
    # points = FoodEvent.objects.filter(id__in=custom_list)
    return render(request,"index.html",{'points':points})
