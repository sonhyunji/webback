from django.contrib import admin
from polls.models import Question, Choice, Contents, Content

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Contents)
admin.site.register(Content)