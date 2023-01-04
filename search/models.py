from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(max_length=255,primary_key=True)
    movie = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    actor = models.CharField(max_length=255)
    year = models.DateField()
    rate = models.IntegerField()
    first_introduction = models.CharField(max_length=255)

    def id(self):
        return self.movie_id

    def movie_name(self):
        return self.movie

    def movie_other_name(self):
        return self.other_name

    def director_name(self):
        return self.director

    def actor_name(self):
        return self.actor

    def date(self):
        return self.year

    def number_of_rate(self):
        return self.rate

    def the_first_introduction(self):
        return self.first_introduction
