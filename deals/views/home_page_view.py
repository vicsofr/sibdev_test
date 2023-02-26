from django.shortcuts import render, redirect


def home_page_view(request):
    return render(request, 'home.html')
