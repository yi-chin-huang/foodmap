from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from foodevent.models import FoodEvent, Place, TakeFood
from django.contrib.auth.decorators import login_required
import math
import pytz

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
		FoodEvent.objects.create(place=place, resource=resource, amount= amount, pai_amount = pai_amount, description=description, time=time, provider=provider,lon=lng,lat=lat)
		return redirect("/food/")
	return render(request, 'home.html', locals())

def count_dis(base_lng, base_lat, lng, lat):

    lon1, lat1, lon2, lat2 = map(math.radians, [base_lng, base_lat, lng, lat])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2) ** 2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371
    return c * r 
# @login_required(login_url='/accounts/')
def food(request):
	# food = FoodEvent.objects.get(id = foodid)	
	if "myplace" in request.POST:
		myplace = request.POST['myplace']
		if myplace == "新體":
			place = Place.objects.create(place=myplace,lon=121.535274,lat=25.021981)
		elif myplace == "社科":
			place = Place.objects.create(place=myplace,lon=121.542431,lat=25.020963)
		elif myplace == "管院":
			place = Place.objects.create(place=myplace,lon=121.543333,lat=25.020953)
		else:
			place = Place.objects.get(place = myplace)
		unsort_foodevents = FoodEvent.objects.all()
		dist = []
		for i in unsort_foodevents:
			dist.append(count_dis(i.lon,i.lat,place.lon,place.lat))
		foodevents = [x for _,x in sorted(zip(dist,unsort_foodevents))]
	else:
		foodevents = FoodEvent.objects.all().order_by('id')	
	all_place = Place.objects.all()

	# all_place = Place.objects.all()
	if "pai" in request.POST:
		taker = request.user
		foodid = request.POST['pai']
		food = FoodEvent.objects.get(id = foodid)
		foodamount = food.pai_amount
		FoodEvent.objects.filter(id = foodid).update(pai_amount = foodamount + 1)
		exp_time = (datetime.now() + timedelta(minutes = int(request.POST['expected_time'])))
		TakeFood.objects.create(taker = taker, food = food, exp_time = exp_time)

	if "finish" in request.POST:
		foodid = request.POST['finish']
		FoodEvent.objects.filter(id = foodid).delete()
	if "edit_amount" in request.POST:
		fid = request.POST['fid']
		new_amount = request.POST['edit_amount']
		FoodEvent.objects.filter(id = fid).update(amount = new_amount)

	my_food = FoodEvent.objects.filter(provider = request.user)
	take_food = TakeFood.objects.filter(food__in = my_food).order_by('exp_time')

	if "taken_food" in request.POST:
		taken_foodid = request.POST['taken_food']
		taken_time = datetime.now().astimezone(pytz.timezone('Asia/Taipei'))
		exp_taken_time = TakeFood.objects.get(id = taken_foodid).exp_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Taipei'))
		print(taken_time - exp_taken_time)
		if taken_time <= exp_taken_time:
			rating = 10
		else:
			rating = max(0,10-((taken_time - exp_taken_time).seconds/60)//5)
			print("taken: ", taken_time)
			print("exp: ", exp_taken_time)
			print("delta: ", (taken_time - exp_taken_time).seconds/3600)
			# print((taken_time - exp_taken_time).seconds/60)
			print((taken_time - exp_taken_time).seconds/60)

		TakeFood.objects.filter(id = taken_foodid).update(rating = rating)




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
def place(request):
	if "create_place" in request.POST:
		place = request.POST['myplace']
		lng = request.POST['lng']
		lat = request.POST['lat']
		Place.objects.create(place=place,lon=lng,lat=lat)
		all_place = Place.objects.all()
	return render(request, 'place.html', locals())



