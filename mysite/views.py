from django.http import HttpResponse

#主页
def main_index(request):
    return HttpResponse('Main_page')