from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article
from django.core.paginator import Paginator


# Create your views here.
def hello(request):
    return HttpResponse("hello Django")


def articles(request):
    lst = Article.objects.values().all()
    return JsonResponse(list(lst), safe=False)


def index_page(request):
    page = request.GET.get("page", "1")
    page = int(page)
    lst = Article.objects.all()
    top_article_list = Article.objects.order_by("-publish_date")[:5]

    # 分页,每页5个
    paginator = Paginator(lst, 3)
    current_article_list = paginator.get_page(page)

    # 上一页下一页
    if current_article_list.has_next():
        next_page = current_article_list.next_page_number()
    else:
        next_page = page

    if current_article_list.has_previous():
        previous_page = current_article_list.previous_page_number()
    else:
        previous_page = page

    data = {
        "article_list": current_article_list,
        "page_range": paginator.page_range,
        "current_page": page,
        "previous_page": previous_page,
        "next_page": next_page,
        "top_article_list": top_article_list,

    }
    return render(request, "myblog/index.html", data)


def detail_page(request, article_id):
    current_article = Article.objects.get(article_id=article_id)

    # 将文本换行拆分，优化显示
    sections = current_article.content.split("\n")

    # 查询上一页下一页
    previous_article = Article.objects.values(
        "article_id", "title"
    ).filter(
        article_id__lt=current_article.article_id
    ).last()

    next_article = Article.objects.values(
        "article_id", "title"
    ).filter(
        article_id__gt=current_article.article_id
    ).first()

    data = {
        "sections": sections,
        "article": current_article,
        "previous_article": previous_article if previous_article else current_article,
        "next_article": next_article if next_article else current_article

    }
    return render(request, "myblog/detail.html", data)
