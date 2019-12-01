from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    college = models.CharField(max_length=60)
    mobile_number = models.CharField(max_length=20)
    place = models.CharField(max_length=30)


@receiver(post_save, sender=User)
def profile_for_new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()
