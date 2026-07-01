# Docker команды

## Основные
docker run IMAGE        — запустить контейнер
docker ps               — запущенные контейнеры
docker ps -a            — все контейнеры
docker images           — скачанные образы
docker stop NAME        — остановить контейнер
docker rm NAME          — удалить контейнер

## Флаги docker run
-d        запустить в фоне
-p 80:80  пробросить порт (хост:контейнер)
--name    задать имя контейнера
