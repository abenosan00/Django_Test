from django import forms
from models import user, tweet

class HelloForm(forms.Form):
    id = forms.IntegerField(label="ID")

class logins(forms.Form):
    user_ids = forms.CharField(label="ユーザーID:")
    user_pass = forms.CharField(label="パスワード:")

class add_userss(forms.Form):
    user_ids = forms.CharField(label="ユーザーID:",min_length=6)
    user_pass = forms.CharField(label="パスワード:",min_length=6)
    email = forms.EmailField(label="メールアドレス:")

class tweetForm(forms.ModelForm):
    class Meta:
        model = tweet
        users = ['title','content','user']
