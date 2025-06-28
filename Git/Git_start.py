git config --global user.name "Wavevladimir"
git config --list
git config --global user.email vikirov43@mail.ru 

git init создание нового git репозитория
git branch -m <new branch name> изменить название текущей ветки
git checkout <branch name> переход в другую ветку
git checkout -b <branch name> создание новой ветки и переход в нее 
git branch отображает список всех веток
git branch -d <branch name> удаление ветки(текущую ветку удалить нельзя)
ls -la вводим данную команду в папке в которой инициализировали гит репозиторий и 
видим скрытую папуц гит
cd .git переходим в эту папку

git status отображает текущее состояние гит репозитория
git add подготовка файлов перед коммитомм 
git commit -m '<message>' создание коммита с записью изменений в репозиторий
git log просмотр истории изменений (коммитов) будут показаны хэши и 
узнав этот хэш можно переместиться по версиям
git checkout <commit hash> переход в определенную версию проекта по SHA1 хэшу коммита
git chekout <branch name> переход в определенную версию проекта по названию ветки


wavevladimir@MacBook-Air-Vladimir Desktop % cd my-project 
wavevladimir@MacBook-Air-Vladimir my-project % git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
wavevladimir@MacBook-Air-Vladimir my-project % cleat
zsh: command not found: cleat
wavevladimir@MacBook-Air-Vladimir my-project % clear

wavevladimir@MacBook-Air-Vladimir my-project % echo "First file text" > first-file.txt
wavevladimir@MacBook-Air-Vladimir my-project % ls
first-file.txt
wavevladimir@MacBook-Air-Vladimir my-project % cat first-file.txt 
First file text
wavevladimir@MacBook-Air-Vladimir my-project % git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	first-file.txt

nothing added to commit but untracked files present (use "git add" to track)
wavevladimir@MacBook-Air-Vladimir my-project % mkdir first-subfolder
wavevladimir@MacBook-Air-Vladimir my-project % cd first-subfolder 
wavevladimir@MacBook-Air-Vladimir first-subfolder % ls
wavevladimir@MacBook-Air-Vladimir first-subfolder % echo "Second file text" > second-file.txt
wavevladimir@MacBook-Air-Vladimir first-subfolder % echo "Third file text" > third-file.txt
wavevladimir@MacBook-Air-Vladimir first-subfolder % ls
second-file.txt	third-file.txt
wavevladimir@MacBook-Air-Vladimir first-subfolder % cat second-file.txt 
Second file text
wavevladimir@MacBook-Air-Vladimir first-subfolder % cat third-file.txt 
Third file text
wavevladimir@MacBook-Air-Vladimir first-subfolder % cd ..
wavevladimir@MacBook-Air-Vladimir my-project % ls
first-file.txt	first-subfolder
wavevladimir@MacBook-Air-Vladimir my-project % git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	first-file.txt
	first-subfolder/

nothing added to commit but untracked files present (use "git add" to track)
wavevladimir@MacBook-Air-Vladimir my-project % git add first-file.txt 
wavevladimir@MacBook-Air-Vladimir my-project % git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   first-file.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	first-subfolder/

wavevladimir@MacBook-Air-Vladimir my-project % git add . 
wavevladimir@MacBook-Air-Vladimir my-project % git status 
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   first-file.txt
	new file:   first-subfolder/second-file.txt
	new file:   first-subfolder/third-file.txt

wavevladimir@MacBook-Air-Vladimir my-project % git log 
fatal: your current branch 'main' does not have any commits yet
wavevladimir@MacBook-Air-Vladimir my-project % git commit -m "First commit" 
[main (root-commit) a537d89] First commit
 3 files changed, 3 insertions(+)
 create mode 100644 first-file.txt
 create mode 100644 first-subfolder/second-file.txt
 create mode 100644 first-subfolder/third-file.txt
wavevladimir@MacBook-Air-Vladimir my-project % git status 
On branch main
nothing to commit, working tree clean
wavevladimir@MacBook-Air-Vladimir my-project % git log 
commit a537d89b626484d3bab80d62493021e85d5df205 (HEAD -> main)
Author: Wavevladimir <vikirov43@mail.ru>
Date:   Thu Jun 26 22:25:33 2025 +0300

    First commit
wavevladimir@MacBook-Air-Vladimir my-project % q
zsh: command not found: q
wavevladimir@MacBook-Air-Vladimir my-project % cd .git
wavevladimir@MacBook-Air-Vladimir .git % ls
COMMIT_EDITMSG	config		hooks		info		objects
HEAD		description	index		logs		refs
wavevladimir@MacBook-Air-Vladimir .git % cd objects 
wavevladimir@MacBook-Air-Vladimir objects % ls
32	4b	79	a5	ac	ea	info	pack
wavevladimir@MacBook-Air-Vladimir objects % git log
commit a537d89b626484d3bab80d62493021e85d5df205 (HEAD -> main)
Author: Wavevladimir <vikirov43@mail.ru>
Date:   Thu Jun 26 22:25:33 2025 +0300

    First commit
wavevladimir@MacBook-Air-Vladimir objects % cd a5
wavevladimir@MacBook-Air-Vladimir a5 % ls
37d89b626484d3bab80d62493021e85d5df205
wavevladimir@MacBook-Air-Vladimir a5 % git cat-file -t a537d89b
commit
wavevladimir@MacBook-Air-Vladimir a5 % git cat-file -p a537d89b
tree 79e275c048fa5542470727cb2e18124a882126ae
author Wavevladimir <vikirov43@mail.ru> 1750965933 +0300
committer Wavevladimir <vikirov43@mail.ru> 1750965933 +0300

First commit
wavevladimir@MacBook-Air-Vladimir a5 % git cat-file -t 79e275
tree
wavevladimir@MacBook-Air-Vladimir a5 % git cat-file -p 79e275
100644 blob ac54b20c20ff83adb2de7931356bf8b207cbe555	first-file.txt
040000 tree 32ef472c6b7a64d9f397090249af49dc12c896e2	first-subfolder
wavevladimir@MacBook-Air-Vladimir a5 % git cat-file -t ac54b20c
blob
wavevladimir@MacBook-Air-Vladimir a5 % git cat-file -p ac54b20c
First file text
wavevladimir@MacBook-Air-Vladimir a5 %  
wavevladimir@MacBook-Air-Vladimir my-project % rm first-file.txt
wavevladimir@MacBook-Air-Vladimir my-project % git status
On branch main
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    first-file.txt

no changes added to commit (use "git add" and/or "git commit -a")
wavevladimir@MacBook-Air-Vladimir my-project % mkdir second-subfolder
wavevladimir@MacBook-Air-Vladimir my-project % cd second-subfolder 
wavevladimir@MacBook-Air-Vladimir second-subfolder % echo "Fourth file text" > fourth-file.txt
wavevladimir@MacBook-Air-Vladimir second-subfolder % echo "Fifth file text" > fifth-file.txt 

wavevladimir@MacBook-Air-Vladimir second-subfolder % ls
fifth-file.txt	fourth-file.txt
wavevladimir@MacBook-Air-Vladimir second-subfolder % cd ..
wavevladimir@MacBook-Air-Vladimir my-project % ls
first-subfolder		second-subfolder
wavevladimir@MacBook-Air-Vladimir my-project % git status 
On branch main
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    first-file.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	second-subfolder/

no changes added to commit (use "git add" and/or "git commit -a")
wavevladimir@MacBook-Air-Vladimir my-project % git add .
wavevladimir@MacBook-Air-Vladimir my-project % git status      
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	deleted:    first-file.txt
	new file:   second-subfolder/fifth-file.txt
	new file:   second-subfolder/fourth-file.txt

wavevladimir@MacBook-Air-Vladimir my-project % git commit -m "Second commit"
[main bb303b8] Second commit
 3 files changed, 2 insertions(+), 1 deletion(-)
 delete mode 100644 first-file.txt
 create mode 100644 second-subfolder/fifth-file.txt
 create mode 100644 second-subfolder/fourth-file.txt
wavevladimir@MacBook-Air-Vladimir my-project % git status 
On branch main
nothing to commit, working tree clean
wavevladimir@MacBook-Air-Vladimir my-project % git log 
commit bb303b80052e7e3265da94836061f87b19236be0 (HEAD -> main)
Author: Wavevladimir <vikirov43@mail.ru>
Date:   Thu Jun 26 22:48:47 2025 +0300

    Second commit

commit a537d89b626484d3bab80d62493021e85d5df205
Author: Wavevladimir <vikirov43@mail.ru>
Date:   Thu Jun 26 22:25:33 2025 +0300

    First commit
wavevladimir@MacBook-Air-Vladimir my-project % git cat-file -t bb303b
commit
wavevladimir@MacBook-Air-Vladimir my-project % git cat-file -p bb303b
tree b1507ffa1116c1429aa451251508e7b09b206dae
parent a537d89b626484d3bab80d62493021e85d5df205
author Wavevladimir <vikirov43@mail.ru> 1750967327 +0300
committer Wavevladimir <vikirov43@mail.ru> 1750967327 +0300

Second commit
wavevladimir@MacBook-Air-Vladimir my-project % git cat-file -t b1507ff
tree
wavevladimir@MacBook-Air-Vladimir my-project % git cat-file -p b1507ff
040000 tree 32ef472c6b7a64d9f397090249af49dc12c896e2	first-subfolder
040000 tree 71234083c8cc74e9af46b881fa501869e8f53519	second-subfolder
wavevladimir@MacBook-Air-Vladimir my-project % git cat-file -t 32ef472c
tree
wavevladimir@MacBook-Air-Vladimir my-project % git cat-file -p 32ef472c
100644 blob ea7580a93773575984ae3dfdfa18994d81995e30	second-file.txt
100644 blob 4b4649dfa122e05de36f523e85347e6c2d416e32	third-file.txt
wavevladimir@MacBook-Air-Vladimir my-project % git cat-file -p 4b4649d
Third file text
wavevladimir@MacBook-Air-Vladimir my-project % git cat-file -p ea7580a9
Second file text
wavevladimir@MacBook-Air-Vladimir my-project % git cat-file -p 712340
100644 blob 564f99320b1d637f6f1e1ca705a579b5287d0065	fifth-file.txt
100644 blob 1e07c319b119f4403aaaf83b0b2f24b79cab4d8f	fourth-file.txt
wavevladimir@MacBook-Air-Vladimir my-project % cd ../.. 
wavevladimir@MacBook-Air-Vladimir ~ % ls
Applications	Downloads	Pictures	Python		teacherpython
DJANGO		Library		Postman		README.md
Desktop		Movies		Public		git
Documents	Music		PycharmProjects	git-course
wavevladimir@MacBook-Air-Vladimir ~ % cd Desktop 
wavevladimir@MacBook-Air-Vladimir Desktop % cd my-project 
wavevladimir@MacBook-Air-Vladimir my-project % ls
first-subfolder		second-subfolder
wavevladimir@MacBook-Air-Vladimir my-project % git status
On branch main
nothing to commit, working tree clean
wavevladimir@MacBook-Air-Vladimir my-project % 
wavevladimir@MacBook-Air-Vladimir my-project % git log
commit bb303b80052e7e3265da94836061f87b19236be0 (HEAD -> main)
Author: Wavevladimir <vikirov43@mail.ru>
Date:   Thu Jun 26 22:48:47 2025 +0300

    Second commit

commit a537d89b626484d3bab80d62493021e85d5df205
Author: Wavevladimir <vikirov43@mail.ru>
Date:   Thu Jun 26 22:25:33 2025 +0300

    First commit
wavevladimir@MacBook-Air-Vladimir my-project % git checkout a537d89b62
Note: switching to 'a537d89b62'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at a537d89 First commit
wavevladimir@MacBook-Air-Vladimir my-project % ls
first-file.txt	first-subfolder
wavevladimir@MacBook-Air-Vladimir my-project % git status
HEAD detached at a537d89
nothing to commit, working tree clean
wavevladimir@MacBook-Air-Vladimir my-project % git log
commit a537d89b626484d3bab80d62493021e85d5df205 (HEAD)
Author: Wavevladimir <vikirov43@mail.ru>
Date:   Thu Jun 26 22:25:33 2025 +0300

    First commit
wavevladimir@MacBook-Air-Vladimir my-project % git checkout main
Previous HEAD position was a537d89 First commit
Switched to branch 'main'
wavevladimir@MacBook-Air-Vladimir my-project % git log
commit bb303b80052e7e3265da94836061f87b19236be0 (HEAD -> main)
Author: Wavevladimir <vikirov43@mail.ru>
Date:   Thu Jun 26 22:48:47 2025 +0300

    Second commit

commit a537d89b626484d3bab80d62493021e85d5df205
Author: Wavevladimir <vikirov43@mail.ru>
Date:   Thu Jun 26 22:25:33 2025 +0300

    First commit
wavevladimir@MacBook-Air-Vladimir my-project % ls
first-subfolder		second-subfolder
wavevladimir@MacBook-Air-Vladimir my-project % git status
On branch main
nothing to commit, working tree clean
wavevladimir@MacBook-Air-Vladimir my-project % 
