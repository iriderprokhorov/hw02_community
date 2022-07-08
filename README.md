# Yatube. Continue project  
## Описание изменений
- Создано и зарегистрировано приложение Posts.
- Подключена база данных.
- Десять последних записей выводятся на главную страницу.
- В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие.
- Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.
- Админка (admin.py)
Зарегистрирована модель Group.
Для модели Post создана кастомная админка:
В списке объектов в админке отображаются поля pk, text, pub_date, author, group.
Содержимое поля group можно редактировать в админке прямо в списке объектов Post.
Доступен поиск по полю text.
Доступна фильтрация по полю pub_date.
Если какое-то поле не заполнено, в нём отображается текст -пусто-.
- View-функции (views.py)
index(): передаёт в шаблон posts/index.html десять последних объектов модели Post.
group_posts(): передаёт в шаблон posts/group_list.html десять последних объектов модели Post, отфильтрованных по полю group, и содержимое для тега <title>.
- Адреса (urls.py)
Для приложения Posts установлен namespace='posts'.
Для главной страницы установлен name='index'.
Страница с постами из определённой группы доступна по URL вида group/<slug>/.
Для страницы с постами группы установлен name='group_list'.
- Шаблоны
Файлы шаблонов хранятся на уровне проекта.
Шаблоны разбиты на логические блоки и собираются с помощью тегов include и extend.
К шаблонам подключена статика.
Шаблоны соответствуют дизайну:
web_hw02_community_with_text.zip
В шаблоне index.html ссылка <a href="">все записи группы</a> адресует пользователя на страницу той группы, которой принадлежит пост.
Из view-функций в словаре context передаётся основное содержимое страницы.
Содержимое тега <title> — для разных страниц разное:
для страницы группы: Записи сообщества <имя_группы>;
для главной страницы: Последние обновления на сайте.

## Системные требования
 Python3 

## Установка
1.clone project
2.install venv
3.install requirements
4.make migrations
5.python3 manage3 runserver

Just open browser and type 127.0.0.1:8000


## Docker

In the future

## License

MIT

**Free Software, Hell Yeah!**


