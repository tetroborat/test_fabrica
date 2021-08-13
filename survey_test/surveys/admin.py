from django.contrib import admin

from surveys.models import Survey, Question

admin.site.register(Survey)
admin.site.register(Question)
