---
layout: post
title:  "github tips"
tags: github git upstream
---

github 모르면 간첩.

## fork 된 저장소 upstream으로 부터 업데이트 하기

fork 한후 upstream에 있는 변경사항을 주기적으로 싱크해야 할때 이렇게 하면 된다.
upstream은 포크 하기전 원본 저장소를 칭하는 것
{% highlight bash%}
git remote add upstream git@github.com/whoever/whatever.git
git fetch upstream
git checkout -b localupstream upstream/master # make tracking branch
git rebase upstream/master
{% endhighlight %}

## ssh key를 등록했음에도 아이디와 패스워드를 물어볼때
git clone을 하고 난후 ssh키를 등록을 했음에도 매번 아이디와 패스워드를 물어본다면 git clone을 https로 해서 그렇다. 그럴때는 이렇게 하면 된다.
{% highlight bash%}
git remote set-url origin git@github.com:username/repo.git
{% endhighlight %}


