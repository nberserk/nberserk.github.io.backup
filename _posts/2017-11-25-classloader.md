---
layout: post
title:  "java classloader"
tags: classloader
published: true
---

java가 어떻게 필요한 class 들을 로드하는지 한번쯤은 궁금해 했을 법한 내용인데 이제서야 정리해 본다. 

## class loader internal

아래 종류의 클래스 로더가 존재한다. System CL까지는 우리가 몰라서 그렇지 계속 사용하게 있던 CL 되겠다.

- bootstrap class loader : java runtime을 가지고 있는 루트 CL 되겠다
- extention CL : 'java.ext.dirs' 에 있는 클래스를 로드하는 CL
- System CL : -jar 혹은 classpath로 지정된 클래스를 로드하는 CL
- custom CL : 사용자가 지정 CL

그렇다면 언제 custom CL이 필요할까?

예들 들어보면, [java tomcat](http://tomcat.apache.org/tomcat-7.0-doc/class-loader-howto.html)을 보면 될것 같다. tomcat은 여러개의 war를 서빙할 수 있는데, 각 war는 같은 클래스를 가질 수 있다. 그렇게 되면 기존의 CL로는 로딩할 수 없는 한계가 있게 된다. 그래서 custom CL의 존재가 필요하게 되는 것이다.


## reference

- [Internal of java class loading](http://www.onjava.com/pub/a/onjava/2005/01/26/classloading.html?page=1)
- [tomcat class loader](http://tomcat.apache.org/tomcat-7.0-doc/class-loader-howto.html)