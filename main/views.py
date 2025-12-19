from django.shortcuts import render
from .models import EntryModel
from django.views.generic import ListView,DetailView
# Create your views here.
class EntryModelView(ListView):
    model=EntryModel
    context_object_name="post"
    template_name="post.html"
    queryset=EntryModel.uploaded.all()