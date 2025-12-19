from django.urls import path
from .views import EntryModelView


app_name="post"
urlpatterns=[
    path("post/",EntryModelView.as_view(),name="post"),
    path("<int:year>/<int:month>/<int:date>",EntryModelViewDetail.as_view(),name="post_detail")
]   