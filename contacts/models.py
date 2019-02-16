from django.db import models

class Mail(models.Model):
    name = models.CharField(max_length=128)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(max_length=2048)

    def __str__(self):
        return self.title