from django.shortcuts import render


# Create your views here.
def index(request):
  """The home page for dpsj."""
  return render(request, 'index.html')
