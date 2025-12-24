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

