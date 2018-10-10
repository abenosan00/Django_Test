from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import user
from .forms import logins, add_userss

# Create your views here.

def index(request ,num=1):
    data = user.objects.all()
    page = Paginator(data,3)
    params = {
        'title':'Hello',
        'data':page.get_page(num),
        'add':'add_user',
        'goto':'login',
    }
    return render(request, 'hello/index.html',params)

### ログイン処理
def login(request):
    ### 初期テキスト
    params = {
        'title':'ログインデータ',
        'form':logins(),
        'goto':'index',
        'add':'add_user',
        'mesg':'',
    }
    ### ログイン処理
    if(request.method == 'POST'):
        u_id = request.POST["user_ids"]
        u_ps = request.POST["user_pass"]
        if 'user_id' in request.session:
            sid = "セッションあるよ"
        else:
            request.session['user_id'] = u_id
            sid = request.session['user_id']
        ### DBからクライアントが入力したデータがあるか判定
        if(user.objects.filter( user_id__startswith=u_id, user_pass__startswith=u_ps)):
            params = {'data':u_id}
            return render(request, 'hello/account.html',params)
        else:
            params = {
                'title':'ログインデータ',
                'add':'add',
                'form':logins(),
                'goto':'index',
                'session':sid,
                'mesg':'IDかパスワードが違います。'
            }
    return render(request, 'hello/login.html',params)

### ユーザー登録
def add_user(request):
    params = {
        'title':"新規ユーザ登録",
        'form':add_userss(),
        'msg':"",
        'goto':'index',
    }
    if(request.method == "POST"):
        u_id = request.POST["user_ids"]
        u_pass = request.POST["user_pass"]
        email = request.POST["email"]
        if(user.objects.filter( user_id__startswith=u_id)):
            params['msg'] = "※すでに入力されたIDが存在しています。"
        else:
            add_users = user(user_id=u_id, user_pass=u_pass, email=email)
            add_users.save()
            return redirect('/hello')

    return render(request, 'hello/add_user.html',params)


