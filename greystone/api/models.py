from django.db import models

#Model to store all messages

class Message(models.Model):
	message_text = models.CharField(max_length=300)

	def __str__(self):
		return self.message