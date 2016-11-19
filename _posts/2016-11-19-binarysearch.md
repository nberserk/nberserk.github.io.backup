---
layout: post
title:  "binary search"
tags: algorithm
category: algorithm
---


## basic

sorted array에서 타겟값을 찾는것. 반으로 나누어서 탐색공간을 1/2씩 줄여서 O(logN)만에 원하는 값을 찾을 수 있음. 엄청나게 느리게 증가하는 것임. 70억개중 하나 찾는 것은 33번만의 분기만에 찾을 수 있음.

```java
    int binarySearch(int target, int[] a){
		int lo = 0;
		int hi = a.length - 1;
		while (lo<=hi) { // notice = is there.
			int mid = lo + (hi-lo)/2;
			if (a[mid] > target ) {
				hi = mid-1;
			}else if (a[mid] < target) {
				lo = mid + 1;
			}else{
				return mid;
			}
		}

		return -1;
	}
```

## biggest satisfying condition

약간 말을 바꾸어서 sorted array에서 target 보다 작은 수중 가장 큰 값을 찾으려면 어떻게 해야할까. `a[mid]<target`이면 `lo=mid+1` 대신에 `lo=mid`를 한다. 그 이유는 a[mid]가 largest일 수 있기 때문. 나머지 경우는 같다.


이것을 일반화 하면 특정 조건을 만족하는 가장 큰 인덱스를 구하는 것으로 볼 수 있고 아래처럼 일반화 할 수 있다. mid를 구할때 `+1`을 해주는 것은 lo=0,hi=1일때 생각하면 루프를 빠져나가지 않기 때문에 +1을 더 해준다.


```java
    int binarySearchBiggestSatisfyingCondition(int lo, int hi, IValidator validator){		
		while (lo<hi) {
			// special
			int mid = lo + (hi-lo+1)/2; // notice +1 added, to work around infinite loop
			
			if (validator.validate(mid)){
				lo = mid;
			}else {
				hi = mid-1;
			}
		}
		
		if (validator.validate(lo)) {
			return lo ;
		}		
		return -1;		
	}
```


## smallest satisfying condition

## with duplicates



## problems

- [two sum II @leetcode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [median of two sorted array @leetcode]( https://leetcode.com/problems/median-of-two-sorted-arrays/) : [explanation](https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation)


## reference

- [tutorial @topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/)
