from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class UserPracticeHistory(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"User  {self.user_id} - {self.question.text}"
