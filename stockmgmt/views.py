from django.shortcuts import render,redirect
from .models import Stock
from .forms import StockCreateForm,StockSearchForm,StockUpdateForm
# Create your views here.

def home(request):
	return render(request, "home.html",{})

def list_item(request):
	title = 'List of Items'
	#myfilter = StockFilter()
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	context = {
		"form": form,
		"title": title,
		"queryset": queryset,
		
	}
	if request.method == 'POST':
		queryset = Stock.objects.filter(item_name__icontains=form['item_name'].value(),
									)
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,}
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

def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('list_item')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)


def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('list_item')
	return render(request, 'delete_items.html')


