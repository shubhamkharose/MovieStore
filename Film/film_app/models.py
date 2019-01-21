from django.db import models


class Movie(models.Model):
    FilmId = models.CharField(primary_key=True,max_length=255,auto_created=True)
    FilmName = models.CharField(max_length=255, null=False)
    Genre = models.CharField(max_length=255)
    Studio = models.CharField(max_length=255)
    Director = models.CharField(max_length=255)
    Producer = models.CharField(max_length=255)
    LeadActor = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.FilmId, self.FilmName)
