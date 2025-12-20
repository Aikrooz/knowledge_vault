from django.urls import path
from .views import EntryModelView,EntryModelDraftView,EntryModelViewDetail,EntryModelDraftViewDetail


app_name="vault"
urlpatterns=[
    path("post/",EntryModelView.as_view(),name="post"),
    path("<int:year>/<int:month>/<int:date>/<slug:slug>/",EntryModelViewDetail.as_view(),name="post_detail"),
    path("draft/",EntryModelDraftView.as_view(),name="draft"),
    path("draft/<int:year>/<int:month>/<int:date>/<slug:slug>/",EntryModelDraftViewDetail.as_view(),name="draft_detail")# cannot be the same or else it will be heading to the post.detail page
]   