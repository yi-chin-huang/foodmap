from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
from foodevent.models import FoodEvent, Place
from django.contrib.auth.decorators import login_required
import math

# @login_required
def home(request):

	if "create_event" in request.POST:
		place = request.POST['food_place']
		resource = request.POST['food_object']
		description = request.POST['food_description']
		amount = int(request.POST['food_amount'])
		pai_amount = 0
		time = datetime.now()
		lng = request.POST['lng']
		lat = request.POST['lat']
		provider = request.user
		FoodEvent.objects.create(place=place, resource=resource, amount= amount, pai_amount = pai_amount, description=description, time=time, provider = provider,lon=lng,lat=lat)
		return redirect("/food/")
	return render(request, 'home.html', locals())
# @login_required(login_url='/accounts/')
def count_dis(base_lng, base_lat, lng, lat):

    lon1, lat1, lon2, lat2 = map(math.radians, [base_lng, base_lat, lng, lat])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2) ** 2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371
    return c * r 
def food(request):
	if "myplace" in request.POST:
		myplace = request.POST['myplace']
		place = Place.objects.get(name=myplace)
		unsort_foodevents = FoodEvent.objects.all().order_by('id')
		dist = []
		for i in unsort_foodevents:
			dist.append(count_dis(i.lon,i.lat,place.lon,place.lat))
		foodevents = [x for _,x in sorted(zip(dist,unsort_foodevents))]
	else:
		foodevents = FoodEvent.objects.all().order_by('id')
	if "pai" in request.POST:
		foodid = request.POST['pai']
		food = FoodEvent.objects.get(id = foodid)
		foodamount = food.pai_amount
		FoodEvent.objects.filter(id = foodid).update(pai_amount = foodamount + 1)
	if "finish" in request.POST:
		foodid = request.POST['finish']
		FoodEvent.objects.filter(id = foodid).delete()
	if "edit_amount" in request.POST:
		fid = request.POST['fid']
		new_amount = request.POST['edit_amount']
		FoodEvent.objects.filter(id = fid).update(amount = new_amount)

	return render(request, 'food.html', locals())
# @login_required
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
