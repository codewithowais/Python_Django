from django.http import HttpResponse


def indexabc(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def myfirstfunc(request):
    return HttpResponse('hello world')
