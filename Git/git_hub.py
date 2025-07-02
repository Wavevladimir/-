git clone <url> клонирование удаленного репозитория в локальный 
origin - имя удаленного репозитория по-умолчанию 
git branch -a отображает все ветки, включая те, которые находятся в удаленных репозиториях 
git checkout <branch name> переход в любую ветку в том чесле и ветку удаленного репозитория
git pull загрузка и применение изменений с удаленной ветки в локальную
git push загрузка изменений из локальной ветки в ветку удаленного репозитория 

1) git remote add origin <url> подключение удаленного репозитория 
2) git push -u origin <branch> загрузка изменений из локальной ветки в удаленную с 
созданием связи между ними
3)git push дальнейшая загрузка изменений в ветку удаленного репозитория после установки связи 
между локальной и удаленной ветками
3)git pull скачать обновления с определенной ветки с удаленного репозитория 


гит клон
wavevladimir@MacBook-Air-Vladimir Desktop % git clone https://github.com/bstashchuk/docker.git
Cloning into 'docker'...
remote: Enumerating objects: 540, done.
remote: Counting objects: 100% (88/88), done.
remote: Compressing objects: 100% (65/65), done.
remote: Total 540 (delta 20), reused 82 (delta 18), pack-reused 452 (from 1)
Receiving objects: 100% (540/540), 1.04 MiB | 1.95 MiB/s, done.
Resolving deltas: 100% (113/113), done.
wavevladimir@MacBook-Air-Vladimir Desktop % cd docker
wavevladimir@MacBook-Air-Vladimir docker % git branch 
* master
wavevladimir@MacBook-Air-Vladimir docker % ls
README.md	containers	images-gallery
wavevladimir@MacBook-Air-Vladimir docker % code .
wavevladimir@MacBook-Air-Vladimir docker % git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
wavevladimir@MacBook-Air-Vladimir docker % git remote -v
origin	https://github.com/bstashchuk/docker.git (fetch)
origin	https://github.com/bstashchuk/docker.git (push)
wavevladimir@MacBook-Air-Vladimir docker %  
