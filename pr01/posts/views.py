from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Galaxy, Object, System
from django.shortcuts import render
from .forms import GalaxiesForm, SystemsForm, ObjectsForm
# Create your views here.

def index(request):
    galaxies = Galaxy.objects.all()
    objects = Object.objects.all()
    systems = System.objects.all()

    if request.method == 'POST':
        if request.POST.get("postId", "")=="3":
            form = GalaxiesForm(request.POST)
            if form.is_valid():
                form.save()
        if request.POST.get("postId", "")=="2":
            form = SystemsForm(request.POST)
            if form.is_valid():
                form.save()
        if request.POST.get("postId", "")=="1":
            form = ObjectsForm(request.POST)
            if form.is_valid():
                form.save()
        if request.POST.get("postId", "")=="4":
            record = Object.objects.get(id=int(request.POST["id"]))
            record.delete()
        if request.POST.get("postId", "")=="5":
            record = System.objects.get(system_name=request.POST["system_name"])
            record.delete()
        if request.POST.get("postId", "")=="6":
            record = Galaxy.objects.get(galaxy_name=request.POST["galaxy_name"])
            record.delete()
    form_galaxy = GalaxiesForm()
    form_system = SystemsForm()
    form_object = ObjectsForm()
    return render(request, 'posts/index.html', {'galaxies':galaxies, 
                                                'objects':objects, 
                                                'systems':systems, 
                                                'form_galaxy':form_galaxy, 
                                                'form_system':form_system, 
                                                'form_object':form_object})
