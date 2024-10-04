from django.contrib.auth.models import User
from rest_framework import serializers
from . import models
# default:
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'password', 'password2']
        extra_kwargs = {"password":{"write_only": True},"password2":{"write_only": True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        return user

class RiderSerializer(serializers.Serializer):
    class Meta:
        model = models.RiderUserModel
        fields = '__all__'

class RiderRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.RiderUserModel
        fields = ['user', 'user_type', 'user_photo', 'gender', 'birth_date']
        extra_kwargs = {
            'user_photo': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        
        rider = models.RiderUserModel.objects.create(
            user=user,
            birth_date=validated_data.get('birth_date', None),
            gender=validated_data.get('gender', None),
            user_photo=validated_data.get('user_photo', None),
            user_type='rider',
        )
        return rider
