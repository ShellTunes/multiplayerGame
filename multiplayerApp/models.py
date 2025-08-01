from django.db import models

class GameCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GameTypes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class ThemeCategory(models.Model):
    theme = models.CharField(max_length=100)

    def __str__(self):
        return self.theme
    

class Bets(models.Model):
    themeCategory = models.ForeignKey(ThemeCategory, on_delete=models.CASCADE, related_name='theme_categories', null= True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null= True)

    def __str__(self):
        return self.title

class Game(models.Model):
    game_category = models.ForeignKey(GameCategory, on_delete=models.CASCADE, related_name='game_category', null= True)
    game_type = models.ForeignKey(GameTypes, on_delete=models.CASCADE, related_name='game_types')
    title = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.title}"


class TruthNDare(models.Model):
    theme_category = models.ForeignKey(ThemeCategory, on_delete=models.CASCADE, related_name='theme_category_dare', null= True)
    title = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.title}"
    

class NaughtyCards(models.Model):
    theme_category = models.ForeignKey(ThemeCategory, on_delete=models.CASCADE, related_name='theme_category_cards', null= True)
    title = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.title}"


class BetCategory(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='bet_categories', null= True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.game.title}"


class Question(models.Model):
    bet_category = models.ForeignKey(BetCategory, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    def __str__(self):
        return self.question_text
