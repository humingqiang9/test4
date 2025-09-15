from django.shortcuts import render
from django.http import HttpResponse

def random_view(request):
    """
    A Django view that renders a template
    """
    context = {
        'message': 'Hello from the random Django view!',
        'items': ['item1', 'item2', 'item3']
    }
    return render(request, 'random_template.html', context)

def another_view(request):
    """
    Another Django view example
    """
    return HttpResponse("This is another view response")