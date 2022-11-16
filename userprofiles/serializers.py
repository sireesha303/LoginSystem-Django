from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """user Register Serializer"""
    password2 = serializers.CharField(write_only=True, max_length=100,)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'password2', 'email']
        read_only = ('id', )
        extra_kwargs = {'password': {'write_only':True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
        {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PasswordResetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)
    password2 = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def update(self, instance, validated_data):
        user = instance
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
