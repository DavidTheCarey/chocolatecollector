from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chocolate

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def chocolates_index(request):
  # We pass data to a template very much like we did in Express!
  chocolates = Chocolate.objects.all()
  return render(request, 'chocolates/index.html', {
    'chocolates': chocolates
  })

def chocolate_detail(request, chocolate_id):
    chocolate = Chocolate.objects.get(id=chocolate_id)
    return render(request, 'chocolates/detail.html', {
        'chocolate': chocolate
    })

class ChocolateCreate(CreateView):
  model = Chocolate
  fields = '__all__'

class ChocolateUpdate(UpdateView):
  model = Chocolate
  fields = ['type', 'description', 'flavor']

class ChocolateDelete(DeleteView):
  model = Chocolate
  success_url = '/chocolates'