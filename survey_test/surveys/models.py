from django.db import models


class Survey(models.Model):
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    start_date = models.DateField(
        verbose_name='Дата старта'
    )
    end_date = models.DateField(
        verbose_name='Дата оконочания'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    active = models.BooleanField(
        verbose_name='Активность опроса'
    )
    interviewees = models.ManyToManyField(
        verbose_name='Опрошенные',
        to='Interviewee'
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            self.start_date = Survey.objects.get(pk=self.pk).start_date
        except:
            pass
        super().save(*args, **kwargs)


class Question(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    TYPES_QUESTION = [
        ('text', 'Ответ с текстом'),
        ('one_option', 'Ответ с одним вариантом'),
        ('several_options', 'Ответ с несколькими вариантами')
    ]

    text_question = models.TextField(
        verbose_name='Текст вопроса'
    )
    type_question = models.CharField(
        verbose_name='Тип вопроса',
        max_length=20,
        choices=TYPES_QUESTION
    )
    survey = models.ForeignKey(
        verbose_name='Опрос',
        to=Survey,
        on_delete=models.CASCADE
    )
    answer_options = models.TextField(
        verbose_name='Варианты ответов (если нужны)',
        blank=True
    )

    def __str__(self):
        return self.text_question


class AnswerToQuestion(models.Model):
    question = models.ForeignKey(
        verbose_name='Вопрос',
        to=Question,
        on_delete=models.CASCADE
    )
    answer = models.TextField(
        verbose_name='Ответ'
    )
    survey = models.ForeignKey(
        verbose_name='Опрос',
        to=Survey,
        on_delete=models.CASCADE
    )
    interviewee = models.ForeignKey(
        verbose_name='Опрашиваемый',
        to='Interviewee',
        on_delete=models.CASCADE
    )


class Interviewee(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=30,
        blank=True
    )
    lastname = models.CharField(
        verbose_name='Фамилия',
        max_length=30,
        blank=True
    )
