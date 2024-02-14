from django.db import models
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return "#{}".format(self.name)


class Note(models.Model):
    title = models.CharField(max_length=200, default="Note title")
    note_text = models.CharField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tags")

    def __str__(self) -> str:
        return self.title
    
    def html_view(self):
        tags_str = ""
        for tag in self.tags.all():
            tags_str += str(tag) + " "
        return "<h3>{}</h1>{}<br>{}<hr>".format(self.title, self.note_text, tags_str)
