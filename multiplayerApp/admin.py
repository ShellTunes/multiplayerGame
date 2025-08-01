from django.contrib import admin
from .models import (
    GameCategory, GameTypes, ThemeCategory, Bets,
    Game, TruthNDare, NaughtyCards, BetCategory, Question
)


class GameCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
admin.site.register(GameCategory, GameCategoryAdmin)


class GameTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
admin.site.register(GameTypes, GameTypesAdmin)


class ThemeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme')
    search_fields = ('theme',)
admin.site.register(ThemeCategory, ThemeCategoryAdmin)



class BetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'themeCategory', 'title', 'description')
    list_filter = ('themeCategory',)
    search_fields = ('title', 'themeCategory__theme')
admin.site.register(Bets, BetsAdmin)



class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'game_category', 'game_type')
    list_filter = ('game_category', 'game_type')
    search_fields = ('title', 'game_category__name', 'game_type__name')
admin.site.register(Game, GameAdmin)



class TruthNDareAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'theme_category')
    list_filter = ('theme_category',)
    search_fields = ('title', 'theme_category__theme')

admin.site.register(TruthNDare, TruthNDareAdmin)



class NaughtyCardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'theme_category')
    list_filter = ('theme_category',)
    search_fields = ('title', 'theme_category__theme')
admin.site.register(NaughtyCards, NaughtyCardsAdmin)


