from django.shortcuts import render,redirect
from django.http import HttpResponse
from article.models import Article
from django.db.models import Q
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    arg = {'post' : post}
    ret = count_art(arg)
    return render(request, 'post.html', ret)


def home(request):
    posts = Article.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 3) #每页显示两个
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    arg = {'post_list' : post_list}
    ret = count_art(arg)
    print(ret)
    return render(request, 'home.html', ret)


def get_count_tag(Articles):
    tag_count = {}
    if Articles:
        for art in Articles:
            tag = art.category
            if tag not in tag_count:
                tag_count[tag]=0
            tag_count[tag]+=1
    return tag_count


def get_count_time(Articles):
    time_count = {}
    if Articles:
        for art in Articles:
            tt = art.date_time.strftime('%Y%m')
            if tt not in time_count:
                time_count[tt]=0
            time_count[tt]+=1
    ret = sorted(time_count.items(), key=lambda e: e[0], reverse=True)
    return ret


def count_art(arg):
    ret = {}
    try:
        posts = Article.objects.all()  # 获取全部的Article对象
    except Article.DoesNotExist:
        raise Http404
    tag_count = get_count_tag(posts)
    time_count = get_count_time(posts)
    ret['tag_count'] = tag_count
    ret['time_count'] = time_count
    ret.update(arg)
    return ret


def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    arg = {'post_list' : post_list,'error' : False}
    ret = count_art(arg)
    return render(request, 'archives.html', ret)


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__icontains = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    arg = {'post_list' : post_list}
    ret = count_art(arg)
    return render(request, 'tag.html', ret)


def search_time(request, t_time):
    try:
        post_list = Article.objects.filter(date_time__year=int(t_time[:4]), date_time__month=int(t_time[4:]))
    except Article.DoesNotExist :
        raise Http404
    arg = {'post_list' : post_list}
    ret = count_art(arg)
    return render(request, 'tag.html', ret)


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            ret = count_art({})
            return render(request,'home.html',ret)
        else:
            post_list = Article.objects.filter(Q(title__icontains = s)| Q(content__icontains = s))
            if len(post_list) == 0:
                arg = {'post_list': post_list, 'error': True}

            else:
                arg = {'post_list': post_list, 'error': False}
            ret = count_art(arg)
            return render(request,'archives.html', ret)
    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content