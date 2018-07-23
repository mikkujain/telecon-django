from django.shortcuts import render
from django.http import HttpResponse
from .forms import PagesForm
# Create your views here.
def home_view(request,*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	#return HttpResponse("<h1> Hello Mikku</h1>")
	return render(request,"page/page_home.html", {})

def contact_view(request,*args,**kwargs):
	my_context = {
		'my_text' : 'Hello dosto',
		'my_number': 24,
		'my_list' : ['Mikku',25,'Mayank',12],
		'my_html' : "<h1> Hello najkcbj</h1>"

	}
	return render(request,"page/page_contact.html", my_context)

def about_view(request,*args,**kwargs):
	return render(request,"page/page_about.html", {})

def page_created_view(request):
	form = PagesForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = PagesForm()
	context = {
		'form' : form,
	}
	return render(request,'page/page_created.html', context)