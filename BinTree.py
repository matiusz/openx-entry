from random import choice

class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BTCalc:
    def treeAverage(self, node):
        (sum, count) = self.__sumAndCount(node)
        return sum / count
    def treeSum(self, node):
        (sum, count) = self.__sumAndCount(node)
        return sum
    def treeMedian(self, node):
        valueList = self.__toList(node)
        if len(valueList) % 2 == 1:
            return self.__quickselect(valueList, (len(valueList)-1)/2)
        else:
            val1 = self.__quickselect(valueList, (len(valueList)/2) - 1)
            val2 = self.__quickselect(valueList, (len(valueList) / 2))
            return (val1 + val2) / 2
    def __sumAndCount(self, node):
        treeSum = node.val
        treeCount = 1
        if node.left:
            left = self.__sumAndCount(node.left)
            treeSum += left[0]
            treeCount += left[1]
        if node.right:
            right = self.__sumAndCount(node.right)
            treeSum += right[0]
            treeCount += right[1]
        return treeSum, treeCount
    def __toList(self, node):
        if node.left:
            leftList = self.__toList(node.left)
        else:
            leftList = []
        if node.right:
            rightList = self.__toList(node.right)
        else:
            rightList = []
        return leftList + [node.val] + rightList
    def __quickselect(self, valueList, k):
        pivot = choice(valueList)
        left = []
        middle = []
        right = []
        for val in valueList:
            if val < pivot:
                left.append(val)
            elif val == pivot:
                middle.append(val)
            else:
                right.append(val)
        if len(left) > k:
            return self.__quickselect(left, k)
        elif len(left) + len(middle) > k:
            return pivot
        else:
            return self.__quickselect(right, k - len(left) - len(middle))


