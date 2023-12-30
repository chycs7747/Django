from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    is_superuser = models.BooleanField()

    def __str__(self):
        return self.username



class Subject(models.Model):
    name = models.CharField(max_length=32, verbose_name="게시판 이름")
    date = models.DateTimeField(auto_now_add=True, verbose_name="게시판 생성일")

    def __str__(self):
        return self.name

class Board(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="게시판 이름")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(max_length=64, verbose_name="글 제목")
    content = models.TextField(verbose_name="글 내용")
    written_date = models.DateTimeField(auto_now_add=True, verbose_name="글 작성일")
    update_date = models.DateTimeField(auto_now_add=True, verbose_name="글 수정일")

    def __str__(self):
        return self.title