# Scraping-Kommersant

Первая версия парсинга газеты kommersant.ru.

url = f'https://www.kommersant.ru/listpage/lazyloaddocs?listtypeid={listtypeid}&listid={category_id}&idafter={idafter}'

Всего около 6 типов (listtypeid), приведены примеры с category_id.
- 1 тип - основные рубрики с id = 2, ..., 9 (rubric/4)
- 2 тип - тема (theme/3423)
- 3 тип - ничего не нашёл
- 4 тип - архив новостей (archive/news)
 - 5 тип - авторы (authors/907)
 - 6 тип - ежедневная газета (daily/139294)
 
 Было выделено 279 основных тэгов. Их точно больше, кому надо - ищите. Они были найдены из основных рубрик 1 типа, брались первые 80-120 записей.
 
 idafter - чтобы была прокрутка вниз указывается последний отображённый id записи, для просмотра вначале указывается пустая строка ('').
 Сначале идут последние вышедшие новости.
 
