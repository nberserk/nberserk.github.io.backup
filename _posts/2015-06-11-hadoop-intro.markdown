---
layout: post
title:  "hadoop 소개"
published: false
categories: hadoop
---

## 소개
하둡은 hdfs + MapReduce + ResourceManager(YARN) 이라고 볼 수 있다. 하둡은 현재 사용되고 있는 모든 클라우드 기술의 근간이라고 봐도 될정도로 기본이 되는 것이고, 모두가 이 hdfs + MR 에 기반해서 새로운 기술들이 나오고 있다. 해서 모든 빅데이터 개발자들의 필수 코스라고 생각된다. 
* hdfs :  distribugted file system, replication은 parallelism의 근간. 하나의 노드의 파일이 날라가도 replication으로 복구하는 컨셉.
* MapReduce : MR 프로그램을 돌릴 수 있는 프레임웍. 그 유명한 Map Reduce. 물리적으로 하나의 컴퓨터에서 계산이 불가능한 것을 여러대의 컴으로 Map 해서 따로 계산후 Reduce로 취합하는 개념.
* YARN : hadoop 2.x 버전 부터 Resource Manager가 독립이 되어 생긴 모듈. 

## 설치 및 설정





