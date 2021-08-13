# Generated by Django 2.2.10 on 2021-08-13 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interviewee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, max_length=30, verbose_name='Фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('start_date', models.DateField(verbose_name='Дата старта')),
                ('end_date', models.DateField(verbose_name='Дата оконочания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('active', models.BooleanField(verbose_name='Активность опроса')),
                ('interviewees', models.ManyToManyField(to='surveys.Interviewee', verbose_name='Опрошенные')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.TextField(verbose_name='Текст вопроса')),
                ('type_question', models.CharField(choices=[('text', 'Ответ с текстом'), ('one_option', 'Ответ с одним вариантом'), ('several_options', 'Ответ с несколькими вариантами')], max_length=20, verbose_name='Тип вопроса')),
                ('answer_options', models.TextField(blank=True, verbose_name='Варианты ответов (если нужны)')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='AnswerToQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('interviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Interviewee', verbose_name='Опрашиваемый')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Question', verbose_name='Вопрос')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey', verbose_name='Опрос')),
            ],
        ),
    ]