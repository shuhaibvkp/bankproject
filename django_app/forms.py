from django import forms


class regform(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email=forms.EmailField()
    psw=forms.CharField(max_length=20)
    cpsw=forms.CharField(max_length=20)


class logform(forms.Form):
    email =forms.EmailField()
    password =forms.CharField(max_length=20)

class fileform(forms.Form):
    filename=forms.CharField(max_length=30)
    file=forms.FileField()


class cardform(forms.Form):
    product=forms.CharField(max_length=30)
    price=forms.IntegerField()
    discript=forms.CharField(max_length=30)
    file=forms.FileField()

class videoform(forms.Form):
    videoname=forms.CharField(max_length=30)
    video=forms.FileField()
    audioname = forms.CharField(max_length=30)
    audio = forms.FileField()
    pdfname = forms.CharField(max_length=30)
    pdf = forms.FileField()


class dateform(forms.Form):
    first_name = forms.CharField(max_length=50)
    date = forms.DateField()

class checkform(forms.Form):
    firstname=forms.CharField(max_length=20)
    gender=forms.CharField(max_length=20)
    date=forms.DateField()
    state=forms.CharField(max_length=20)