
from rest_framework import serializers
from .models import Game, ThemeCategory, Bets

class BetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bets
        fields = ['id', 'title', 'description', 'themeCategory']

class ThemeCategorySerializer(serializers.ModelSerializer):
    bets = BetsSerializer(many=True, read_only=True)  # reverse relation

    class Meta:
        model = ThemeCategory
        fields = ['id', 'theme', 'bets']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'game_category', 'game_type']