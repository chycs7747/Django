from django.urls import path
from notice_board import views

app_name = 'notice_board'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:subject_id>/', views.subject_detail, name="subjectId")
]