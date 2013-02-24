from django.db import models

class Blog(models.Model):
    id = models.IntegerField(default=1,db_index=True,primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

