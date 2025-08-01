from django.urls import path

from .views import (
    # BetsByCategoryThemeView,
    GamesByCategoryView,
    ThemeCategoryListView,
    AllBetsListView,
    BetsByCategoryView,
)

urlpatterns = [
    path('theme-categories/', ThemeCategoryListView.as_view(), name='theme-category-list'),
    path('bets/', AllBetsListView.as_view(), name='all-bets'),
    path('theme-categories/<int:category_id>/bets/', BetsByCategoryView.as_view(), name='bets-by-category'),
    # path('theme-categories/<str:category_theme>/bets/', BetsByCategoryThemeView.as_view()),
    path('game-categories/<int:category_id>/games/', GamesByCategoryView.as_view(), name='games-by-category'),
]
