from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Question, Choice

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        #fields = ['id', 'question', 'choice_text', 'vote']
        fields = ['id', 'choice_text', 'vote']