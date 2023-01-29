from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.


def display_topics(request):
    QST=Topic.objects.all()
    d={'topics': QST}
    return render(request,'display_topics.html', d)
      

def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.filter(topic_name='cricket')
    QSW=Webpage.objects.exclude(topic_name='cricket')
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.all().order_by('-name')
    QSW=Webpage.objects.all().order_by(Length('name'))
    QSW=Webpage.objects.filter(topic_name='cricket').order_by('-name')
    QSW=Webpage.objects.all().order_by(Length('name'))
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    QSW=Webpage.objects.filter(name__startswith='D')
    QSW=Webpage.objects.filter(name__regex='\w{7}')
    d={'webpages': QSW}
    return render(request,'display_webpages.html', d)


def display_accessrecords(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='1998-08-10')
    QSA=AccessRecords.objects.filter(date__gt='1988-08-18')
    QSA=AccessRecords.objects.filter(date__gte='1980-07-04')
    QSA=AccessRecords.objects.filter(date__lte='1980-08-12')
    QSA=AccessRecords.objects.filter(date__year='1998')
    QSA=AccessRecords.objects.filter(date__month='1')
    QSA=AccessRecords.objects.filter(date__day='08')
    QSA=AccessRecords.objects.filter(date__year__gt='1990')
    d={'accessrecords': QSA}
    return render(request,'display_accessrecords.html', d)

     
def update_webpage(request):
    #Webpage.objects.filter(name='chinni').update(url='https://basha.in')
    #Webpage.objects.filter(topic_name='Cricket').update(name='MSD')
    #Webpage.objects.filter(name='bangaram').update(topic_name='Cricket')
    #Webpage.objects.filter(name='chinni').update(topic_name='Hockey')
    #Webpage.objects.update_or_create(name='suresh',defaults={'url':'https://suresh.in'})
    #Webpage.objects.update_or_create(name='MSD',defaults={'url':'https://MSD.in'})
    T=Topic.objects.get_or_create(topic_name='Cricket')[0]
    T.save()
    Webpage.objects.update_or_create(name='ashu',defaults={'topic_name':T,'url':'https://suresh.in'})
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d) 


def delete_webpage(request):
    Webpage.objects.filter(name='Abcdefg').delete()
    Webpage.objects.filter(topic_name='Cricket').delete()
    Webpage.objects.filter(name='chinni').delete()
    Webpage.objects.all().delete()
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)





























