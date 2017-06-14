from django.db import models
import datetime


class UserData(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.EmailField(unique=True, max_length=25)
    password = models.CharField(null=True, max_length=20)
    designation = models.CharField(max_length=25, null=True)


class Room(models.Model):

    name = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)


class Booking(models.Model):

    user_id = models.ForeignKey(UserData, blank=False)
    room_id = models.ForeignKey(Room, blank=False)
    booking_date = models.DateTimeField(default=datetime.date.today, blank=False)
    start_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)
