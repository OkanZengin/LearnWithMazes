from django.db import models


class UserMaze(models.Model):
    user = models.CharField(max_length=40)
    maze_id = models.CharField(max_length=24, primary_key=True)
    maze_level = models.CharField(max_length=20)
    maze_layout = models.JSONField()
    maze_wall_positioning = models.JSONField()
    rating = models.FloatField(default=0)
    rate_count = models.IntegerField(default=0)
