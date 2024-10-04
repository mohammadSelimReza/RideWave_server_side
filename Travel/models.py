from django.db import models
from Rider.models import RiderUserModel
from Driver.models import DriverUserModel
from datetime import timedelta,datetime
from django.utils import timezone
# Vehicle types for choices
VEHICLE_TYPE = (
    ('bike', 'Bike'),
    ('cng', 'CNG'),
    ('car', 'Car'),
)
PAYMENT_METHOD = (
    ('cash','Cash'),
    ('net_banking','Net Banking'),
    ('card','Card'),
)

# Travel Request Model
class TravelRequestModel(models.Model):
    rider = models.ForeignKey(RiderUserModel, on_delete=models.CASCADE)
    request_no = models.AutoField(primary_key=True, unique=True)  # Auto-incrementing primary key
    start_location = models.CharField(max_length=400)
    destination_location = models.CharField(max_length=400)
    payment_method = models.CharField(max_length=100,choices=PAYMENT_METHOD,default='cash')
    travel_vehicle = models.CharField(max_length=100, choices=VEHICLE_TYPE)
    path_distance = models.FloatField(default='0.00')
    travel_fare = models.FloatField(default='0.00')
    driver_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Travel Request {self.id} for Rider {self.rider.user.username}"


# Travel Details Model
class TravelDetailsModel(models.Model):
    rider = models.ForeignKey(RiderUserModel, on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverUserModel, on_delete=models.CASCADE)
    request_no = models.PositiveIntegerField(default=1,primary_key=True)  # Reference to TravelRequestModel
    start_location = models.CharField(max_length=400)
    destination_location = models.CharField(max_length=400)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(null=True, blank=True)
    distance = models.FloatField()
    price = models.FloatField()
    payment_method = models.CharField(max_length=100,choices=PAYMENT_METHOD)
    payment_status = models.BooleanField(default=False)
    travel_running = models.BooleanField(default=False)
    def end_ride(self):
        """Ends the ride and moves the details to travel history."""
        self.end_time = timezone.now().time()
        self.save()  # Save the updated details

        # Create a new entry in TravelHistoryModel
        TravelHistoryModel.objects.create(
            rider=self.rider,
            driver=self.driver,
            travel_details=self,
            completed_date_time=timezone.now()
        )
    @property
    def travelled_for(self):
        """Calculate the duration of travel in timedelta format."""
        if self.end_date and self.end_time:
            # Combine date and time for both start and end
            start_datetime = datetime.combine(self.start_date, self.start_time)
            end_datetime = datetime.combine(self.end_date, self.end_time)
            return end_datetime - start_datetime
        return timedelta(0)

    def __str__(self):
        return f"{self.rider.user.username} - {self.start_location} to {self.destination_location}"


# Travel History Model
class TravelHistoryModel(models.Model):
    rider = models.ForeignKey(RiderUserModel, on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverUserModel, on_delete=models.CASCADE)
    travel_details = models.ForeignKey(TravelDetailsModel, on_delete=models.CASCADE)
    completed_date_time = models.DateTimeField()
    def __str__(self):
        return f"{self.rider.user.username} - {self.driver.user.username}"
