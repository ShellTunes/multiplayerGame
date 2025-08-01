from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game, ThemeCategory, Bets
from .serializers import GameSerializer, ThemeCategorySerializer, BetsSerializer
from django.shortcuts import get_object_or_404

# Get all categories
class ThemeCategoryListView(APIView):
    def get(self, request):
        categories = ThemeCategory.objects.all()
        serializer = ThemeCategorySerializer(categories, many=True)
        return Response(serializer.data)

# Get all bets
class AllBetsListView(APIView):
    def get(self, request):
        bets = Bets.objects.all()
        serializer = BetsSerializer(bets, many=True)
        return Response(serializer.data)

# Get bets by category ID
class BetsByCategoryView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(ThemeCategory, pk=category_id)
        bets = category.theme_categories.all()  # use the related_name
        serializer = BetsSerializer(bets, many=True)
        return Response(serializer.data)


# class BetsByCategoryThemeView(APIView):
#     def get(self, request, category_theme):
#         category = get_object_or_404(ThemeCategory, theme__iexact=category_theme)
#         bets = Bets.objects.filter(themeCategory=category)
#         serializer = BetsSerializer(bets, many=True)
#         return Response(serializer.data)

class GamesByCategoryView(APIView):
    def get(self, request, category_id):
        games = Game.objects.filter(game_category_id=category_id)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)