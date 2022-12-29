from django.urls import path

from . import views #views.py의 메소드를 사용하기 위해 import

urlpatterns = [
    path('', views.index), #views.index 메소드 실행
]