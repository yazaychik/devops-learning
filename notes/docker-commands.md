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

## Управление контейнером
docker stop NAME        — остановить контейнер
docker start NAME       — запустить остановленный
docker logs NAME        — посмотреть логи
docker exec -it NAME bash  — зайти внутрь контейнера
docker rm NAME          — удалить контейнер (должен быть остановлен)
docker rmi IMAGE        — удалить образ

## Свои образы
docker build -t NAME .     — собрать образ из Dockerfile
docker images              — посмотреть все образы
test
