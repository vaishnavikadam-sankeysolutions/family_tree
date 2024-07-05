# tree/views.py

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tree:home')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def person_list(request):
    persons = Person.objects.all()
    data = []
    for person in persons:
        data.append({
            'id': person.id,
            'name': person.name,
            'image_url': person.image.url if person.image else '',
            'parent_id': person.parent.id if person.parent else None,
            'spouse_id': person.spouse.id if person.spouse else None,
        })
    return JsonResponse(data, safe=False)




