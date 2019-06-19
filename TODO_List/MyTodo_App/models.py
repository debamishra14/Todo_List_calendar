from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title       = models.CharField(max_length=50)
    description = models.TextField()
    created     = models.DateField(auto_now_add=True)
    status      = models.ForeignKey(Status, on_delete=models.CASCADE)
    due_date    = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    modified    = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + '|'+ self.description +'|'+ self.status +'|'+self.created+'|'+self.modified+'|'+self.due_date
