from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=130)
    picture = models.ImageField(upload_to='pictures')

    class Meta:
        db_table = "profile"
