from django.shortcuts import render, redirect
from .models import Tasks
from django.contrib.auth.models import User, auth

# Create your views here.
def checkBox(val):
	if len(val) == 1:
		return True
	else:
		return False
def index(request):
	if not request.user.is_authenticated :
		return redirect('/')
	tasks=Tasks.objects.filter(user=request.user.username)
	context={'tasks':tasks}
	if request.method == 'POST':
		title = request.POST['title']
		title = title.strip()
		task = Tasks(title=title, user = request.user.username)
		if(len(title)!=0):
			task.save()
		return redirect('/index/')
	else:
		return render(request, 'index.html',context)

def update(request, pkey):
	if(not Tasks.objects.filter(id=pkey).exists()):
		return redirect('/index')
	task = Tasks.objects.get(id=pkey)
	if(task.user != request.user.username):
		return redirect('/index')
	if(request.method=="POST"):
		if request.POST["update"]=="Cancel":
			return redirect('/index')
		title = request.POST["title"]
		title = title.strip()
		if(title==""):
			return redirect('/index')
		completed = request.POST.getlist("completed")
		task.title = title
		task.completed = checkBox(completed)
		task.save()
		return redirect('/index')
	else:
		return render(request, 'update.html',{'task':task})

def delete(request, pkey):
	task = Tasks.objects.get(id=pkey)
	if(request.method == "POST"):
		choice = request.POST["choice"]
		if(choice == "Delete"):
			task.delete()
		return redirect('/index')
		# else:
		# 	redirect('/')
	else:
		return render(request, 'delete.html', {'task':task})
