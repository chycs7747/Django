from django.shortcuts import render, redirect
from .models import Board, Post, Comment

# Create your views here.
def main_index(request):
    board_list = Board.objects.all()
    post_list = Post.objects.all()
    context = {'board_list': board_list, 'post_list': post_list}
    return render(request, 'board/main_screen.html', context)

def board_index(request, board_name):
    board = Board.objects.get(name=board_name)
    context = {'board': board}
    return render(request, 'board/board_screen.html', context)

def post_index(request, post_name):
    post=Post.objects.get(name=post_name)

    context = {
        'post': post,
    }
    return render(request, 'board/post_screen.html', context)

def board_create(request):
    return render(request, 'board/board_create.html')

def board_create_submit(request):
    if request.method == 'POST':
        board=Board(name=request.POST['create_content'])
        board.save()
        return redirect('board:main_index')

def post_create(request, board_name):
    board=Board.objects.get(name=board_name)
    context = {
        'board': board,
    }
    return render(request, 'board/post_create.html', context)

def post_create_submit(request, board_name):
    board=Board.objects.get(name=board_name)
    create_name=request.POST['create_name']
    create_content=request.POST['create_content']
    post = Post(board=board, name=create_name, content=create_content)
    post.save()
    return redirect('board:board_index', board_name)

def post_modify(request, post_name):
    post=Post.objects.get(name=post_name)
    context = {
        'post': post,
    }
    return render(request, 'board/post_modify.html', context)

def post_modify_submit(request, post_name):
    if request.method == 'POST':
        post=Post.objects.get(name=post_name)
        print('Post가 어떻게 넘어오는지 확인')
        print(request.POST)
        print('\n\n\n')
        post.content = request.POST['modify_content']
        post.save()
        return redirect('board:post_index', post_name=post_name)

def board_delete(request, board_name):
    if request.method == 'POST':
        board=Board.objects.get(name=board_name)
        board.delete()
        return redirect('board:main_index')

def post_delete(request, post_name):
    if request.method == 'POST':
        post=Post.objects.get(name=post_name)
        post.delete()
        return redirect('board:main_index')

def post_comment_submit(request, post_name):
    if request.method == 'POST':
        post=Post.objects.get(name=post_name)
        user = request.POST['comment_user_name']
        content = request.POST['comment_content']
        if user!="" and content!="":
            new_comment = Comment(user_name=user, content=content, post=post)
            new_comment.save()
            return redirect('board:post_index', post_name=post_name)
        return redirect('board:post_index', post_name=post_name)


    
#게시판 url을  바궈라

#post_screen.html의 수정 버튼을 클릭 -> 'post/modify/<int:post_id>'로 접속하며 views.post_modify실행 -> Render로 수정페이지 띄운 후 수정완료 버튼을 클릭 (이 때 render로 넘겼던 post객체를 id값을 통해 기억하고 post_submit을 실행시킬 때 매개변수로 넣어줌)
#post_modiy 함수에서 실행된 html에서 id값을 넘겨받고 그 id값을 이용해 변경사항을 저장 후, mainscreen으로 넘어감.