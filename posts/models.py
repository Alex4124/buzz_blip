from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=280, verbose_name='Text')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-published']
