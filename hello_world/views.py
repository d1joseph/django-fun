from django.shortcuts import render

# Create your views here.
def hello_world(request):
    """ Basic view function: takes an argument 
    'request', which is an HttpRequestObject, and
    renders html along with model data. """
    return render(request, 'hello_world.html', {})