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
    print("request:",request)
    print(f'request formating: {request}')
    print('request formating: {:}' .format(request))
    print("request.method:",request.method)
    print("request.session:", request.session)
    if request.method == "GET":
        post=Post.objects.get(name=post_name)
        context = {
            'post': post,
        }
        print("request:",request)
        return render(request, 'board/post_screen.html', context)

def board_create(request):
    return render(request, 'board/board_create.html')

def board_create_submit(request):
    if request.method == 'POST':
        board=Board(name=request.POST.get(['create_content'], None)) #request.POST['create_content'] == request.POST.get(['create_content'], None)
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
        print('Post??? ????????? ??????????????? ??????')
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


    
#????????? url???  ?????????

#post_screen.html??? ?????? ????????? ?????? -> 'post/modify/<int:post_id>'??? ???????????? views.post_modify?????? -> Render??? ??????????????? ?????? ??? ???????????? ????????? ?????? (??? ??? render??? ????????? post????????? id?????? ?????? ???????????? post_submit??? ???????????? ??? ??????????????? ?????????)
#post_modiy ???????????? ????????? html?????? id?????? ???????????? ??? id?????? ????????? ??????????????? ?????? ???, mainscreen?????? ?????????.