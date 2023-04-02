# SplitBySameAverage
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
We need to split A into B and C. Considering that B should have the same mean as A, sumOfB * lengthB = sumOfA * lengthA, so sumOfB is an integer. For this fact we can optimize our search, we cannot find a valid solution if sumOfA * lengthB % lengthA is not equal to 0.
The check method recursively tries to see if we can create with the values we have in A sumOfB. If so, check returns true otherwise false.
