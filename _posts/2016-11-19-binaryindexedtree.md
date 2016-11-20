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



## idea

integer는 2^n승의 조합으로 표현할 수 있는것처럼, cumulative sum도 그렇게 나타낼 수 있겠다는 것.
2진수 표현에서 착안.
`tree(i) = sum from i-2^r+1 to i`
라고 정의 r은 i를 2진수로 나타내었을때 마지막 1이 있는 자리수. 0b10은 1, 0b1은 0 

아래 예를 보면 이해가 되려나.. 

```
1=0b01,  r=0, [1-1]까지의 합. 
2=0b10,  r=1, [1-2]까지의 합
3=0b11,  step0: 0b11, r=0, [3-3]까지의 합
         step1: 0b10, r=1, [1-2]까지의 합.
```

## 2D


## problems

- [Range sum query 2D @leetcode](https://leetcode.com/problems/range-sum-query-2d-mutable/)


## reference

