import random
import string
from django.shortcuts import render
from django.http import HttpResponse


def random_string_view(request):
    """
    A Django view that renders a template with some context data.
    """
    # Generate some random data to pass to the template
    random_data = {
        'random_string': ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        'random_number': random.randint(1, 100),
    }
    
    # Render the template with the context data
    return render(request, 'random_template.html', context=random_data)


def another_sample_view(request):
    """
    Another example view that renders a different template.
    """
    items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    return render(request, 'list_template.html', {'items': items})


def simple_response_view(request):
    """
    A view that returns a simple HttpResponse.
    """
    return HttpResponse("Hello, this is a simple response!")
