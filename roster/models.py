from django.db import models


class Days(models.TextChoices):
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'


class Role(models.Model):
    name = models.CharField()


class Shift(models.Model):
    day = models.CharField(choices=Days.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Employee(models.Model):
    name = models.CharField()

    role = models.ForeignKey(Role)


class Availability(models.Model):
    day = models.CharField(choices=Days.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    employee = models.ForeignKey(Employee)
