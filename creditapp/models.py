from django.db import models

from datetime import datetime    
# Create your models here.

class User(models.Model):
	username 	= models.CharField(max_length=50)
	email		= models.EmailField()
	credits 	= models.IntegerField()

	def __str__(self):
		return self.username

class TransferHistory(models.Model):
	sender	= models.ForeignKey(User,related_name='send_credits',on_delete=models.CASCADE)
	reciever= models.ForeignKey(User,on_delete=models.CASCADE)
	amount	= models.PositiveIntegerField()
	date    = models.DateTimeField(default=datetime.now(), blank=True)

	def __str__(self):
		return self.sender.username


	