from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class Article(models.Model):
    '''
    Model For News Article
    '''
    
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    '''
    Model For Article Comments
    '''
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('article_list')
    
