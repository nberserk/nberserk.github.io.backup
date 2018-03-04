---
layout: post
title:  "Aurora architecture"
tags: architecture aws
published: true
---

Amazon Aurora는 아마존의 managed DB service인데, 최근에 mysql이나 postgress에서 많이 갈아타는 듯 하다. 
우연히 [aurora architecutre에 관한 논문](https://www.allthingsdistributed.com/files/p1041-verbitski.pdf)을 보았는데 인상깊은 부분들이 있어 여기에 리뷰를 해보려 한다.

3가지 큰 포인트는 :
1. building storage as an independent fault-tolerant and self-healing service
1. only writing redo logs
1. make backup&recovery from one time expensive operations to asynchronous operations across a large distributed fleets.

## Durability
quorum-based voting protocol!

aws에서 사용하는 az(availability zone)은 3개. Aurora는 하나의 AZ가 고장나도 failover할 수 있는것을 목표임. 그래서 각 AZ에 2개의 storage node를 두고 총 6개의 replication을 유지. 이렇게 해서 read는 3/6 quorum, write는 4/6 quorum 을 기준으로 둔다. 즉, 6개 노드중 3개의 노드가 동일한 값을 주면 그것을 성공으로 간주, write의 경우는 4개의 노드에서 같은 응답을 받으면 성공으로 간주 하게 된다.

이렇게 해서 OS나 security updates등도 쉽게 적용할 수 있게 된다. 사용자도 모르게.

## Log equlas DB

storage node로 전송하는 것은 redo log뿐이다. database page를 매번 처음부터 생성하는 것은 비싼 작업이기 때문에 중간중간에 materialize를 시킨다. 그래서 recovery등은 checkpointing과는 다르게 빠르게 실행된다.




최신의 OLTP DB에서는 여러 스토리지 노드로 IO를 분산할 수 있기 때문에, IO는 더이상 bottleneck이 아니다. bottleneck은 network으로 옮겨가고 있다.

기존의 DB 시스템의 disk read/write등은 syncrounous인데, 모든 노드에게서 응답을 받을 때까지 대기하게 되고, transaction인 경우 얘기는 더 복잡해진다. multip-phase sync protocol은 2-phase commit등은 더 challeging 하다. 

그래서, Aurora에서는 traditional kernel(query processor, transactions, locking, buffer cache, access methods, undo mgmt)등과 storage node(redo logging, durable storage, crash recovery)의 기능을 구분한다.








## References

- [checkstyle](ttp://checkstyle.sourceforge.net/index.html)




