from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('psot_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
