
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    
    picture = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name="my_friends")

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_profile(sender ,instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)#sent profile class as a argument.
                                    
    def __str__(self):
        return self.profile.name

class Messages(models.Model): #not working
    sender = models.ForeignKey(Profile, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.timestamp}"

