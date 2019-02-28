from rest_framework import serializers
from owners.models import Owner, Season


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('year', 'wins', 'losses', 'team_name', 'made_playoffs', 'playoff_wins', 'playoff_losses',
                  'made_superbowl', 'superbowl_wins', 'superbowl_losses', 'acquisitions', 'trades')


class OwnerSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True,read_only=True)

    class Meta:
        model = Owner
        fields = ('id', 'name', 'current_participant', 'email', 'phone_number', 'instagram_name', 'twitter_name', 'seasons')
