---
layout: post
title:  Hadoop cluster docker for ARM
tags: hadoop arm docker
---

ARM architecture에 hadoop cluster docker image를 만들어 보았다.

docker hub의 armv7/armhf-ubuntu_core:15.10  이미지를 기반으로 Dockerize를 시도.

크게 3개의 이미지를 만들 것
- hadoop-base 
- hadoop-slave
- hadoop-master


## hadoop-base image



hadoop-base 에서는 slave와 master에서 공통적으로 사용할 것들을 설정
* install java, openssh server
* qemu-arm-static. 이것은 아래에서 설명
* passwordless ssh
* install hadoop


#### qemu-arm-static
qemu를 사용해서 x86 머신에서 docker를 빌드/테스트 하는 이유는 아래 2가지 이유 때문.

1. arm device가 잘 없다는 것. raspberry pi 정도?
1. arm device는 대게 x86 desktop 보다 느리니까

그래서 구글링 하다가 [qemu를 이용해서 하는 방법](https://resin.io/blog/building-arm-containers-on-any-x86-machine-even-dockerhub/)을 찾아서 따라해 보니 잘 동작한다. 원리는 모든 커맨드 바로 앞에 `qemu-arm-static`을 붙여서 arm instruction을 x86으로 변환해 주는 것 되겠다.

## install packages


java, ssh server, vim 등을 설치해 준다.


```
RUN apt-get update && apt-get install -y openjdk-7-jdk openssh-server openssh-client rsync vim

```

## passwordless ssh

hadoop cluster를 구성하려면 cluster간 passwordless ssh가 구성이 되어야 한다. 그것을 위해서 

```
# sshd setting
RUN ssh-keygen -t rsa -f /root/.ssh/id_rsa -P ''
RUN cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
ADD config /root/.ssh/
RUN chmod 600 /root/.ssh/config
#RUN chown root:root /root/.ssh/config  
RUN echo 'root:sheepdog' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo "UsePAM no" >> /etc/ssh/sshd_config
RUN echo "Port 2122" >> /etc/ssh/sshd_config

```


## Controller

urls.py를 request url을 regex로 각 뷰로 dispatch한다.

```python
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    ]
```

## View(Template)

우리가 서버로 사용하는 것은 Django이고 실제로 웹사이트의 사용자가 보게 되는 것은 html이다. 그러면 django object를 html로 변환하는 과정이 필요하게 마련인데, 이것을 해주는 것이 template 되겠다.

object는 handle bar형식으로 표현이 되고, 그 외의 것은 `{% raw %} {% tag %} {% endraw %}`로 표현이 된다. 아래의 예제에서 extends, block, for, endfor, endblock 등이 되겠다.

신선했던 것은 template도 상속관계를 가질수 있다는 것. 그래서 전체적인 구조(block)는 base.html에서 잡아두고, override 하고 싶은 부분만 extends해서 커스터마이징 할 수 있다. 실제로도 아주 편한 피쳐임.

```html
{% raw %}
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}
{% endraw %}

```


## revision history
* 2016-4-15 draft
* 2016-5-10 controller, view 업데이트



