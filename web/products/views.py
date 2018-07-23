from django.shortcuts import render
from .models import Products
# Create your views here.

def products_detail_view(request):
	obj = Products.objects.get(id=1)
	# context= {
	# 	'title' : obj.tite,
	# 	'description' : obj.description
	# }
	context = {
	'object' : obj,
	}
	return render(request, 'product/product_detail.html', context)

def product_created_view(request):	
	#print(request.GET)
	#print(request.POST)
	if request.method == "POST":
		my_new_title=request.POST.get('Title')
		print(my_new_title)

	context = {}
	return render(request,'product/product_created.html', context)