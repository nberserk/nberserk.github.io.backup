---
layout: post
title:  "Maximum XOR"
tags: algorithm
published: false
---

아래 문제를 보자

```
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
Could you do this in O(n) runtime?

Example:
Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

```

위 문제는 naive하게는 두원소를 가면서 매번 XOR를 해서 max를 구하면 된다. 이것은 O(N^2).

## idea

먼저 하나의 bit만 생각해보자. n번째 bit a^b 이 1이 되려면 1과 0이 둘다 있어야 한다. 그런데 우리는 최대값을 구하는 것이므로 가장 상위의 bit가 1이 되는것이 우선이다. 그래서 31번째 bit부터


```java
    
```


## Problems


- [Maximum XOR  @leetcode](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) 

## Reference




