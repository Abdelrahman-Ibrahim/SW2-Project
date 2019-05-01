from django.db import models

# Create your models here.
# api/models.py

class AllData(models.Model):
    title = "All Data"
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.title, self.data)