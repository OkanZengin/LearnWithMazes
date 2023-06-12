from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    user_id = models.AutoField(primary_key=True)
    mazes_i_played_rated = models.JSONField(default=list)

    def __str__(self):
        return self.username
