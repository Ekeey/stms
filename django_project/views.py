 # student_dash/views.py

from django.shortcuts import render

def index(request):
    """
    View function for the homepage of the student dashboard.
    """
    context = {
        'message': 'Welcome to the Student Dashboard!',
    }
    return render(request, 'index.html', context)
