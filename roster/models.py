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
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '{}'.format(self.name)


class Shift(models.Model):
    day = models.CharField(max_length=10, choices=Days.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return '{}: {} - {}'.format(self.name, self.start_time, self.end_time)


class Employee(models.Model):
    name = models.CharField(max_length=50)

    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL, related_name='employee')

    def __str__(self):
        return '{} [{}]'.format(self.name, self.role)


class Availability(models.Model):
    day = models.CharField(max_length=10, choices=Days.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {} - {}'.format(self.name, self.start_time, self.end_time)
