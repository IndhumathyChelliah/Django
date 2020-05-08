from django.shortcuts import render
from karthiapp import forms

def index(request):
    return render (request,'index.html')

def info(request):
    form = forms.FormName()
    if request.method=="POST":
        form=forms.FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
            #return HttpResponseRedirect('/index/')
        else:
            print ("ERROR FORM INVALID")

    return render(request,'info.html',{'form':form})

def success(request):
    return render(request,'success.html')

