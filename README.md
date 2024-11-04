# Тестовое задание для компании "Звонок"

## Вопрос 1

**Вопрос:**

Есть веб-сервис А, принимающий запросы от пользователей, запросов может приходить в час 200 000.
В день приходит до 2 000 000 запросов. Сервис А должен отправить эти данные в сервис Б, чтоб обработать данные. 
Сервис Б может обработать 100 000 запросов в час. Запросы от пользователей поступающий в сервис А нельзя потерять.
Как бы вы организовали межсервисное взаимодействие, хранение данных, результатов, какие инструменты  использовали бы для этого?

**Ответ:**

1. Поскольку сервис Б обрабатывает данные медленнее, чем это делает сервис А, необходимо предусмотреть прослойку
между сервисами в виде очереди (RabbitMQ, Kafka). Сервис А будет класть задачи в очередь, сервис Б будет их обрабатывать.
Во избежание потери данных в очереди можно так же продумать механизм репликации и распределения потоков данных.
2. Предусмотреть механизм масштабирования сервиса Б (напр. репликация), чтобы при росте нагрузки на сервис А увеличивалось
кол-во экземпляров сервиса Б.

## Вопрос 2

**Вопрос:**

Даны две таблицы в PostgresSQL - таблица статей и таблица комментариев к этим статьям 

Необходимо написать запрос, который выведет все статьи без комментариев (у которых нет комментариев)

Таблицы тут: http://sqlfiddle.com/#!17/84c62 (Или тут https://www.db-fiddle.com/f/kGzmoWLCRkQ9mzHM83u2vT/0)

```sql
CREATE TABLE article (
    id        integer CONSTRAINT articlekey PRIMARY KEY,
    title       varchar(255) NOT NULL,
    text         text NOT NULL
);


CREATE TABLE comment (
    id        integer CONSTRAINT commentkey PRIMARY KEY,
    article_id integer NOT NULL,
    text         text NOT NULL
);


INSERT INTO article (id, title, text) VALUES (1, 'Phasellus gravida eu ante et imperdiet', 'Mauris rutrum augue risus, sodales maximus neque vulputate a. Curabitur porttitor, risus eu fermentum hendrerit, urna est dictum est, quis condimentum lectus nisi eget diam.');
INSERT INTO article (id, title, text) VALUES (2, 'Maecenas egestas fermentum rutrum', 'Vivamus varius nibh et iaculis mollis. Phasellus eu massa a libero eleifend scelerisque. Nulla molestie justo libero, ac aliquet mi iaculis eget.');
INSERT INTO article (id, title, text) VALUES (3, 'Nam vestibulum dignissim volutpat', 'Praesent neque lectus, porttitor et nunc vitae, congue semper felis. Pellentesque convallis facilisis odio id fringilla. Vivamus quis nibh felis.');
INSERT INTO article (id, title, text) VALUES (4, 'Phasellus augue ipsum, rutrum a imperdiet', 'Praesent in turpis ac nisl pellentesque volutpat. Maecenas vitae viverra ipsum. Proin accumsan diam vitae nulla tincidunt, a mollis diam luctus.');
INSERT INTO article (id, title, text) VALUES (5, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit', 'Integer eget urna porttitor, dictum quam quis, cursus tellus. Pellentesque dictum accumsan mauris a pulvinar.');

INSERT INTO comment (id, article_id, text) VALUES (1, 1, 'Nunc ac arcu non lectus bibendum mattis. Suspendisse suscipit, enim sit amet ultrices laoreet, dolor dui rhoncus quam');
INSERT INTO comment (id, article_id, text) VALUES (2, 1, 'Aenean cursus a sapien ac malesuada');
INSERT INTO comment (id, article_id, text) VALUES (3, 1, 'Fusce sit amet lacus dignissim, tempus massa sed, ultricies dolor');
INSERT INTO comment (id, article_id, text) VALUES (4, 4, 'Phasellus non urna commodo, finibus lectus ac, gravida lectus');
INSERT INTO comment (id, article_id, text) VALUES (5, 4, 'Suspendisse pretium porttitor iaculis. Nulla in tortor vel est lobortis fermentum');
INSERT INTO comment (id, article_id, text) VALUES (6, 4, 'Etiam gravida vehicula massa non condimentum');
INSERT INTO comment (id, article_id, text) VALUES (7, 4, 'Etiam rutrum purus a ipsum viverra laoreet. Nunc aliquet ex vitae tincidunt luctus');
INSERT INTO comment (id, article_id, text) VALUES (8, 4, 'Sed facilisis fermentum lacus, non semper est sodales sed.');
INSERT INTO comment (id, article_id, text) VALUES (9, 5, 'Integer vitae ipsum auctor, interdum leo eu, facilisis dui. Suspendisse ut feugiat dolor, in ultrices leo');
```

**Ответ:** 

```sql
SELECT article.id,
	   article.title,
       article.text
FROM article 
LEFT JOIN comment ON comment.article_id = article.id 
WHERE comment.article_id IS NULL;
```

## Вопрос 3

**Вопрос:** 

На входе есть такие записи выполненных часов работниками
(по дням, дни можно опустить - они не имеют значения):

```
Андрей 9
Василий 11
Роман 7
X Æ A-12 45
Иван Петров 3
..
Андрей 6
Роман 11
...
```

Формат - имя, пробел, число.
Если имя повторяется, то это один и тот же работник. <b>Имя может содержать пробелы и цифры.</b>

Необходимо написать программу на python, которая выводит статистику по каждому работнику + сумму часов, например:

```
Андрей: 9, 6; sum: 15
Василий: 11; sum: 11
Роман: 7, 11: sum: 18
...
```

**Ответ:** 
Ответ приведён в файле `main.py`
Тесты для функции парсинга приведены в файле `test_main.py`

Для запуска парсера необходимо выполнить команду:
```shell
python main.py
```

Для запуска тестов необходимо выполнить команду:
```shell
python -m unittest test_main.py
```
