from django.shortcuts import render, get_object_or_404
from .models import Subject
from .models import Board


def index(request):
    subject_list = Subject.objects.order_by('-date')
    context = {'subject_list': subject_list}
    return render(request, 'notice_board/subject_list.html', context)

def subject_detail(request, subject_id):
    subject = Subject.objects.get(subject_id)
    return render(request, 'notice_board/subject_detail.html', subject)