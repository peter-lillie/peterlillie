from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def landing_page(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="core/landing_page.html")