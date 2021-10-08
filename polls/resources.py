from import_export import resources

from .models import Answer, Choice, Poll, Question


class PollResource(resources.ModelResource):
    class Meta:
        model = Poll
        fields = ('id', 'name', 'pub_date', 'start_date',
                  'end_date', 'description',)


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question
        fields = ('id', 'poll', 'question_text', 'question_type',)


class ChoiceResource(resources.ModelResource):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text',)


class AnswerResource(resources.ModelResource):
    class Meta:
        model = Answer
        fields = ('id', 'user_id', 'poll', 'question', 'choice', 'choice_text')
