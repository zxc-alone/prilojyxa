# prilojyxa
В данном проекте реализован сайт похожий на ленту новостей с помощью фреймворка Django
## Созданно приложение rereww в котором описана вся работа приложения
### requirements.txt отвечает за все зависимости проекта 
### Также в проекте использовалось виртуальное окружение venv 
### static отвечает за css и img на сайтах сами сайты хранятся в папке templates
# В проекте реальзована также админская зона 
с помощью которой можно управлять постами, группами и пользователями 
# В проект таже подключена база данных SQL
В ней хранятся данные о постах и группах




# Как создавался проект 
С помощью следующих ссылок:
### Урок 6: Создание проекта https://colab.research.google.com/drive/1aV4XXFqCcpyaOAC9tgVtcLsYsc1adarc?usp=sharing
### Урок 7: urls и veiws.py https://colab.research.google.com/drive/1w1Naanzi1JJKWk8-PetZtVpqgi2Pg8S5?usp=sharing
### Урок 8: Верстка и фреймворк Bootstrap https://colab.research.google.com/drive/1HYN_wVf8UWy4SqHKtTXrPwH7S_-oENjg?usp=sharing
### Урок 9: Шаблоны и теги в Django https://colab.research.google.com/drive/18kfIeLm9LY4hidLL-qnJRUu0UHRvuVAW?usp=sharing
### Урок 10: База данных и Django ORM https://colab.research.google.com/drive/1IlL82klbMhq6_vZlBTr51_Z_iVAOKyLv?usp=sharing
Также использовались нейросети Deep Seek и Gimini

#### В 6 уроке мы создали репозиторий на github настроили виртуальное окружение скачали питон, джанго в это окружение создали первое приложение, сделали первый запуск и первый коммит.
#### В 7 уроке мы настроили файл с адресами urls.py разобрались как с ним работать, Настроили файл veiws.py добавив в него некоторые функции.
#### В 8 уроке мы разобрались как сделать наш сайт более привлекательным добавив в него css, чтобы он работал не только локально но еще и на сервере, также в этом уроке мы создали папку static в которой будет хранится вся информация о стилях и все изображения.
#### В 9 уроке мы подключили CSS в Django. Load static для загрузки всех стилей и изображений на сайтах. Настроили файл veiws.py добавив в него некоторые функции и изменив старые.
#### В 10 уроке мы создали сайт для администратора, подключили к проекту базу данных с тестовыми заданиями.




# Памятка по ОRM(базы данных)
Переводчик с Python на SQL
Для работы с базами данных в моделях Django есть встроенный набор методов. Они наследуются от класса models.Model и поддерживают основные операции по обработке данных в БД: CRUD. Вы знакомы с этой аббревиатурой из урока по SQL

CRUD-операции
Create: Model.objects.create() — создание объекта в базе
Read: Model.objects.get(id=N) — чтение объекта по его ключу
Update: object.property= 'new value' и потом object.save() — изменение объекта
Delete: object.delete() — удаление объекта из базы
Сейчас мы разберёмся с основными задачами, которые решает Django ORM. Но перед этим познакомимся с инструментом, который упростит нам тестирование кода.

Python shell
С интерпретатором кода Python, как и со многими другими программами, можно работать через командную строку. Если в консоли выполнить команду $python3 без параметров, то интерпретатор Python запустится в «интерактивном режиме». Теперь можно ввести в командную строку любые скрипты python — и они будут выполняться прямо в терминале. Это похоже на работу командной строки, но вместо команд для работы с файлами выполняется программный код, строчка за строчкой.

Откройте новое окно терминала и посмотрите, как работает python shell.

Символы >>> — это приглашение для ввода команд, то же, что и знак $ в командной строке.

# запускаем интерпретатор без параметров
$ python3
 дальше пишем на python
 создаём переменную
> best_slogan = "Mischief Managed!"
 вызываем функцию print()
> print(best_slogan)
# и получаем результат
Mischief Managed!
# арифметика тоже работает
> 2 + 2 * 2
6
Прелесть этого режима в том, что он тут же выводит результат выполнения скрипта. Например, создадим и выведем переменную:

> x = 5
> x
5
Обратите внимание: переменные, которые вы создали во время работы в python shell, будут доступны до тех пор, пока вы не закроете окно терминала.

Django Python shell
В таком же интерактивном режиме можно работать и с Django-проектами. Для этого python shell надо запустить в виртуальном окружении проекта.

Откройте терминал, убедитесь, что запущено виртуальное окружение проекта Yatube, и выполните команду:

(venv) $ python manage.py shell
Вы увидите примерно такой результат:

(venv) $ python manage.py shell
Python 3.8.0 (default, Nov 22 2019, 23:37:58)
[Clang 11.0.0 (clang-1100.0.33.12)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
Всё, что вы хотите узнать, но стесняетесь спросить — выясняйте через команду help.

При работе в интерактивном режиме в Django вам становятся доступны все данные проекта. Можно создавать объекты, управлять базой данных, тестировать функции проекта.

(venv) $ python manage.py shell
Python 3.8.0 (default, Nov 22 2019, 23:37:58)
[Clang 11.0.0 (clang-1100.0.33.12)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
 чтобы убедиться, что мы работаем именно с нашим проектом Yatube
 импортируем модели из проекта и заглянем в базу данных:
 запросим все объекты модели Post
> from posts.models import Post, User
> Post.objects.all()
Основы работы с shell разобрали, теперь можно и делами заняться. Все следующие команды выполняйте в shell.

Работаем с проектом
Запрос к базе возвращает специальный объект QuerySet, который содержит список объектов, соответствующих условиям запроса. По запросу .all() мы получили все объекты модели Post.

Чтобы получить определённый объект, можно обратиться к нему по его primary key:

 можно использовать User.objects.get(id=1)
> me = User.objects.get(pk=1)
> me
 python shell сообщает, что переменная me содержит <Объект> класса User,
 а поле username этого объекта равно "admin"
<User: admin>
Класс User предустановлен в Django, и для него настроен вывод на экран именно в таком виде. При создании любого класса можно описать, каким образом объекты этого класса будут выводиться на экран (например, в python shell или при вызове print(any_object)). Это описывается в «магическом методе» __str__.

Запросим пользователя с pk=13: у нас в базе такой записи пока что нет. Если объект с запрошенным ключом не найден, то появится сообщение об ошибке:

> User.objects.get(pk=13)
Traceback (most recent call last):
    File "<console>", line 1, in <module>
    File "/Dev/Yatube/venv/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
        return getattr(self.get_queryset(), name)(*args, **kwargs)
    File "/Dev/Yatube/venv/lib/python3.8/site-packages/django/db/models/query.py", line 415, in get
        raise self.model.DoesNotExist(
django.contrib.auth.models.User.DoesNotExist: User matching query does not exist.
Новый объект в базе можно создать методом create():

 создаём объект, передаём свойства
> new = Post.objects.create(author=me, text="Смотри, этот пост я создал через shell!")
 посмотрим, какой id присвоен этому объекту в базе
> new.id
39
 а что в поле text?
> new.text
"Смотри, этот пост создан через shell!"
 а что в поле author?
> new.author
<User: admin>
# смотрим, что записано в поле username того объекта, на который ссылается поле author
>>> new.author.username
'admin'
Объект new в момент создания сохранился в базе и получил уникальный id.

Чтобы изменить этот объект, надо присвоить новое значение одному из его полей и вызвать метод save():

 присваиваем новое значение полю text
> new.text = "Смотри, этот пост обновлён!"
но пока что значение изменено лишь в коде. В БД всё ещё хранится старое значение
чтобы отправить новое значение в базу данных — вызываем метод save()
> new.save()
Если вы изменили объект в коде — он не изменится в базе до тех пор, пока вы не вызовете метод save().

Теперь обновлённый текст записи можно увидеть в админ-зоне.

Удалить объект из базы можно методом delete(). При вызове этот метод дополнительно удалит и все связанные объекты, для которых был задан параметр on_delete=models.CASCADE.

> new.delete()
Для дальнейшей работы нам понадобятся тестовые посты админа, создайте их:

> first_post = Post.objects.create(author=me, text="Oops, I did it again!")
> second_post = Post.objects.create(author=me, text="Утромъ гольдъ Дерсу Узала на повторно заданный вопросъ согласенъ ли онъ поступить проводникомъ изъявилъ свое согласіе и съ этого момента онъ сталъ членом экспедиціи")
Фильтрация объектов
Основная задача при работе с базой — это поиск объектов по заданным признакам. В SQL за это отвечают команды блока WHERE, в Django ORM — метод filter():

 найти все объекты, значение поля author у которых равно me
 в этой переменной хранится объект User с pk=1
> Post.objects.filter(author=me)
<QuerySet [<Post: Oops, I did it again!>, <Post: Утромъ гольдъ Дерсу Узала...>]>
В базе найдены две записи, соответствующие условиям запроса.

Если ваш вывод выглядит так <QuerySet [<Post: Post object(39)>, <Post: Post object(40)>] значит в классе Post не хватает метода __str__ , который нужен для красивого вывода объектов на экран. Добавьте его:

class Post:
    ...
    def __str__(self):
        # выводим текст поста
        return self.text
Увидеть SQL-запрос, который будет отправлен к базе, можно с помощью команды .query:

> print(Post.objects.filter(author=me).query)
SELECT "posts_post"."id", "posts_post"."text", "posts_post"."pub_date",
"posts_post"."author_id", "posts_post"."group_id" FROM "posts_post" WHERE
"posts_post"."author_id" = 1
В Django ORM аналог команд WHERE выглядит так: указывается имя поля, затем два знака подчеркивания __, название фильтра и его значение:

 найти посты, где поле text__содержит строку "again"
> Post.objects.filter(text__contains='again')
<QuerySet [<Post: Oops, I did it again!>]>
При запросе указываются именованные параметры функции filter(). Имя параметра состоит из имени поля и суффикса, указывающего, какой оператор применять. Доступные операторы:

exact — точное совпадение. «Найти пост, где поле id точно равно 1»

ORM: Post.objects.filter(id__exact=1) или Post.objects.filter(id=1)

На SQL это условие выглядит так: SELECT ... WHERE id = 1.

Сравнение работает и с None. Выражение Post.objects.filter(text=None) превратится в SELECT ... WHERE text IS NULL

contains — поиск по тексту в поле text. «Найти пост, где в поле text есть слово "oops" именно в таком регистре»

ORM: Post.objects.filter(text__contains='oops')

SQL: SELECT ... WHERE text LIKE '%oops%';

В большинстве баз данных (например, в MySQL или PostgreSQL) ничего не найдётся: регистр символов не совпадает. В посте админа написано "Oops", а в запросе — "oops".

Однако в нашем проекте установлена СУБД SQLite (Django ставит её по умолчанию), и у неё есть неприятная особенность: она не различает регистр символов нигде, кроме как в кодировке ASCII (а мы все давно уже работаем в UTF-8, ведь в ней есть смайлики 😃).

Мануалы формулируют проблему так: SQLite only understands upper/lower case for ASCII characters by default.

in — вхождение в множество. «Найти пост, где значение поля id точно равно одному из значений: 1, 3 или 4»

ORM: Post.objects.filter(id__in=[1, 3, 4])

SQL: SELECT ... WHERE id IN (1, 3, 4);

Если вместо списка будет передана строка, она разобьётся на символы: «Найти пост, где значение поля text точно равно "o", "p" или "s"»

ORM: Post.objects.filter(text__in='oops')

SQL: SELECT ... WHERE text IN ('o', 'p', 's');

Операторы сравнения

gt — > (больше),

gte — >= (больше или равно),

lt — < (меньше),

lte — <= (меньше или равно).

«Найти пост, где значение поля id больше пяти»

ORM: Post.objects.filter(id__gt=5)

SQL: SELECT ... WHERE id>5;

Операторы сравнения с началом и концом строки startswith, endswith

«Найти посты, где содержимое поля text начинается со строки "Утромъ"»

ORM: Post.objects.filter(text__startswith="Утромъ")

SQL: SELECT ... WHERE text LIKE Утромъ% ESCAPE

range — вхождение в диапазон

import datetime
start_date = datetime.date(1890, 1, 1)
end_date = datetime.date(1895, 3, 31)
Post.objects.filter(pub_date__range=(start_date, end_date))
 SQL: SELECT ... WHERE pub_date BETWEEN '1890-01-01' and '1895-03-31';
 выберет посты, опубликованные в диапазоне с 1 января 1890 до 31 марта 1895
При работе с частями дат можно применять дополнительные суффиксы date, year, month, day, week, week_day, quarter и указывать для них дополнительные условия:
 условия для конкретной даты
Post.objects.filter(pub_date__date=datetime.date(1890, 1, 1))
Post.objects.filter(pub_date__date__lt=datetime.date(1895, 1, 1))
 условия для года и месяца
Post.objects.filter(pub_date__year=1890)
Post.objects.filter(pub_date__month__gte=6)
 условия для квартала
Post.objects.filter(pub_date__quarter=1)
Такой же синтаксис применяется и для времени: hour, minute, second.

isnull — проверка на пустое значение.

ORM: Post.objects.filter(pub_date__isnull=True)

SQL: SELECT ... WHERE pub_date IS NULL;

Объединение условий
В одном запросе можно указать несколько условий одновременно. Для этого последовательно вызовите методы filter() с различными параметрами. Будет сгенерирован SQL-запрос, в котором все условия объединены оператором AND.

Исключить данные из выборки можно методом exclude():

 выбрать посты, начинающиеся со слова "Утромъ"
 исключить из выборки посты автора me
 и показать только те посты, которые опубликованы не ранее 30 января 1895 года
> Post.objects.filter(
...     text__startswith='Утромъ'
... ).exclude(
...     author=me
... ).filter(
...     pub_date__gte=datetime.date(1895, 1, 30)
... )
Сортировка и ограничение количества результатов
Этот синтаксис вам знаком: мы применяли сортировку во view-функции index() и там же ограничили число возвращаемых результатов запроса.

order_by('-pub_date') — сортировать результаты по полю pub_date в обратном порядке (от больших значений к меньшим)

[:11] — вернуть не более одиннадцати результатов из найденных.

> print(Post.objects.order_by('-pub_date')[:11].query)
SELECT "posts_post"."id", "posts_post"."text", "posts_post"."pub_date",
"posts_post"."author_id", "posts_post"."group_id" FROM "posts_post" ORDER
BY "posts_post"."pub_date" DESC LIMIT 11
Сортировку и ограничение числа возвращаемых результатов можно объединить с фильтрацией:

> Post.objects.filter(text__startswith='Утромъ').order_by('-pub_date')[:2]
В Django ORM есть и дополнительный синтаксис, он описан в документации.