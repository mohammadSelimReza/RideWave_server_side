from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)
def validate_nid(value):
    if len(str(value)) != 8:  # Example check for a 10-digit NID
        raise ValidationError('NID must be 8 digits long.')
def validate_phone_number(value):
    if len(str(value)) != 10:
        raise ValidationError('Phone number must be 10.')
def validate_driving_license_no(value):
    if len(str(value)) != 8 or not str(value).isdigit():
        raise ValidationError('License number must be exactly 8 digits.')
# Create your models here.
class DriverUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    user_type = models.CharField(max_length=20, default="driver")
    user_photo = models.URLField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE,blank=True, null=True)
    birth_date = models.DateField(blank=True,null=True)
    nid = models.IntegerField(validators=[validate_nid])
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])
    driving_license_no = models.CharField(max_length=15, validators=[validate_driving_license_no])
    user_photo = models.URLField(max_length=255, blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    has_car = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.user.username