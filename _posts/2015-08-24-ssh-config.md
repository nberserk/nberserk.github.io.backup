---
layout: post
title:  "ssh config"
tags: ssh
---

aws를 사용하다보면 ssh 작업을 많이 하게 되는데, 이 때 알아두면 너무 너무 편리한 팁들이다. 

## 패스워드 없이 ssh
나의 public key(.ssh/id_rsa.pub)를 대상 컴의 .ssh/authrized_keys 에 복사해주면
` ssh user@server ls / `를 패스워드 없이 바로 실행할 수 있다.

만약 .ssh 폴더가 없다면, `ssh-keygen -t rsa`로 생성해 주면 된다.

## .ssh/config
ssh의 여러가지 설정을 담고 있는 설정 파일이다. 

```
Host my
     User darren
     Hostname 10.1.1.1
```

위 설정 파일을 사용하면 `ssh my`만 타이핑 하면, `ssh darren@10.1.1.1`로 번역되어 실행 된다.

```
Host bas
     User ec2-user
     Hostname bastion
     Port 352
     IdentityFile ~/.ssh/bastion.pem
```

위 설정 파일은 `ssh bas`를 `ssh -i ~/.ssh/bastion.pem ec2-user@bastion -p 352` 로 해석 된다.

## ssh tunneling
특정 포트를 포트 포워딩할 수도 있다. 보통 회사의 네트웍 같은 경우 80 포트를 제외한 나머지는 모두 방화벽으로 막혀 있는 경우가 많은데 이럴때 유용하게 사용할 수 있다.

```
Host tunnel
    HostName mysql
    IdentityFile ~/.ssh/mysql.key
    LocalForward 9906 127.0.0.1:3306
    User mysqlUser
```

database컴의 3306 포트가 localhost:9906로 포트 포워딩 된다. localhost:9906에서 mysql의 웹에 접근할 수 있다. 
## ControlPath
control path를 사용하면 ssh connection을 캐쉬 해서 접속 시간을 줄일 수 있어, 반복적으로 ssh 명령을 불러야 할때 사용하면 유용하다.

```
Host *
	ControlPath            ~/.ssh/mux-%r@%h:%p
```
## proxyCommand
TBD


## Reference
- [ssh proxy](http://backdrift.org/transparent-proxy-with-ssh)
- [ssh portforward](http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/)


## revision history
* 2015/8/24 initial draft
* 8/28 ControlPath added


