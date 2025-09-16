from django.shortcuts import render

def my_template_view(request):
    """
    A simple Django view that renders a template.
    """
    context = {
        'message': 'Hello from the Django view!',
        'user': request.user if request.user.is_authenticated else 'Guest'
    }
    return render(request, 'my_template.html', context)