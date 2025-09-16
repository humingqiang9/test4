from django.shortcuts import render
from django.http import HttpResponse

def my_template_view(request):
    """
    A Django view that renders a template
    """
    context = {
        'title': 'My Django App',
        'message': 'Hello from Django!',
        'items': ['apple', 'banana', 'cherry']
    }
    return render(request, 'my_template.html', context)

def another_view(request):
    """
    Another Django view example
    """
    return HttpResponse("This is another view")
