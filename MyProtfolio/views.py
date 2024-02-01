# contains functions and classes that handle what data is displayed in the HTML templates

from django.shortcuts import render

# render an HTML file named home.html
def home(request):
    return render(request, "MyProtfolio/home.html", {})
