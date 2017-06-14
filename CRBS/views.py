from django.shortcuts import render
from CRBS.models import UserData, Room, Booking
from django.http import Http404
from CRBS.forms import UserForm, UserLoginForm
from django.http import HttpResponse
import json
import crypt


def index(request):
    return render(request, "index.html")


def sign_up(request):
    return render(request, "signup.html")


def log_in(request):
    return render(request, "login.html")


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = UserData.objects.get(username = email)
            except UserData.DoesNotExist:
                print "Does not exist"
                return HttpResponse("User Does Not Exist")

            if user:
                if crypt.crypt(password,"dfkjfkgkfg") == getattr(user,'password',''):
                    print "login successfull"
                    return render(request, "success.html")
                else:
                    print "wrong password"
                    return HttpResponse("Wrong Password")
                    #Entered wrong password
            else:
                return HttpResponse("User Not Found")
                #user not found
        else:
            print form.errors
            form = UserLoginForm()
            return HttpResponse("Something Went wrong while Submitting data")
    else:
        return Http404


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            designation = form.cleaned_data['designation']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            new_user = UserData(first_name=first_name, last_name=last_name, designation=designation,
                                username=email, password=crypt.crypt(password,"dfkjfkgkfg"))
            new_user.save()
            #Once the data is updated show the user that his account has been created
            print "New User has been Created"
            return render(request, "login.html")
        else:
            #password_hash = crypt.crypt("skhdkfhsd");
            print form.errors
            form = UserForm()
            return render(request, "index.html")
            #Hasnt entered all the required details
    else:
        return Http404


def get_rooms(request):
    if request.method == 'POST':
        rooms = Room.objects.all()
        #show the page where all rooms are shown to the user once he is logged in


def show_bookings(request, room_id):
    bookings = Booking.objects.all(id=room_id)
    if request.method == 'POST':
        pass
        #Send this data to the template and populate the fields
    else:
        return Http404


def book_a_room(request, user_id, room_id):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        if json_data['user_id'] and json_data['room_id'] and json_data['booking_date'] and json_data['start_time'] \
                and json_data['end_time']:
            new_booking = Booking(user_id=json_data['user_id'], room_id=json_data['room_id'],
                                  booking_date=json_data['booking_date'], start_time=json_data['start_time'],
                                  end_time=json_data['end_time'])
            new_booking.save()
            #booking has been updated


