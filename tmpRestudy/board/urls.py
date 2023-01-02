from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.main_index, name='main_index'),
    path('board/<str:board_name>/', views.board_index, name='board_index'),
    path('create/', views.board_create, name='board_create'),
    path('create/submit/', views.board_create_submit, name='board_create_submit'),
    path('board/delete/<str:board_name>', views.board_delete, name='board_delete'),

    path('post/<str:post_name>/', views.post_index, name='post_index'),
    path('modify/<str:post_name>', views.post_modify, name='post_modify'),
    path('modify/submit/<str:post_name>', views.post_modify_submit, name='post_modify_submit'),
    path('post/delete/<str:post_name>', views.post_delete, name='post_delete'),

    path('comment/submit/<str:post_name>', views.post_comment_submit, name='post_comment_submit')
]