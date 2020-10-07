from django.shortcuts import render,redirect
from .models import Stock
from .forms import StockCreateForm

# Create your views here.

def home(request):
	return render(request, "home.html",{})

def list_item(request):
	title = 'List of Items'
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "list_item.html", context)

def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_item')

	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)