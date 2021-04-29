from django.shortcuts import render

def homeMaster(request):
     
    data = {
            
    }
    return render(request,'homeMaster.html',data)


