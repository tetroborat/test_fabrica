from django.urls import path
from rest_framework.routers import SimpleRouter

from surveys.views import SurveyViewSet, QuestionViewSet, PassedSurveysViewSet

router = SimpleRouter()
router.register(r'survey', SurveyViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'passed_surveys', PassedSurveysViewSet)

urlpatterns = router.urls
