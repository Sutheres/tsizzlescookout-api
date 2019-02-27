from rest_framework import serializers
from owners.models import Owner, Season


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'name', 'email', 'phone_number', 'instagram_name', 'twitter_name')

