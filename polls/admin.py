from django.contrib import admin
from import_export.admin import ImportMixin

from polls.models import Answer, Choice, Poll, Question

from .resources import (AnswerResource, ChoiceResource, PollResource,
                        QuestionResource)


class PollAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = PollResource
    list_display = ('id', 'name', 'pub_date', 'start_date',
                    'end_date', 'description',)


class QuestionAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = QuestionResource
    list_display = ('id', 'poll', 'question_text', 'question_type',)


class ChoiceAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = ChoiceResource
    list_display = ('id', 'question', 'choice_text',)


class AnswerAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = AnswerResource
    list_display = ('id', 'user_id', 'poll',
                    'question', 'choice', 'choice_text')


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
