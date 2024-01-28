from django.db import models

# Create your models here.

##  Booking Model 
class Booking(models.Model):
    full_name = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    service = models.CharField(max_length = 250)
    location = models.CharField(max_length = 250)
    date = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)
    message = models.CharField(max_length = 500)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"

## Testimonial Model
class Testimonial(models.Model):
    name = models.CharField(max_length = 20)
    comment = models.CharField(max_length = 500)
    service = models.CharField(max_length = 250)
    date = models.CharField(max_length = 20)

    def __str__(self):
        return f"{self.name}'s Testimonail."
    
## Team Model
class Team(models.Model):
    name = models.CharField(max_length = 20)
    position = models.CharField(max_length = 20)
    # bio = models.CharField(max_length = 500)
    # facebookLInk = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='static/img')

    def __str__(self):
        return f"{self.name}'s Profile."
    
## Team on site pictures Model
class TeamOnSite(models.Model):
    image = models.ImageField(upload_to='static/img')

    def __str__(self):
        return f"{self.image.url}"


    
