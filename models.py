from django.db import  models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


""""class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    phone=models.TextField()
    address=models.TextField()

@receiver(post_save,sender=User)
def create_user_profie(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profie(sender,instance,**kwargs):
    instance.profile.save()"""