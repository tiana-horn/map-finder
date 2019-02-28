from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import Http404
# from users.models import FarmMap, Farmer, User
# from users.forms import FarmMapForm



# Create your views here.
def request_map(request):
    form_class = FarmMapForm
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            farm_map = form.save(commit=False)
            # farm_map.farmer = request.user
            farm_map.save()
            return redirect("farm_datamap", slug=farm_datamap.pk)
    else: 
        form = form_class()

    return render(request, 'user/farm_application.html', {
        "form":form,
    })

def farm_datamap(request):
    farm_map = FarmMap.objects.get(slug=slug)
    return render(request, 'user/farm_datamap.html', {
        'farm_map': farm_map,
    })

            
