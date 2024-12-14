from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'role', 'cart']
        extra_kwargs = {
            'role': {'required': False},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        password = validated_data.pop('password', None)
        user = super().create(validated_data)

        if password:
            user.set_password(password)
            user.save()
        for group in groups_data:
            group_instance, created = Group.objects.get_or_create(name=group.name)
            user.groups.add(group_instance)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
