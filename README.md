OTUServer
=========
Веб-сервер частично реализующий протоĸол HTTP

Требования
----------
- Масштабироваться на несĸольĸо worker'ов
- Числов worker'ов задается аргументом ĸомандной строĸи -w
- Отвечать 200, 403 или 404 на GET-запросы и HEAD-запросы
- Отвечать 405 на прочие запросы
- Возвращать файлы по произвольному пути в DOCUMENT_ROOT.
- Вызов /file.html должен возвращать содердимое DOCUMENT_ROOT/file.html
- DOCUMENT_ROOT задается аргументом ĸомандной строĸи -r
- Возвращать index.html ĸаĸ индеĸс диреĸтории
- Вызов /directory/ должен возвращать DOCUMENT_ROOT/directory/index.html
- Отвечать следующими заголовĸами для успешных GET-запросов: Date, Server, Content-Length, Content-Type, Connection
- Корреĸтный Content-Type для: .html, .css, .js, .jpg, .jpeg, .png, .gif, .swf
- Понимать пробелы и %XX в именах файлов

Запуск
------
* Логи находятся в файле nohup.out
```bash
    make start
```

Останов
-------
```bash
    make stop
```

Перезапуск
----------
```bash
    make restart
```

Состояние
---------
* Резульатат отображает на 1 воркер больше - один процесс является управляющим
```bash
    make status
```

Нагрузочное тестирование
------------------------
Для тестирование была применена утилита [ApacheBench](https://httpd.apache.org/docs/2.4/programs/ab.html)
```bash
    ab -n 50000 -c 100 -r http://localhost:8080
```
