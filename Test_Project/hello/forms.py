from django import forms

class HelloForm(forms.Form):
    id = forms.IntegerField(label="ID")

class logins(forms.Form):
    user_ids = forms.CharField(label="ユーザーID:")
    user_pass = forms.CharField(label="パスワード:")

class add_userss(forms.Form):
    user_ids = forms.CharField(label="ユーザーID:")
    user_pass = forms.CharField(label="パスワード:")
    email = forms.EmailField(label="メールアドレス:")
