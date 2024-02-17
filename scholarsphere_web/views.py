from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import pyrebase
 
config={
    "apiKey": "AIzaSyDj0kF48kaX_HowSVkrfy_asiJ1vDT1hh8",
    "authDomain": "scholorsphere.firebaseapp.com",
    "projectId": "scholorsphere",
    "storageBucket": "scholorsphere.appspot.com",
    "messagingSenderId": "708801876860",
    "appId": "1:708801876860:web:a1ae6fe384bdd56a080af9",
    "measurementId": "G-KM0D969JHE",
    "databaseURL" : "https://scholorsphere-default-rtdb.asia-southeast1.firebasedatabase.app/"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
 
def test(request):
    day = database.child('Data').child('Day').get().val()
    id = database.child('Data').child('Id').get().val()
    projectname = database.child('Data').child('Projectname').get().val()
    return render(request,"test.html",{"day":day,"id":id,"projectname":projectname })


def home(request, username):
    name = database.child(username).child('name').get().val()
    return render(request, "home.html", {"name": name , "username": username})

def profile(request, username): 
    name = database.child(username).child('name').get().val()
    return render(request, "profile.html", {"name": name , "username": username})

def calender(request, username):
    name = database.child(username).child('name').get().val()
    return render(request, "calender.html", {"name": name , "username": username})

def deaf(request,username ):
    name = database.child(username).child('name').get().val()
    return render(request, "deaf.html" ,  {"name": name , "username": username})

def subjects(request, username):
    name = database.child(username).child('name').get().val()
    return render(request, "subjects.html", {"name": name , "username": username})



def feed(request, username):
    name = database.child(username).child('name').get().val()
    return render(request, "feed.html", {"name": name , "username": username})