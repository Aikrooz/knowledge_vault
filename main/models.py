from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
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

class PublishedEntryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="UPLOADED")

class DraftEntryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="DRAFT")

class EntryModel(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique_for_date="published")# tags the uniqueness of the flug to the publish field which is a date
    content=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="knowledge_vault",null=True,blank=True)
    published=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)# THe time cannot be editable
    updated=models.DateTimeField(auto_now=True)# time can be editable
    status=models.CharField(choices=STATUS,default="DRAFT")
    category=models.CharField(choices=CATEGORY,default="STUDY NOTES")
    objects = models.Manager()  # Default manager
    uploaded=PublishedEntryManager()
    draft=DraftEntryManager()

    class Meta:
        ordering=("-published",)

    def __str__(self):
        return self.title

    def get_unique_url(self):
        return reverse("vault:post_detail",
        args=[
            self.published.year,
            self.published.month,
            self.published.day,
            self.slug
        ])

    def get_draft_url(self):
        return reverse("vault:draft_detail",
        args=[
            self.published.year,
            self.published.month,
            self.published.day,
            self.slug
        ])

    


