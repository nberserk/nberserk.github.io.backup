---
layout: post
title:  "proxy setting"
tags: proxy
---

어느 정도의 규모가 있는 회사는 보통 보안 및 관리상의 이유로 proxy를 많이 사용한다. 각 툴마다 설정하는 방법등이 상이해서 여기에 정리해 보고자 한다. 


## general

대부분의 shell command등은 환경변수 http(s)_proxy 을 설정하는 것만으로 대부분 잘 동작한다. 

`~/.bash_profile' 에 아래 내용을 추가.

```
export http_proxy=http://<ip:port>
export https_proxy=http://<ip:port>
```


## java cert

간혹 회사에서 https 사설 인증서를 사용하는 경우가 있는데(우리회사 --), 이런 경우 인증서가 공인인증기관에서 인증된 것이 아니기 때문에 https handshake에서 에러가 난다. 이런 경우 회사 인증서를 신뢰할 수 있다고 설정을 해줘야 하는데, 맥의 경우 아래 커맨드를 실행하면 된다.

`/Library/Java/JavaVirtualMachines/jdk1.7.0_75.jdk/Contents/Home/jre/lib/security$ sudo keytool -import -keystore cacerts -file ~/Desktop/samsung.cer`



## npm 
`~/.npmrc ` 에 아래 내용을 추가

```
registry=http://registry.npmjs.org/
strict-ssl=false
proxy=<ip:port>
https-proxy=<ip:port>
```

## pip

`~/.pip/pip.conf` 에 아래 내용 추가하거나 `pip install --proxy http://<ip:port> ipython` 이런식으로 불러주면 된다.


```
[global]
cert = <cert_path>
proxy = <ip:port>
```

## bower

`~/.bowerrc` 에 아래 내용 추가. 

```
{ 
  "proxy":"http://1<ip:port>",
  "https-proxy":"http://<ip:port>",
  "strict-ssl" : false
}
```




