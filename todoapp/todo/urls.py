from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo_list, name='todo_list'), # 주소에 todo_list view 연결
    path('<int:pk>/',views.todo_detail, name ='todo_detail'), # url > /pk/ 설정하여 해당하는 pk의 Todo 연결, pk : 몇 번째 todo인지 구분하기 위함
    path('post/',views.todo_post, name='todo_post'),
    path('<int:pk>/edit/',views.todo_edit,name='todo_edit'),
    path('done/',views.done_list, name='done_list'),
    path('done/<int:pk>/', views.todo_done,name = 'todo_done'),
]