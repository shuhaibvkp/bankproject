from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
# Create your views here.
def first(request):
    return HttpResponse('my first django page')

def second(request):
    return render(request,'first.html')

def four(request):
    return render(request,'registration.html')

def five(request):
    return render(request,'login.html')

def external(request):
    return render(request,'external files.html')

def register(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['first_name']
            ln=a.cleaned_data['last_name']
            em=a.cleaned_data['email']
            ps=a.cleaned_data['psw']
            cps=a.cleaned_data['cpsw']
            if ps == cps:
                b=reg_model(first_name=fn,last_name=ln,email=em,psw=ps)
                b.save()
                return redirect(login_view)
            else:
                return HttpResponse('password doesnt match')
        else:
            return HttpResponse('registration failed')
    return render(request,"reg.html")


def login_view(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=reg_model.objects.all()
            for i in b:
                if i.email==em and i.psw==ps:
                    return redirect(homeview)
            else:
                return HttpResponse('login failed')
    return render(request,"login.html")


def display(request):
    b=reg_model.objects.all()
    return render(request,'display.html',{'c':b})

def deletedata(request,id):
    a=reg_model.objects.get(id=id)
    a.delete()
    return redirect(display)

def fileupload(request):
    if request.method=='POST':
        a=fileform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['filename']
            fl=a.cleaned_data['file']
            b=filemodel(filename=fn,file=fl)
            b.save()
            return HttpResponse('file upload success')
        else:
            return HttpResponse('file upload file')
    return render(request,'fileupload.html')


def filedisplay(request):
    a=filemodel.objects.all()
    id=[]
    flnm=[]
    img=[]
    for i in a:
        id1=i.id
        id.append(id1)
        nm=i.filename
        flnm.append(nm)
        im=str(i.file).split('/')[-1]
        img.append(im)
    pair=zip(flnm,img,id)
    return render (request,'filedisplay.html',{'b':pair})

def filedelete(request,id):
    a=filemodel.objects.get(id=id)
    os.remove(str(a.image))
    a.delete()
    return redirect(filedisplay)
def fileedit(request,id):
    a=filemodel.objects.get(id=id)
    img=str(a.file).split('/')[-1]
    if request.method=='POST':
        a.filename=request.POST.get('imgname')
        if len(request.FILES)!=0:
            if len(a.file)!=0:
                os.remove(a.file.path)
            a.file=request.FILES['image']
        a.save()
        return redirect(filedisplay)
    return render(request,'editfile.html',{'a':a,'img':img})









def cardupload(request):
    if request.method=='POST':
        a=cardform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['product']
            pc=a.cleaned_data['price']
            ds=a.cleaned_data['discript']
            fl=a.cleaned_data['file']
            b=cardmodel(product=fn,price=pc,discript=ds,file=fl)
            b.save()
            return HttpResponse('card upload success')
        else:
            return HttpResponse('card upload file')
    return render(request,'cardupload.html')


def carddisplay(request):
    a=cardmodel.objects.all()
    flnm=[]
    prc=[]
    dsc=[]
    img=[]
    for i in a:
        nm=i.product
        flnm.append(nm)
        pr=i.price
        prc.append(pr)
        dg=i.discript
        dsc.append(dg)
        im=str(i.file).split('/')[-1]
        img.append(im)
    pair=zip(flnm,prc,dsc,img)
    return render (request,'cardisplay.html',{'b':pair})

def videoupload(request):
    if request.method=='POST':
        a=videoform(request.POST,request.FILES)
        if a.is_valid():
            vn=a.cleaned_data['videoname']
            vi=a.cleaned_data['video']
            an=a.cleaned_data['audioname']
            ai=a.cleaned_data['audio']
            pn = a.cleaned_data['pdfname']
            pi = a.cleaned_data['pdf']
            b=videomodel(videoname=vn,video=vi,audioname=an,audio=ai,pdfname=pn,pdf=pi)
            b.save()
            return HttpResponse(' upload success')
        else:
            return HttpResponse('upload failed')
    return render(request,'videoupload.html')


def avpddisplay(request):
    a=videomodel.objects.all()

    vnm=[]
    vn=[]
    anm=[]
    an=[]
    pdnm=[]
    pd=[]
    for i in a:

        vdn=i.videoname
        vnm.append(vdn)
        vd=str(i.video).split('/')[-1]
        vn.append(vd)
        adn = i.audioname
        anm.append(adn)
        ad = str(i.audio).split('/')[-1]
        an.append(ad)
        pdn = i.pdfname
        pdnm.append(pdn)
        pdf = str(i.pdf).split('/')[-1]
        pd.append(pdf)

    pair=zip(vnm,vn,anm,an,pdnm,pd)
    return render (request,'avpdisplay.html',{'b':pair})

def avpdelete(request,id):
    a=videomodel.objects.get(id=id)
    os.remove(str(a.video))
    os.remove(str(a.audio))
    os.remove(str(a.pdf))
    a.delete()
    return redirect(avpdisplay)

def avpedit(request,id):
    a=videomodel.objects.get(id=id)
    vid=str(a.video).split('/')[-1]
    aud=str(a.audio).split('/')[-1]
    pd=str(a.pdf).split('/')[-1]
    if request.method == 'POST':
        a.videoname = request.POST.get('videoname')
        a.audioname=request.POST.get('audioname')
        a.pdfname=request.POST.get('pdfname')
        if request.FILES.get('video')==None:

            a.save()
        else:
              a.video = request.FILES['video']
        if request.FILES.get('audio')==None:

            a.save()
        else:
            a.audio = request.FILES['audio']
        if request.FILES.get('pdf')==None:

            a.save()
        else:
            a.pdf = request.FILES['pdf']
        a.save()
        return redirect(avpdisplay)
    return render(request, 'audvidpdedit.html', {'a': a, 'vid': vid,'aud':aud,'pd':pd})


def indexview(request):
    return render(request,'index.html')

def homeview(request):
    return render(request,'home.html')

def editdata(request,id):
    a=reg_model.objects.get(id=id)
    if request.method=='POST':
        a.first_name=request.POST.get('first_name')
        a.last_name = request.POST.get('last_name')
        a.email = request.POST.get('email')
        a.save()
        return redirect(display)

    return render (request,'editdata.html',{'a':a})

def dateupload(request):
    if request.method=='POST':
        a=dateform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['first_name']
            fl=a.cleaned_data['date']
            b=datemodel(first_name=fn,date=fl)
            b.save()
            return HttpResponse('date upload success')
        else:
            return HttpResponse('date upload filed')
    return render(request,'dateedit.html')

def datedisplay(request):
    b=datemodel.objects.all()
    return render(request,'datedisplay.html',{'c':b})

def editdate(request,id):
    a=datemodel.objects.get(id=id)
    if request.method=='POST':
        if request.POST.get('date') == '':
            a.save()
        else:
            a.date = request.POST.get('date')
        a.first_name = request.POST.get('first_name')
        a.save()
        return redirect(datedisplay)


    return render (request,'editdate.html',{'a':a})

def check(request):
    if request.method=='POST':
        a=checkform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['firstname']
            gd = a.cleaned_data['gender']
            dt= a.cleaned_data['date']
            st = a.cleaned_data['state']
            e=request.POST.get('eng')
            if e=='on':
                e=True
            else:
                e=False
            m = request.POST.get('mal')
            if m == 'on':
                m = True
            else:
                m = False
            h = request.POST.get('hind')
            if h == 'on':
                h = True
            else:
                h = False
            b=checkmodel(firstname=nm,gender=gd,date=dt,state=st,eng=e,mal=m,hind=h)
            b.save()
            return HttpResponse('success')
        else:
            return HttpResponse('Failed')
    return render(request,'regform.html')

def formdisplay(request):
    b=checkmodel.objects.all()
    return render(request,'formdisplay.html',{'c':b})

def index (request):
    return render(request,'index.html')

def indexx (request):
    return render(request,'index1.html')