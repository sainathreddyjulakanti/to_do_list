from django.db import models

class Lists(models.Model):
    S_No = models.IntegerField(unique=True)  # Enforce uniqueness of S_No
    Items = models.CharField(max_length=255)

    def __str__(self):
        return self.Items





