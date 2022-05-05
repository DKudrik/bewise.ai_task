from django.db import models


class Question(models.Model):
    question_id = models.IntegerField(db_index=True)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=100)
    question_created = models.DateTimeField()
