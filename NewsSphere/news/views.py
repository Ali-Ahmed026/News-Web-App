from django.http import HttpResponse


def home(request):
    return HttpResponse("NewsSphere is running.")