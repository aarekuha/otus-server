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

Результаты нагрузочного тестирования
------------------------------------
```bash
$ ab -n 50000 -c 100 -r http://localhost:8080/
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 5000 requests
Completed 10000 requests
Completed 15000 requests
Completed 20000 requests
Completed 25000 requests
Completed 30000 requests
Completed 35000 requests
Completed 40000 requests
Completed 45000 requests
Completed 50000 requests
Finished 50000 requests


Server Software:
Server Hostname:        localhost
Server Port:            8080

Document Path:          /
Document Length:        25 bytes

Concurrency Level:      100
Time taken for tests:   2.773 seconds
Complete requests:      50000
Failed requests:        1
   (Connect: 0, Receive: 1, Length: 0, Exceptions: 0)
Total transferred:      9450000 bytes
HTML transferred:       1250000 bytes
Requests per second:    18031.92 [#/sec] (mean)
Time per request:       5.546 [ms] (mean)
Time per request:       0.055 [ms] (mean, across all concurrent requests)
Transfer rate:          3328.16 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2   4.5      2    1009
Processing:     0    3   0.7      3       8
Waiting:        0    2   0.7      2       7
Total:          0    6   4.6      5    1012

Percentage of the requests served within a certain time (ms)
  50%      5
  66%      6
  75%      7
  80%      7
  90%      7
  95%      7
  98%      8
  99%      8
 100%   1012 (longest request)
```
