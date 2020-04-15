from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail,name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('questions/', views.QuestionList.as_view(), name='questions'),
    path('questions/<int:question_id>/', views.QuestionDetail.as_view(), name='question'),
    path('choices/', views.ChoiceList.as_view(), name='choices'),
    path('choices/<int:choice_id>/', views.ChoiceDetail.as_view(), name='choice'),
]