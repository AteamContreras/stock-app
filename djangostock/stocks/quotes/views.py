from django.shortcuts import render, redirect
import json
import requests
from .models import Stock
from django.contrib import messages
from .forms import StockForm

#Defining how to request for the homepage.html
def home(request):

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_d30bf9bf67574d449c3d283759ffa5e7")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'homepage.html', {'api': api})
    else:
        return render(request, 'homepage.html', {'ticker': "Click the Menu in the top right, and type in a ticker symbol inside the search bar.. ."})


def about(request):
    return render(request, 'aboutpage.html', {})


def watchlist(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added!"))
            return redirect('watchlist')

    else:
        ticker = Stock.objects.all()
        return render(request, 'watchlist.html', {'ticker': ticker})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect(watchlist)