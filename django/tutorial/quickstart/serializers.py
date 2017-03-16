from rest_framework import serializers
from tutorial.quickstart.models import Keyboard, Message, MessageResponse

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = ('type',)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text',)

class MessageResponseSerializer(serializers.ModelSerializer):
    message = MessageSerializer(read_only=True)

    class Meta:
        model = MessageResponse
        fields = ('message',)
