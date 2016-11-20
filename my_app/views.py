from django.shortcuts import render
from .models import Person
from django.http import HttpResponseRedirect
from .forms import PersonForm
# Create your views here.
def index(request):
    persons = Person.objects.all()
    form = PersonForm()
    return render(request, 'index.html', {'persons': persons, 'form': form} )

def detail(request, person_id):
    person = Person.objects.get(id = person_id)
    return render(request, 'detail.html', {'person': person})

def post_person(request):
    form = PersonForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = True)

    return HttpResponseRedirect('/')
