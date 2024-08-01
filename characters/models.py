from django.db import models


class Character(models.Model):
    class StatusChoices(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        UNKNOWN = "Unknown"

    class GenderChoices(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        GENDERLESS = "Genderless"
        UNKNOWN = "Unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(choices=StatusChoices.choices, default=StatusChoices.UNKNOWN, max_length=50)
    species = models.CharField(max_length=255)
    gender = models.CharField(choices=GenderChoices.choices, default=GenderChoices.UNKNOWN, max_length=50)
    image = models.URLField(unique=True, max_length=255)

    def __str__(self):
        return self.name
