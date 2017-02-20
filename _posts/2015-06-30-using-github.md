---
layout: post
title:  "github tips"
tags: github git upstream
---

github 모르면 간첩.

## fork 된 저장소 upstream으로 부터 업데이트 하기

fork 한후 upstream에 있는 변경사항을 주기적으로 싱크해야 할때 이렇게 하면 된다.
upstream은 포크 하기전 원본 저장소를 칭하는 것

```bash
git checkout master
git remote add upstream git@github.com:whoever/whatever.git
git fetch upstream # update apache remote
git rebase upstream/master # rebase upstream/master to current branch(master)
# make tracking branch 이렇게하면 upstream은 apache master와 싱크를 하게 되고, 로컬에 unpushed commit이 생기게 된다.
git push # git push로 내 계정의 git에 최신사항으로 업데이트 함.


# merge upstream with master; 최신 변경 사항을 master로 가지고 온다.
#git checkout master
#git merge upstream

# make topic branch;
git checkout -b topic # make topic branch
git push -u origin topic # push topic branch to origin
# 이 상태에서 github상에서 pull request를 요청하면 된다.
```

## make topic branch

포크한 repo에서 바로 작업을 하게 되면 나중에 apache/master를 rebase하기가 힘들어 진다. 그래서 토픽 브랜치를 만들어서 거기서 태스크를 위한 커밋을 하고, 준비가 되면 거기서 바로 pull request를 하고, 업스트림에 머지가 되면 그 토픽브랜치는 이제 더이상 필요가 없다. 그후 업스트림으로 부터 다시 리베이스를 하면 마스터 브랜치는 최신으로 유지가 가능하다.


```bash
# assume current branch is master
git checkout -b topic # make topic branch
...
git commit -m "..."
git push -u origin topic # push topic branch to origin
# 이 상태에서 github상에서 pull request를 요청하면 된다.

git checkout master
git merge --squash topic  # merge to master ans make 1 commit
```


## undoing commits

git reset 명령을 하게 되면 커밋은 돌려지고 HEAD의 체인지가 워킹 디렉토리에 반영이 되지만(그래서 원복을 할 기회가 있음.), --hard를 붙이면 워킹 디렉토리의 변경사항은 없다. 따라서 --hard옵션은 조심해서 쓸것.

```bash
git reset --hard <dest_commithash> # move head to the designated commit
git reset (--hard) HEAD^1 # reset last commit
# HEAD^1 : parent of head
```


## revision selection


- `HEAD^1` : parent of head
- `HEAD^2` : 2nd parent of head. only valid for merge commit
- `HEAD@{n}` : nth prior head

## cherrypick specific file from different branch

`git cherry-pick`은 커밋 단위로 가지고 오기때문에, 다른 파일의 변경사항도 같이 적용이 된다. 이럴때는 `checkout file`을 사용하면 된다.


```bash
git checkout <branch> -- <filename>
```

## ssh key를 등록했음에도 아이디와 패스워드를 물어볼때
git clone을 하고 난후 ssh키를 등록을 했음에도 매번 아이디와 패스워드를 물어본다면 git clone을 https로 해서 그렇다. 그럴때는 이렇게 하면 된다.

```bash
git remote set-url origin git@github.com:username/repo.git
```




