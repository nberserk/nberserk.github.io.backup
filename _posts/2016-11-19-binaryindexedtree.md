---
layout: post
title:  "binary indexed tree"
tags: tree
category: algorithm
---

binary indexed tree(bit)는 [Segment tree]({% post_url 2015-11-11-segmenttree %})처럼 range sum을 구하는 것에 최적화된 알고리즘이지만, segment tree보다 구현이 훨씬 쉽다. 대신 이해는 좀 더 여렵다. 그래서 segment tree는 이제 안녕.



|     |time complexity|
|:---:|:-------------:|
|construction| O(NlogN)|
| sum | O(logN) |
| update | O(logN)|



## intro

 i번째 비트가 1이면 그 수부터 밑으로 `2^(i-1)`개의 숫자를 더한 값을 tree에 가지고 있게 정하자.그러면 sum(n)은 n의 1bit가 들어가는 tree의 값들을 더해주면 sum(n)을 구할 수 있다. 아래 예를 보면 이해가 되려나.. 

```
1=0b01,  1(0b1)부터 1(2^0)까지의 합
2=0b10,  2(0b10)부터 1(2로부터 2개는 1임)까지의 합
3=0b11,  a[3] + tree(2)
```

## 2D


## problems

- [Range sum query 2D @leetcode](https://leetcode.com/problems/range-sum-query-2d-mutable/)


## reference

