from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List
from .forms import ListForm
from django.contrib import messages

def index(request):
    return render(request, "index.html")

@login_required(login_url='/members/login_user')
def home(request):
    return render(request, "home.html")
        
@login_required(login_url='/members/login_user')
def base(request):
    return render(request, "base.html")

@login_required(login_url='/members/login_user')
def list(request):  
    if request.method == "POST":  
        form = ListForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_list')
            except:  
                pass  
    else:  
        form = ListForm()
    return render(request,'direct_list.html',{'form':form})  

@login_required(login_url='/members/login_user')
def show_list(request):  
    lists = List.objects.all()  
    return render(request,"show_list.html",{'lists':lists})  

@login_required(login_url='/members/login_user')
def edit_list(request, id):  
    list = List.objects.get(id=id)  
    return render(request,'edit_list.html', {'list': list})  

@login_required(login_url='/members/login_user')
def update_list(request, id):  
    list = List.objects.get(id=id)  
    form = ListForm(request.POST, instance = list)  
    if form.is_valid():  
        form.save()  
        return redirect("home")  
    return render(request, 'edit_list.html', {'list': list})  

@login_required(login_url='/members/login_user')
def destroy_list(request, id):  
    list = List.objects.get(id=id)  
    list.delete()  
    return redirect("/show_list")