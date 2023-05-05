from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import News, Category
from .forms import NewsForm, UserRegisterForm
from django.views.generic import ListView, DetailView, CreateView

from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегались")
            return redirect('login')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'news/registr.html', {"form": form})


def login(request):
    return render(request, 'news/login.html')


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_public=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_public=True)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    raise_exception = True


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, "news/add_news.html", context={"form": form})



# def index(request):
#     news = News.objects.all()
#
#     context = {
#         "news": news,
#         "title": "Список новостей",
#     }
#     return render(request, "news/index.html", context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#
#     context = {
#         "news": news,
#         "category": category
#     }
#
#     return render(request, "news/category.html", context=context)


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         "news_item": news_item
#     }
#     return render(request, "news/view_news.html", context=context)
