from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), #http://localhost:8000/pybo/ URL은 index, http://localhost:8000/pybo/2와 같은 URL에는 detail 이라는 별칭을 부여한 것이다.
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), #answer_create별칭 이용(pybo:answer_create <파라미터>)로 이용가능
    path('question/create/', views.question_create, name='question_create'),
]