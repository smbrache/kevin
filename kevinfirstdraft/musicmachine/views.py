from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == "POST":
        response = HttpResponse(open("kevinfirstdraft/testdownloads/downloadfile.txt", 'rb').read())
        response['Content-Type'] = 'text/plain'
        response['Content-Disposition'] = 'attachment; filename=DownloadedText.txt'
        return response

    return render(request, 'musicmachine/home.html')

