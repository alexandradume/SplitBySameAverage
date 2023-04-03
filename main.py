

class Solution(object):
    def splitArraySameAverage(self, A):
        # Assume that A is the smaller array
        lengthOfA= len(A)
        lengthOfB= int(lengthOfA / 2)
        totalSum = sum(A)
        # We know that , sumOfA/lengthOfB = sumOfB / lengthOfB = sumOfC / lengthOfC, so
        # sumOfA*lengthOfB/lengthOfB = sumOfB,
        # knowing that sumOfB is an integer, it follows that sumOfA*lengthOfB%lengthOfB equals to 0
        verify = False
        for index in range(1, lengthOfB + 1):
            if totalSum * index % lengthOfA == 0:
                verify = True
                break
        # if no index can be found that satisfies the condition, the method returns false
        if not verify:
            return False
        # After that, all the possible combinations of the sum of k numbers from the table are generated
        sums = [set() for _ in range(lengthOfB + 1)]
        sums[0].add(0)
        for num in A:
            for index in range(lengthOfB, 0, -1):
                for t in sums[index - 1]:
                    sums[index].add(t + num)
        # if an index is found that satisfies the condition totalSum * index % lengthOfA == 0 and we have
        # on the index position in sums hashset the value totalSum * index / lengthOfA the method returns true
        for index in range(1, lengthOfB + 1):
            if totalSum * index % lengthOfA == 0 and int(totalSum * index / lengthOfA) in sums[index]:
                return True
        # method could not find a solution
        return False


def teste():
    # this method is one that tests some arrays that have or don't have values that can
    #        # be split into two arrays with the same average
    print("Testing started")
    solution = Solution()
    assert (solution.splitArraySameAverage([1, 1]) == True)
    assert (solution.splitArraySameAverage([1, 2, 13, 4, 5, 6, 7, 8]) == True)
    assert (solution.splitArraySameAverage([4, 6, 10, 2]) == False)
    assert(solution.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13, 14, 15, 8, 8]) == True)
    assert(solution.splitArraySameAverage([1,2,3,0])== True)
    assert(solution.splitArraySameAverage([1,2,3,4,5]) == True)
    assert(solution.splitArraySameAverage([0,0,0,0,1,1,1,1]) == True)
    assert(solution.splitArraySameAverage([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]) == False)
    print("Passed..")

if __name__ == '__main__':
    teste()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
