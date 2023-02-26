from django.db import models

TYPE_CHOICES = []

class TransactionRecord(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    progress = models.IntegerField()
    description = models.TextField()
