from django.shortcuts import render

def apps(request):
        return render(request, 'apps/archivo.html')