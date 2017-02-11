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


## cert

회사 proxy에 사설 인증서를 사용하는 경우가 있는데(우리회사 --), 이런 경우 인증서가 공인인증기관에서 인증된 것이 아니기 때문에 https handshake에서 에러가 난다. 이럴경우 대부분의 https 통신이 실패하기 때문에 개발환경 잡기가 어렵다. 그때 어떻게 하면 환경을 잡을수 있는지 아래에 정리한다.

### Java

JDK가 설치된 폴더의 cacerts 파일에 keytool을 이용해서 추가해주면 된다. 아래처럼 

`/Library/Java/JavaVirtualMachines/jdk1.7.0_75.jdk/Contents/Home/jre/lib/security$ sudo keytool -import -keystore cacerts -file ~/Desktop/samsung.cer`


### pythn 

python의 cacert가 위치한 파일을 찾아서 samsung.cer을 추가


```bash
# find cacert.pem in vritualenv direcgtory
find . | grep cacert
#./venv/lib/python2.7/site-packages/requests/cacert.pem
# append samsung.cer to bottom of cacert.pem
cat samsung.cer >> ./venv/lib/python2.7/site-packages/requests/cacert.pem

```


