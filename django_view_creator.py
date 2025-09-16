import random
import string

def generate_random_filename():
    """Generate a random filename with .py extension"""
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{random_chars}.py"

def create_django_view():
    """Create Django view code that renders a template"""
    view_code = '''from django.shortcuts import render
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
'''
    return view_code

def save_to_file(filename, content):
    """Save content to a file"""
    with open(filename, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    # Generate random filename
    filename = generate_random_filename()
    
    # Create Django view code
    view_content = create_django_view()
    
    # Save to file
    save_to_file(filename, view_content)
    
    print(f"Django view saved to {filename}")