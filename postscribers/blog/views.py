#from multiprocessing import context
from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm


def index(request):
    posts = PostModel.objects.all().order_by('-date_created')
    if request.method == 'POST':
      form = PostModelForm(request.POST)
   
    if form.is_valid():
            instance = form.save(commit=False) 
            instance.author = request.user 
            instance.save()
            return redirect('index-blog')
           
    else:
       form = PostModelForm()
    
    context={
        'posts':posts,
        'form':form,
    }
    return render(request, 'blog/index.html', context) 




