from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100 , default="")
    city = models.CharField(max_length= 20, default="")
    website = models.URLField(default="")
    phone = models.DecimalField(max_digits=10, decimal_places=4, default="")

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

            post_save.connect(sender.create_profile, sender=User)

    def __str__(self):
        return '%s - %s - %s' % (self,  UserProfile)