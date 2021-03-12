from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Steps
from django.shortcuts import redirect

# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        if request.POST['steps'] and request.POST['date']:
            inst = Steps()
            inst.steps = request.POST['steps']
            inst.date = request.POST['date']
            inst.owner = request.user
            inst.save()
            return redirect('home')
        else:
            return render(request, 'steps/home.html', {'error': 'All fields are required.'})
    else:        
        return render(request, 'steps/home.html')