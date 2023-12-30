from django.contrib import admin
from .models import Question

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content'] # admin - app 에서 검색 필터 (Question 모델의 필드 subject, content로 접근 가능)


admin.site.register(Question, QuestionAdmin)