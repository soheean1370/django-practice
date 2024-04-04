from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100) #제목
    description = models.TextField(blank = True) # 설명
    created = models.DateTimeField(auto_now_add =True) #생성일자
    complete = models.BooleanField(default=False) #완료 여부
    important = models.BooleanField(default=False) #중요 여부

    def __str__(self):
        return self.title