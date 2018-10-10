from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('login',views.login, name='login'),
    path('add_user',views.add_user,name='add_user'),
    path('message/'views.message,name='message'),
    path('message/<int:page>',views.message,name='message'),
]
