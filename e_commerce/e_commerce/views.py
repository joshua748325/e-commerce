from django.shortcuts import render

def custom_403_view(request,exception):
    return render(request, 'core/403.html')

def custom_404_view(request,exception):
    return render(request, 'core/404.html')

def custom_500_view(request):
    return render(request,'core/500.html')