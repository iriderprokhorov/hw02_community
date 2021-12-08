from django.shortcuts import render, get_object_or_404

# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by("-pub_date")[:10]
    title = "Последние обновления на сайте"
    # В словаре context отправляем информацию в шаблон
    context = {
        "posts": posts,
        "title": title,
    }
    return render(request, "posts/index.html", context)


# View-функция для страницы сообщества:
def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает ошибк, если объект не найден.
    # В нашем случае в group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:10]
    title = "Записи сообщества"
    context = {
        "group": group,
        "posts": posts,
        "title": title,
    }
    return render(request, "posts/group_list.html", context)
