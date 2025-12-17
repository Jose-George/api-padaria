from django.db import models

class User(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=150)
	username = models.CharField(max_length=150, unique=True)
	password = models.CharField(max_length=128)

	class Meta:
		db_table = 'users'
	
	def __str__(self):
		return self.username 