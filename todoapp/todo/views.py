from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

# 목록 화면 뷰
def todo_list(request):  # 완료되지 않은 Todo 만 전달해야하므로 complete = False filtering
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html',{'todos':todos})

# 상세 조회 뷰
def todo_detail (request,pk):
    todo = Todo.objects.get(id=pk)  # todo 변수에 Todo model로 들어오는 데이터를 id로 구분해서 하나씩 가져와 저장
    return render (request, 'todo/todo_detail.html', {'todo':todo})

def todo_post(request):
    if request.method == "POST":    # POST 요청이 들어오는 경우
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:  # GET 요청이 들어오는 경우
        form = TodoForm()
    return render(request,'todo/todo_post.html',{'form':form})

# 수정 뷰
def todo_edit(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request,'todo/todo_edit.html',{'form':form})

def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html',{'dones':dones})
   
# dones 변수에 저장 : complete = True 로 필터링 된 데이터
# 완료로 바꾸는 뷰

def todo_done(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')
 
# Todo 객체를 id 로 구분 > todo 변수에 저장 > todo를 complet=True 로 설정 > todo.save()로 상태 저장
