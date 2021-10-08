from django.urls import include, path
from rest_framework.routers import DefaultRouter

from polls.views import (AnswerViewSet, ChoiceViewSet, Login, PollViewSet,
                         QuestionViewSet, UserAnswers)

router_v1 = DefaultRouter()

router_v1.register('polls', PollViewSet, basename='Poll')
router_v1.register('questions', QuestionViewSet, basename='Question')
router_v1.register('choices', ChoiceViewSet, basename='Choice')
router_v1.register('answers', AnswerViewSet, basename='Answer')


urlpatterns = [
    path('v1/login/', Login, name='login'),
    path('v1/answers/view/<int:user_id>/', UserAnswers.as_view()),
    path('v1/', include(router_v1.urls)),
]
