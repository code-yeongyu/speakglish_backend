from rest_framework import serializers
from Server.models import Article

class ArticleSerializer(serializers.ModelSerializer) :
    writer = serializers.ReadOnlyField(source='writer.username')
    class Meta :
        model = Article
        fields = ('id', 'content', 'writer', 'doneAt', 'timer', 'timerLeft')