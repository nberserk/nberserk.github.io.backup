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

## search range of target value (with duplicates)

`1, 2, 3, 3, 3, 6, 7, 9, 10` 처럼 중복된 수가 있을때 특정 값의 개수를 알려면 어떻게 해야 할까? basic처럼 해서 왼쪽, 오른쪽으로 이동하면서 범위를 찾을 수 있지만 이렇게 하면 time complexity가 O(N)이 된다.(중복된 수가 많다고 가정해 보라.) 이럴때는 바이너리서치를 2번해서 한번은 시작점을 찾고 또한번은 끝점을 찾으면 해당 값의 range를 알 수 있다.

요점은 start점을 찾을때는 타겟값을 만나면 hi를 m으로 변경하고, end점을 찾을때는 lo를 m으로 변경한다는 사실.


```java
    int binarySearchStart(int[] a, int key) {
		int lo = 0;
		int hi = a.length - 1;

		while (lo < hi) {
			int m = lo + (hi-lo) / 2;
			if (a[m] > key) {
				hi = m - 1;
			} else if (a[m] < key) {
				lo = m + 1;
			} else {
				hi = m;
			}
		}

		if (a[lo] == key) // what if key doesn't exist
			return lo;

		return -1;
	    }

    int binarySearchEnd(int[] a, int key) {
		int lo = 0;
		int hi = a.length - 1;

		while (lo < hi) {
			int m = (lo + hi + 1) / 2;
			if (a[m] > key) {
				hi = m - 1;
			} else if (a[m] < key) {
				lo = m + 1;
			} else {
				lo = m;
			}
		}

		if (a[lo] == key)
			return lo;

		return -1;

	}
```

## in a rotated array

`{5,6,7,8,1,2,3}` 처럼 한번 rotated된 배열에서 특정 숫자를 찾는다고 생각해보자. 이때에도 바이너리 서치를 사용할 수 있을까? 답은 예스. 반으로 잘랐을때 왼쪽과 오른쪽 하나는 ascending이므로 이 것을 이용해서 target이 왼쪽에 있는지 오른쪽에 있는지 판단할 수 있다!

```java
    static int bsearchRotatedSimpler(int[] a, int key){
        int lo = 0;
        int hi = a.length-1;
        while(lo<=hi){
            int m = (lo+hi)/2;    
            if(key==a[m]) return m;

            if(a[lo]<=a[m]){
                if(a[lo] <= key && key <= a[m])
                    hi=m-1;
                else lo=m+1;
            }else{
                if(a[m] <=key && key <=a[hi])
                    lo=m+1;
                else hi=m-1;
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




## problems

- [two sum II @leetcode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [Search in rotated sorted array @leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [Search in rotated sorted array II @leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) : tricky,
- [find minimum in rotated sorted array @leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [find minimum in rotated sorted array II @leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
- [find peak element @leetcode](https://leetcode.com/problems/find-peak-element/)
- [median of two sorted array @leetcode]( https://leetcode.com/problems/median-of-two-sorted-arrays/) : [explanation](https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation)


## reference

- [tutorial @topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/)
- [my implementation & test cases](https://github.com/nberserk/codejam/blob/master/java/src/main/java/crackcode/binarysearch/BinarySearch.javan)

## history

- 11/28/2016 , binarySearchRotatedArray/searchRange added
