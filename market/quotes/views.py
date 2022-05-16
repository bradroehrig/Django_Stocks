from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List
from .forms import ListForm
from django.contrib import messages

from .models import Stock
from .forms import StockForm




def index(request):
    return render(request, "index.html")

# @login_required(login_url='/members/login_user')
# def home(request):
#     return render(request, "home.html")
        
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




















@login_required(login_url='/members/login_user')
def home(request):
    import requests
    import json
    
    if request.method == 'POST':
        ticker = request.POST['ticker']
        
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=pk_9235ca76a9104162b621848b60c87a7a")
    
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})
            
    else:
        return render(request, 'home.html')

@login_required(login_url='/members/login_user')
def about(request):
    return render(request, 'about.html', {})

@login_required(login_url='/members/login_user')
def base(request):
    return render(request, "base.html")

@login_required(login_url='/members/login_user')
def add_stock(request):
    import requests
    import json
    
    if request.method == 'POST':
        form = StockForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added!"))
            return redirect('add_stock')
    else:     
        ticker = Stock.objects.all()
        output =[]
        
        
        for ticker_item in ticker:        
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) +"/quote?token=pk_9235ca76a9104162b621848b60c87a7a")
    
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        
        return render(request, 'add_stock.html', {'ticker':ticker, 'output':output})

@login_required(login_url='/members/login_user')
def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect(add_stock)

@login_required(login_url='/members/login_user')
def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})