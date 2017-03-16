from django.db import models

class Keyboard(models.Model):
    type = models.CharField(max_length=4, blank=False, default='text')

    @classmethod
    def create(cls):
        keyboard = cls()
        return keyboard

class Message(models.Model):
    text = models.CharField(max_length=1000, blank=True, null=True)

    @classmethod
    def create(cls, text):
        Message = cls(text=text)
        return Message

class MessageResponse(models.Model):
    message = models.OneToOneField(Message, on_delete=models.CASCADE)

    @classmethod
    def create(cls, message):
        MessageResponse = cls(message=message)
        return MessageResponse
