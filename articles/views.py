from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.views.generic import (ListView,
                                  DetailView)
from django.views.generic.edit import (UpdateView,
                                       DeleteView,
                                       CreateView)
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(LoginRequiredMixin,
                      ListView):
    '''
    View For Article List
    '''
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin,
                        DetailView):
    '''
    View For Article Detail
    '''
    model = Article
    template_name = 'article_detail.html'
    
    
class ArticleUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        UpdateView):
    '''
    View For Updating An Article
    '''
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'
    
    def test_func(self):
        '''
        Article Author Validation
        '''
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        DeleteView):
    '''
    View For Deleting An Article
    '''
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    
    def test_func(self):
        '''
        Article Author Validation
        '''
        obj = self.get_object()
        return obj.author == self.request.user

    
class ArticleCreateView(LoginRequiredMixin,
                        CreateView):
    '''
    View For creating An Article
    '''
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_new.html'
    
    def form_valid(self, form):
        '''
        Setting The Author As The Current User
        '''
        form.instance.author = self.request.user 
        return super().form_valid(form) # Form Validation