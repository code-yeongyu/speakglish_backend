from rest_framework import serializers
from api.models import Article

class ArticleSerializer(serializers.ModelSerializer) :
    writer = serializers.ReadOnlyField(source='writer.username')
    class Meta :
        model = Article
        fields = ('id', 'content', 'writer', 'doneAt', 'timer', 'timerLeft')