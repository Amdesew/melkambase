from django.shortcuts import render, redirect
from melkamapp.models import natural_products, car_spare_part, orders, samples
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from rest_framework import viewsets, status
from melkamapp.serializers import OrdersSerializer, SamplesSerializer, CraSparePartSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

def logein(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("successfully Loged In")
                return redirect('/order')
            else:
                return redirect('/logein')
        else:
            print("Form Is Invalid")
    else:
        form = AuthenticationForm()
    
    return render(request, 'home.html', {"form": form})

def home(request):
    return render(request, 'order.html')

ImageForm = ['image_link', 'image_title', 'image_price']

def natural_form(request):
    natural = natural_products.objects.all()

    if request.method == 'POST':
        item_img = request.POST['image_link']
        item_title = request.POST['image_title']
        item_price = request.POST['image_price']

        natural = natural_products(
            item_img = item_img, 
            item_title = item_title, 
            item_disc = item_price
        )
        
        natural.save()  # Save the form data to the database
        return redirect('/')  # Redirect to a success page or another view
    else:
        print("Failed")

    return render(request, 'natural_form.html')

def spare_form(request):
    car = car_spare_part.objects.all()

    if request.method == 'POST':
        item_img = request.POST['image_link']
        item_title = request.POST['image_title']
        item_price = request.POST['image_price']

        car = car_spare(
            item_img = item_img, 
            item_title = item_title, 
            item_disc = item_price
        )
        
        car.save()  # Save the form data to the database
        return redirect('/')  # Redirect to a success page or another view
    else:
        print("Failed")

    return render(request, 'spare_form.html')

class OrderViewSet(ModelViewSet):
    queryset = orders.objects.all()
    serializer_class = OrdersSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def csrf_token(request):
        token = get_token(request)
        return JsonResponse({'csrfToken': token})

class samplesViewSet(ModelViewSet):
    queryset = samples.objects.all()
    serializer_class = SamplesSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def csrf_token(request):
        token = get_token(request)
        return JsonResponse({'csrfToken': token})

class CarSpareViewSet(ModelViewSet):
    queryset = car_spare_part.objects.all()
    serializer_class = CraSparePartSerializer

    def create(self, request, *args, **kwars):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def csrf_token(request):
        token = get_token(request)
        return JsonResponse({'csrfToken': token})