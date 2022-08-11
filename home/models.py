from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    #dictates what the model is printed out as 
    def __str__(self):
        return self.name

#Project Fields
class Project(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    lessons = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images", default="test123.jpg")
    #takes tags from other model
    tags = models.ManyToManyField(Tag, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
