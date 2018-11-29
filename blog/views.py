import markdown
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from comments.forms import CommentForm


def index(request):
  article_list = Article.objects.all().order_by('-created_time')
  return render(request, 'blog/index.html', context={'article_list': article_list})


def detail(request, pk):
  article = get_object_or_404(Article, pk=pk)
  article.increase_views()
  article.body = markdown.markdown(article.body,
                                   extensions=[
                                       'markdown.extensions.extra',
                                       'markdown.extensions.codehilite',
                                       'markdown.extensions.toc',
                                   ])

  form = CommentForm()
  # 获取所有的评论
  comment_list = article.comment_set.all()
  # 将文章，表单，评论列表作为模版变量传给detail.html
  context = {
      'article': article,
      'form': form,
      'comment_list': comment_list,
  }
  return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
  article_list = Article.objects.filter(created_time__year=year,
                                        created_time__month=month,
                                        ).order_by('-created_time')
  return render(request, 'blog/index.html', context={'article_list': article_list})


def category(request, pk):
  cate = get_object_or_404(Category, pk=pk)
  article_list = Article.objects.filter(
      category=cate).order_by('-created_time')
  return render(request, 'blog/index.html', context={'article_list': article_list})
