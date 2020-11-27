from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Content(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content_text = models.CharField(max_length=500)

    def __str__(self):
        return self.content_text

class Contents(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    contents_text = models.CharField(max_length=50000)

    def __str__(self):
        return self.contents_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


