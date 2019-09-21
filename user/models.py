from django.db import models

# Create your models here.
 
class ProfilePicture(models.Model): 
	name = models.CharField(max_length=50) 
	profile_picture = models.ImageField(upload_to='images/') 
