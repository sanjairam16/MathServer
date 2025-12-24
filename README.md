# Ex.04 Design a Website for Server Side Processing
## Date: 24.12.2025
## REFNO: 25009774

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
url.py
~~~
from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path("", views.lamp_power, name="lamp_power"),
]
~~~
views.py
~~~
from django.shortcuts import render
def lamp_power(request):
    power = None
    if request.method == "POST":
        try:
            I = float(request.POST.get("intensity", 0))
            R = float(request.POST.get("resistance", 0))
            power = (I ** 2) * R
        except ValueError:
            power = "Invalid input"
    return render(request, "mathapp/math.html", {"power": power})


~~~


## OUTPUT - SERVER SIDE:


## OUTPUT - WEBPAGE:
![alt text](<../Screenshot 2025-12-24 103329.png>)


## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
