from django.views.generic import ListView
from .models import Cmdr

class HomePageView(ListView):
    model = Cmdr
    template_name = 'index.html'

# Create your views here.
