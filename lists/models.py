from django.db import models

# Create your models here.
class Tasks(models.Model):
	user = models.CharField(default = "",max_length=20)
	title = models.CharField(max_length=100)
	completed =  models.BooleanField(default=False)
	add_date = models.DateField(auto_now_add=True)

