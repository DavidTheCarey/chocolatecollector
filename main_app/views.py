from django.shortcuts import render

chocolates = [
  {'name': 'Melt-Aways', 'type': 'Whipped', 'description': 'A delectable confectionery piece so smooth and so perfect it melts in your mouth', 'flavor': "Milk Chocolate"},
  {'name': 'Butter Cream', 'type': 'Cream Filled', 'description': 'A delicious confectionery piece with a familiar creamy center', 'flavor': "Dark Chocolate"},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def chocolates_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'chocolates/index.html', {
    'chocolates': chocolates
  })
