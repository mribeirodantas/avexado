from django.db import models


class Page(models.Model):
    name = models.CharField(max_length='20', primary_key=True)
    content = models.TextField(blank=True, null=True)
    last_edited_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
