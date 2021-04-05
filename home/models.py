from django.db import models
from audiofield.fields import AudioField

class Crackels_mod(models.Model):
    loc= (
        ('location1', 'Location1'),
        ('location2', 'Location2'),
        ('location3', 'Location3'),
        ('location4', 'Location4'),
        ('location5', 'Location5'),
        ('location6', 'Location6'),)

    sno = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    firstname1 = models.CharField(max_length=255)
    lastname1 = models.CharField(max_length=255)
    # inputGroupFile02 = models.FileField(upload_to='home/sounds_file', default="")
    AudioFile= models.FileField(upload_to='home/sounds_file', default="")
    PFT_Location= models.CharField(max_length = 20, choices = loc, default='location1')
    PFT_image = models.FileField(upload_to='images/', blank=True)
    Comment_box  = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
         return self.firstname1
