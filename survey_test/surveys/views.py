
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from surveys.models import Survey, Question, Interviewee, AnswerToQuestion
from surveys.serialazers import SurveySerializer, QuestionSerializer, UserSurveysSerializer


class SurveyViewSet(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['name', 'active', 'interviewees']
    search_fields = ['name', 'description']
    ordering_filters = ['start_date', 'end_date']


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['survey']


class PassedSurveysViewSet(ModelViewSet):
    queryset = AnswerToQuestion.objects.all()
    serializer_class = UserSurveysSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['interviewee', 'survey']
