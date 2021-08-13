from rest_framework.serializers import ModelSerializer

from surveys.models import Survey, Question, AnswerToQuestion


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ['name']


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['text_question', 'answer_options']


class UserSurveysSerializer(ModelSerializer):
    class Meta:
        model = AnswerToQuestion
        fields = ['question', 'answer']
