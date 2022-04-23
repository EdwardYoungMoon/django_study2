from re import template
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.conf import settings

from blog.models import Post

from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

class PostLV(ListView):
    model = Post # PostLV 클래스의 대상 테이블은 Post 테이블이다.
    template_name = 'blog/post_all.html' # 템플릿 파일 지정. 지정하지 않으면 파일명은 'blog/post_list.html'이 된다.
    context_object_name = 'posts' # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명 지정. 
    paginate_by = 2 # 한 페이지에 보여주는 객체 리스트의 숫자. 페이징 기능이 활성화되면 하단에 페이지 이동 버튼을 만들 수 있다.

class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        # 책이랑 다름 
        return Post.objects.filter(tags__name__in = [self.kwargs.get('tag')]) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

# Form View
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) 
        | Q(description__icontains=searchWord) 
        | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_form'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context) # No Redirection
# 84쪽까지


