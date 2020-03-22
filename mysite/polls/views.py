from django.http import HttpResponse


def index(request):
    print(request)
    print(dir(request))
    print(request.META)
    try:
        1/0
    except:
        return HttpResponse("error rtya again with other values")        
    return HttpResponse("Hello,sdfsdfsdfsdfsd world. You're at the polls index.")
