from django.db import models

# Create your models here.

class Paragraph(models.Model):
    text = models.TextField()
