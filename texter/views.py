#created this file-nj

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse ('''<h1>hello world</h1>''')


def about(request):
    return HttpResponse ('''About this page <button href="/">home</button>''')

def urls(request):
    return HttpResponse ('''Link navigation <br> <a href="https://twitter.com/home" target="_blank">My twitter home</a> <br> <a href="https://www.linkedin.com/feed/" target="_blank">My LinkedIn home</a><br> <a href="https://mail.yahoo.com/d/folders/1?.intl=in&.lang=en-IN&.partner=none&.src=fp" target="_blank">My Yahoo home</a><br> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7" target="_blank">Django tutorial</a><br> <a href="https://web.whatsapp.com/" target="_blank">My WhatsApp</a> <br><button href="/">home</button>''')     


