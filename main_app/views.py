from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Chocolate, Store
from .forms import OrderForm


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
    order_form = OrderForm()
    id_list = chocolate.stores.all().values_list('id')
    not_at_stores = Store.objects.exclude(id__in=id_list)
    return render(request, 'chocolates/detail.html', {
        'chocolate': chocolate, "order_form": order_form, "stores": not_at_stores
    })

def add_order(request, chocolate_id):
  # create a ModelForm instance using 
  # the data that was submitted in the form
  form = OrderForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # we can't save to the db yet
    # because we have not assigned the
    # cat_id FK.
    new_order = form.save(commit=False)
    new_order.chocolate_id = chocolate_id
    new_order.save()
  return redirect('detail', chocolate_id=chocolate_id)


class ChocolateCreate(CreateView):
  model = Chocolate
  fields = '__all__'

class ChocolateUpdate(UpdateView):
  model = Chocolate
  fields = ['type', 'description', 'flavor']

class ChocolateDelete(DeleteView):
  model = Chocolate
  success_url = '/chocolates'

class StoreList(ListView):
  model = Store

class StoreDetail(DetailView):
  model = Store

class StoreCreate(CreateView):
  model = Store
  fields = '__all__'

class StoreUpdate(UpdateView):
  model = Store
  fields = ['name', 'distance']

class StoreDelete(DeleteView):
  model = Store
  success_url = '/stores'

def assoc_store(request, chocolate_id, store_id):
  Chocolate.objects.get(id=chocolate_id).stores.add(store_id)
  return redirect('detail', chocolate_id=chocolate_id)

def unassoc_store(request, chocolate_id, store_id):
  Chocolate.objects.get(id=chocolate_id).stores.remove(store_id)
  return redirect('detail', chocolate_id=chocolate_id)