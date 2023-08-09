from django.db import models
from item.models import Item
from django.contrib.auth.models import User

class Conversation(models.Model):
    item=models.ForeignKey(Item,related_name='conversation',on_delete=models.CASCADE)
    members=models.ManyToManyField(User,related_name='members')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated_at']

    def __str__(self):
        return f"{self.item}, {self.created_at}"

class ConversationMessage(models.Model):
    conversation=models.ForeignKey(Conversation,related_name='messages',on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='created_messages',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"