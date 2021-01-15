from django.shortcuts import render,redirect
from.models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
import datetime

def homepage(request):
    last5 = FoodTruck.objects.all().order_by('-id')[:5]
    now = datetime.datetime.now().strftime('%H:%M:%S')
    return render(request,'home.html',{"trucks":last5,"current_time":now})

'''Listing for all the trucks'''

def alltrucks(request):
    query = request.GET.get('trucksearch')
    page = request.GET.get('page',1)

    
    if query:
        trucks = FoodTruck.objects.filter(Q(foodtype__foodtype__icontains = query) | Q(location__icontains = query))
    else:
        trucks = FoodTruck.objects.all()

    paginator = Paginator(trucks,5)
    now = datetime.datetime.now().strftime('%H:%M:%S')
    try:
        truck = paginator.page(page)
    except PageNotAnInteger:
        truck = paginator.page(1)
    except EmptyPage:
        truck = paginator.page(paginator.num_pages)
    return render(request,'foodtrucks/alltruck.html',{"trucks":truck,"current_time":now})

''' Adding New truck'''

def addtruck(request):
    foodtype = FoodType.objects.all()
    truck_dict = {}
    if request.method == 'POST':
        print(request.POST.get('image'))
        truck = FoodTruck.objects.create(
            foodtype = FoodType.objects.get(id=request.POST.get('foodtype')),
            location = request.POST.get('location'),
            owner_name = request.POST.get('owner_name'),
            truck_image = request.FILES['image'],
            opening_time = request.POST.get('open_time'),
            closing_time = request.POST.get('close_time')
        )
        truck.save()
        return redirect('foodtrucks:alltrucks')
    return render(request,'foodtrucks/addtruck.html',{"foodtype":foodtype})


'''Edit Truck Details'''

def edit(request,truck_id):
    foodtruck = FoodTruck.objects.get(id=truck_id)
    foodtype = FoodType.objects.all()
    if request.method == 'POST':
        foodtruck.foodtype = FoodType.objects.get(id=request.POST.get('foodtype'))
        foodtruck.location = request.POST.get('location')
        foodtruck.owner_name = request.POST.get('owner_name')
        if request.FILES.get('image'):
            foodtruck.truck_image = request.FILES['image']
        foodtruck.opening_time = request.POST.get('open_time')
        foodtruck.closing_time = request.POST.get('close_time')
        foodtruck.save()
        return redirect('foodtrucks:edit',truck_id=truck_id)
    return render(request,'foodtrucks/truckedit.html',{"foodtruck":foodtruck,
                                                        "foodtype":foodtype})



def deletetruck(request,truck_id):
    foodtruck = FoodTruck.objects.get(id=truck_id)
    foodtruck.delete()
    return redirect('foodtrucks:alltrucks')



