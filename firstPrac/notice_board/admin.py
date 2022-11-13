from django.contrib import admin
from .models import User
from .models import Subject
from .models import Board
# Register your models here.
class QuestionUser(admin.ModelAdmin):
    search_fields = ['subject']
    
class QuestionSubject(admin.ModelAdmin):
    search_fields = ['subject']

class QuestionBoard(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(User, QuestionUser)
admin.site.register(Subject,QuestionSubject )
admin.site.register(Board, QuestionBoard)
