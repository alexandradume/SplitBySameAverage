# SplitBySameAverage
Problem:
In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)  
Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.
Example:
Sample input: 
[1,2,3,4,5,6,7,8]  
Sample output:
True
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.   
Note:  
The length of A will be in the range [1, 30].  
A[i] will be in the range of [0, 10000].

Solution:

We assume that B is the smaller array.

We know that for an array that have the propriety we search for that:
sumOfA/lengthOfA = sumOfB/lengthOfB = sumOfC/lengthOfC => 
we `have chance to split the array only if sumOfA * lengthOfB % lengthOfA = 0 (because sumOfB is integer). The algorithm performs early pruning to optimize the solution. So, if we do not find lengthOfB ( between 1 and lengthOfA/2) for which sumOfA * lengthOfB % lengthOfA is equal to 0, our array do not have this propriety.

We generate all possible combination sum of lengthOfB numbers from the array using dynamic programming. If totalSum * lengthOfB / lengthOfA exists in the lengthOfB th combination sum hashset than method returns true, otherwise returns false. 
 
