from django.db import models

from .validators import date_validator


class Poll(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название опроса',
        blank=False,
        null=False,
        unique=True,
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания опроса',
        auto_now_add=True,
    )
    start_date = models.DateTimeField(
        validators=[date_validator],
        verbose_name='Дата начала опроса',
        blank=False,
        null=False,
    )
    end_date = models.DateTimeField(
        validators=[date_validator],
        verbose_name='Дата окончания опроса',
        blank=False,
        null=False,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=False,
        null=False,
        help_text='Укажите тематику и цель опроса.',
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(
        Poll,
        verbose_name='Опрос',
        related_name='questions',
        on_delete=models.CASCADE
    )
    question_text = models.CharField(
        verbose_name='Текст вопроса',
        max_length=200,
        null=True
    )
    question_type = models.CharField(
        verbose_name='Тип вопроса',
        max_length=200
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        verbose_name='Выбор',
        related_name='choices',
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(
        verbose_name='Текст выбора',
        max_length=200
    )

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выборы'

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user_id = models.IntegerField(
        verbose_name='Пользователь',
        blank=False,
        null=False,
        help_text='Укажите уникальный ID.',
    )
    poll = models.ForeignKey(
        Poll,
        verbose_name='Опрос',
        related_name='poll',
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        verbose_name='Вопрос',
        related_name='question',
        on_delete=models.CASCADE
    )
    choice = models.ForeignKey(
        Choice,
        verbose_name='Выбор',
        related_name='choice',
        on_delete=models.CASCADE,
        null=True
    )
    choice_text = models.CharField(
        max_length=200,
        null=True
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.choice_text
