from django.db import models
from django.contrib.auth.models import User
GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

# Create your models here.
class RiderUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    user_type = models.CharField(max_length=20, default="rider")
    user_photo = models.URLField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE,blank=True, null=True)
    birth_date = models.DateField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.user.username
    