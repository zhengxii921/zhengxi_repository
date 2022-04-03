from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import PlaceCreateForm
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "numazutourist/index.html"


class ReviewListView(generic.ListView):
    model = Review


class PlaceListView(generic.ListView):
    model = Place


class PlaceCreateView(generic.CreateView):
    model = Place
    form_class = PlaceCreateForm
    success_url = reverse_lazy("numazutourist:places")