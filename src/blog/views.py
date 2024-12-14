from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def article(request, number_article):
    return render(request, f"blog/article_{number_article}.html")