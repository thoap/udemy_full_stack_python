from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

import misaka

from second_clone.groups import models as group_models

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(
        group_models.Group, related_name='Posts', null=True, blank=True
    )

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'posts:single',
            kwargs={
                'username': self.user.username,
                'pk': self.pk
            }
        )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']