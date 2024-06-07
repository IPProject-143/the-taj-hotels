from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class hotel(models.Model):
    location = models.CharField(max_length = 14)

    def save(self, *args, **kwargs):
        if not self.location and hotel.objects.exists():
        # if you'll not check for self.pk 
        # then error will also be raised in the update of exists model
            raise ValidationError('There is can be only one NormalRoom instance')
        return super(hotel, self).save(*args, **kwargs)

    def __str__(self):
        return f"Hotel at {self.location}"


class CouplesRoom(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_adults = models.IntegerField(default= 2, validators = [MinValueValidator(2), MaxValueValidator(4)])
    no_of_kids = models.IntegerField(default= 0, validators = [MinValueValidator(0), MaxValueValidator(2)])
    booked = models.BooleanField(default = False)
    vip_services = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_location = models.ForeignKey(hotel, on_delete = models.CASCADE)

    def __str__(self):
        return f"Couples room for {self.user.username} for {self.no_of_adults} adult(s) and {self.no_of_kids} kid(s)"

class NormalRoom(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_adults = models.IntegerField(default= 1, validators = [MinValueValidator(1), MaxValueValidator(8)])
    no_of_kids = models.IntegerField(default= 0, validators = [MinValueValidator(0), MaxValueValidator(4)])
    booked = models.BooleanField(default = False)
    vip_services = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_location = models.ForeignKey(hotel, on_delete = models.CASCADE)

    def __str__(self):
        return f"Normal room for {self.user.username} for {self.no_of_adults} adult(s) and {self.no_of_kids} kid(s)"

class VIPRooms(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_adults = models.IntegerField(default= 1, validators = [MinValueValidator(1), MaxValueValidator(8)])
    no_of_kids = models.IntegerField(default= 0, validators = [MinValueValidator(0), MaxValueValidator(4)])
    booked = models.BooleanField(default = False)
    vip_services = models.BooleanField(default = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_location = models.ForeignKey(hotel, on_delete = models.CASCADE)

    def __str__(self):
        return f"Normal room for {self.user.username} for {self.no_of_adults} adult(s) and {self.no_of_kids} kid(s)"
