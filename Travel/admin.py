from django.contrib import admin
from .models import TravelDetailsModel,TravelRequestModel,TravelHistoryModel
# Register your models here.
admin.site.register(TravelDetailsModel)
admin.site.register(TravelRequestModel)
admin.site.register(TravelHistoryModel)