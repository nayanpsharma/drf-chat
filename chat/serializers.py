from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import Message


#user serializer
class UserSerializer(serializers.ModelSerializer):
    #for serializing user_
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']


#message serializers
class MessageSerializer(serializers.ModelSerializer):
    #for serializing message
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']