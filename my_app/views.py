from django.shortcuts import render
from .models import Person
from django.http import HttpResponseRedirect
from .forms import PersonForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
        person = form.save(commit = False)
        person.user = request.user
        person.save()

    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    persons = Person.objects.filter(user = user)
    return render(request, 'profile.html', {'username': username, 'persons': persons})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print('The account has been disabled!')
            else:
                print('The username or password is incorrect.')

    else:
        form = LoginForm()
        return render(request, 'user_login.html', { 'form' : form })


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
