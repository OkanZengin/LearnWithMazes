from django.db import models


class Question(models.Model):
    maze_id = models.CharField(max_length=100)
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    question_position = models.CharField(max_length=10)

    def __str__(self):
        return self.question
