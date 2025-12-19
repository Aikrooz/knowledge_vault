from django.shortcuts import render
from .models import EntryModel
from django.views.generic import ListView,DetailView
# Create your views here.
class EntryModelView(ListView):
    model=EntryModel
    context_object_name="post"
    template_name="post.html"
    queryset=EntryModel.uploaded.all()
    paginate_by=5

class EntryModelViewDetail(DetailView):
    model=EntryModel
    context_object_name="post"
    template_name="post_detail.html"
    queryset=EntryModel.uploaded.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class EntryModelDraftView(ListView):
    model=EntryModel
    context_object_name="post"
    template_name="draft.html"
    queryset=EntryModel.draft.all()
    paginate_by=5

class EntryModelDraftViewDetail(DetailView):
    model=EntryModel
    context_object_name="post"
    template_name="draft_detail.html"
    queryset=EntryModel.draft.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

