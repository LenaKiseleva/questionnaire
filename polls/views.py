from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from polls.models import Answer, Choice, Poll, Question
from polls.permissions import ReadOnly
from polls.serializers import (AnswerSerializer, ChoiceSerializer,
                               PollSerializer, QuestionSerializer)

now = timezone.now()


class UserAnswers(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(Answer, user_id=user_id)
        serializer = AnswerSerializer(
            user,
            context={'request': request},
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


@csrf_exempt
@api_view(['GET'])
def Login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response(
            {'error': 'Пожалуйста, укажите имя пользователя и пароль'},
            status=HTTP_400_BAD_REQUEST
        )
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Неверные учетные данные'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class PollViewSet(ModelViewSet):
    queryset = Poll.objects.filter(
        end_date__gte=now
    ).filter(start_date__lte=now)
    serializer_class = PollSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    pagination_class = PageNumberPagination


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    pagination_class = PageNumberPagination


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

