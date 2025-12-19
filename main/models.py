from django.db import models

# Create your models here.
STATUS=[
    ("DRAFT","DRAFT"),
    ("UPLOADED","UPLOADED")
]

CATEGORY=[
    ("STUDY NOTES","STUDY NOTES"),
    ("LEARNIGN RESOURCES","LEARNIGN RESOURCES"),
    ("SHORT EXPLANATIONS","SHORT EXPLANATIONS"),
    ("IDEAS","IDEAS")
]

class EntryModel(models.Model):
    title=models.CharField()
    slug=models.SlugField(unique_to_date="publish")# tags the uniqueness of the flug to the publish field which is a date
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)# THe time cannot be editable
    updated=models.DateTimeField(auto_now=True)# time can be editable
    status=models.CharField(choices=STATUS)
    category=models.CharField(choices=CATEGORY)
