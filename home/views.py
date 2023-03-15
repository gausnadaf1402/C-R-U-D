from django.shortcuts import render,HttpResponse,redirect
from home.models import Entry

# Create your views here.
def index(request):
    return render(request,'home.html')

def show(request):
    data=Entry.objects.all()
    return render(request,'show.html',{'data':data})

def send(request):
    if request.method=='POST':
        ID=request.POST['id']
        Data1=request.POST['data1']
        Data2=request.POST['data2']
        en=Entry(ID=ID,Data1=Data1,Data2=Data2)
        en.save()
        msg='data stored successfully'
        return render(request,'home.html',{'msg':msg})
    else:
        return HttpResponse('this is send')
    
def delete(request):
    ID=request.GET['id']
    Entry.objects.filter(ID=ID).delete()
    return redirect('show')

def edit(request):
    ID = request.GET['id']
    Data1 = Data2 = "Not Available"
    for data in Entry.objects.filter(ID=ID):
        Data1 = data.Data1
        Data2 = data.Data2
    return render(request,"edit.html",{'ID':ID,'data1':Data1,'data2':Data2})

def recordedit(request):
    if request.method == 'POST':
        ID = request.POST['id']
        Data1 = request.POST['data1']
        Data2 = request.POST['data2']
        Entry.objects.filter(ID=ID).update(Data1=Data1,Data2=Data2)
        return redirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
