from django.shortcuts import render,redirect
from vege.models import *

# Create your views here.
def recipe(request):
  if request.method == "POST":  
    data=request.POST
    reciepe_image=request.FILES.get('reciepe_image')
    reciepe_name1=data.get('reciepe_name')
    reciepe_desc=data.get('reciepe_desc')
   
    Receipe.objects.create(
      reciepe_name=reciepe_name1,
      reciepe_image=reciepe_image,
      reciepe_desc=reciepe_desc,
    )

    return redirect('/reciepe')
  
  querryset=Receipe.objects.all()
  context={'receipes':querryset}
  
  return render(request,"add_reciepies.html",context=context)
  
