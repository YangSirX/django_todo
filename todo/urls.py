from django.urls import path

from django.conf.urls import include, url

from . import views
app_name = 'todo'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('index',views.index,name ='index'),
    path('detail',views.detail,name ='detail'),
    # ex: /polls/5/
    path('<int:id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]