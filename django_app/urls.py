from django.urls import path
from.views import *
urlpatterns=[
    path('first/',first),
    path('second/',second),

    path('four/',four),
    path('five/',five),
    path('external/',external),
    path('registration/',register),
    path('loginpage/',login_view),
    path('display/',display),
    path('fileupload/',fileupload),
    path('filedisplay/',filedisplay),
    path('cardupload/',cardupload),
    path('cardisplay/',carddisplay),
    path('videoupload/',videoupload),
    path('avpdisplay/',avpddisplay),
    path('indexview/',indexview),
    path('homeview/',homeview),
    path('delete/<int:id>',deletedata),
    path('edit/<int:id>',editdata),
    path('date/',dateupload),
    path('datedisplay/',datedisplay),
    path('editdate/<int:id>',editdate),
    path('forms/',check),
    path('formdisplay/',formdisplay),
    path('filedelete/<int:id>',filedelete),
    path('editfile/<int:id>',fileedit),
    path('avpedit/<int:id>',avpedit),
    path('index/',index),
    path('index1/',indexx)



]