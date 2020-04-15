from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import QuestionSerializer, ChoiceSerializer
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print(type(latest_question_list))
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return HttpResponse("You're looking at question: %s." % question)

def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choices = question.choices.all()
    output = ', '.join([str(c) for c in choices])
    return HttpResponse(output)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer

    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer

    def get_object(self):
        obj = get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))
        return obj

