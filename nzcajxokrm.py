import random
import string
from django.shortcuts import render
from django.http import HttpResponse

def random_string_view(request):
    """A Django view that renders a template with some context data."""
    # Generate some random data to pass to the template
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    context = {
        'random_string': random_string,
        'message': 'Hello from the Django view!',
    }
    return render(request, 'random_template.html', context)

def another_view(request):
    """Another simple Django view that returns an HttpResponse."""
    return HttpResponse("This is another Django view response.")