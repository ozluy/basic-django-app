from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html', {'persons': persons})


class Person:
    def __init__(self, name, age, experience, title, location, avatar):
        self.name = name
        self.experience = experience
        self.age = age
        self.title = title
        self.location = location
        self.avatar = avatar

persons = [
    Person('Jon Snow', 25, 2, 'Front-end Developer', 'Istanbul', 'jon_snow.png'),
    Person('Ned Stark', 46, 14, 'Software Architect', 'Ankara', 'ned_stark.png'),
    Person('Jaime Lannister', 28, 6, 'UI Designer', 'Izmir', 'jaime_lannister.png'),
    Person('Khal Drogo', 30, 8, 'Full-stack Developer', 'Antalya', 'khal_drogo.png'),
]
