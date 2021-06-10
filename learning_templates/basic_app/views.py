from django.shortcuts import render

# Create your views here.
def home(request):
    context_dict = {'text':'hello world','number':100}
    return render(request, 'basic_app/home.html',context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
