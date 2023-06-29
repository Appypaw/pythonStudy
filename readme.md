파이썬 공부.

Troubleshooting
1. Git 연동 문제.
"pythonStudy/ does not have a commit checked out"는 "pythonStudy/" 디렉토리가 Git 저장소에 커밋되지 않아서 발생하는 문제.

    git init 명령을 사용하여 "pythonStudy/" 디렉토리를 Git 저장소로 초기화하세요. 다음 명령을 실행하여 "pythonStudy/" 디렉토리를 Git 저장소로 만듭니다:

cd pythonStudy/
git init

이 명령은 "pythonStudy/" 디렉토리를 Git 저장소로 초기화.

변경 사항을 스테이징 영역에 추가하고 "pythonStudy/" 디렉토리에서 변경된 파일을 스테이징 영역에 추가하기 위해 git add.를 실행.

git add .

이 명령은 "pythonStudy/" 디렉토리의 변경된 파일을 스테이징 영역에 추가합니다.
(스테이징 영역은 커밋에 포함될 변경 사항들을 임시로 저장하는 공간)
커밋을 생성하세요. 변경 사항을 커밋으로 기록하기 위해 다음 명령을 실행하세요:

git commit -m "test"

"main" 브랜치를 원격 저장소로 푸시 변경 사항을 원격 저장소로 푸시하려면 다음 명령을 실행하세요:

    git push -u origin main

    이 명령은 "main" 브랜치를 원격 저장소의 "main" 브랜치로 푸시하고 로컬 "main" 브랜치를 원격 "origin" 저장소의 "main" 브랜치와 연결

위 단계를 따라 진행하면 "pythonStudy/" 디렉토리의 변경 사항이 스테이징되고 커밋하는데 성공.

2. 또 생긴 문제. 터미널 로그

PS C:\python> git commit -m "syntax, Variables 추가" 
On branch main

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        pythonStudy/

nothing added to commit but untracked files present (use "git add" to track)
PS C:\python> cd pythonStudy
PS C:\python\pythonStudy> git commit -m "syntax, Variables 추가"
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Basic Syntax/Syntax.py
        Basic Syntax/Variables.py

nothing added to commit but untracked files present (use "git add" to track)
PS C:\python\pythonStudy> git add .
PS C:\python\pythonStudy> git commit -m "syntax, Variables 추가"
[main 8df69c4] syntax, Variables 추가
 2 files changed, 52 insertions(+)
 create mode 100644 Basic Syntax/Syntax.py
 create mode 100644 Basic Syntax/Variables.py
PS C:\python\pythonStudy> git push -u origin main
git: 'credential-vscode' is not a git command. See 'git --help'.
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 929 bytes | 929.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Appypaw/pythonStudy.git
   7712c2b..8df69c4  main -> main
branch 'main' set up to track 'origin/main'.
PS C:\python\pythonStudy>

다음과 같이 해결
