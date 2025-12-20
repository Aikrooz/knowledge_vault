from django.urls import path
from .views import EntryModelView,EntryModelDraftView,EntryModelViewDetail,EntryModelDraftViewDetail


app_name="post"
urlpatterns=[
    path("post/",EntryModelView.as_view(),name="post"),
    path("<int:year>/<int:month>/<int:date>",EntryModelViewDetail.as_view(),name="post_detail"),
    path("detail/",EntryModelDraftView.as_view(),name="draft"),
    path("<int:year>/<int:month>/<int:date>",EntryModelDraftViewDetail.as_view(),name="draft_detail")
]   