from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
from .models import Choice

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def index(request):
	post=Question.objects.all()
	return render(request, 'polls/index.html',{'post':post})

def home(request):
	return render(request, 'polls/home.html')

def cart(request):
	context = {}
	return render(request, 'polls/cart.html', context)

def choice(request):
	post = Choice.objects.all()
	return render(request, 'polls/choice.html',{'post':post})
def register(request):
	form=UserCreationForm
	if request.method=='POST':
		regForm=UserCreationForm(request.POST)
		if regForm.is_valid():
			regForm.save()
			messages.success(request, 'user has been registered.')
	return render(request,'polls/register.html',{'form':form})

