from django.db import models

# Create your models here.
class RoomMember(models.Model):
    name = models.CharField(max_length=100)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.username

        
