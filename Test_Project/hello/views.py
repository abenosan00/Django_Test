from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend , user
from .forms import logins, add_userss
# Create your views here.

def index(request):
    data = Friend.objects.all().values()
    params = {
        'title':'Hello',
        'data':data,
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
    ### FROMからのrequesr
    if(request.method == 'POST'):
        u_id = request.POST["user_ids"]
        u_ps = request.POST["user_pass"]
        ### DBからクライアントが入力したデータがあるか判定
        if(user.objects.filter( user_id__startswith=u_id, user_pass__startswith=u_ps)):
            return render(request, 'hello/account.html',params)
        else:
            params = {
                'title':'ログインデータ',
                'form':logins(),
                'goto':'index',
                'add':'add',
                'mesg':'IDかパスワードが違います。'
            }
    return render(request, 'hello/login.html',params)

### ユーザー登録
def add_user(request):
    params = {
        'title':"新規ユーザ登録",
        'form':add_userss(),
        'goto':'index',
    }
    return render(request, 'hello/add_user.html',params)
    if(request.method == "POST"):
        u_id = request.POST["user_ids"]
        u_pass = request.POST["user_pass"]
        email = request.POST["email"]
        add_users = user(user_id=u_id, user_pass=u_pass, email=email)
        add_users.save()
    return render(request, 'hello/login.html',params)
