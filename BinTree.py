from random import choice

class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BTCalc:

    @staticmethod
    def treeAverage(node):
        (sum, count) = BTCalc.__sumAndCount(node)
        return sum / count

    @staticmethod
    def treeSum(node):
        (sum, count) = BTCalc.__sumAndCount(node)
        return sum

    @staticmethod
    def treeMedian(node):
        valueList = BTCalc.__toList(node)
        if len(valueList) % 2 == 1:
            return BTCalc.__quickselect(valueList, (len(valueList)-1)/2)
        else:
            val1 = BTCalc.__quickselect(valueList, (len(valueList)/2) - 1)
            val2 = BTCalc.__quickselect(valueList, (len(valueList) / 2))
            return (val1 + val2) / 2

    @staticmethod
    def __sumAndCount(node):
        treeSum = node.val
        treeCount = 1
        if node.left:
            left = BTCalc.__sumAndCount(node.left)
            treeSum += left[0]
            treeCount += left[1]
        if node.right:
            right = BTCalc.__sumAndCount(node.right)
            treeSum += right[0]
            treeCount += right[1]
        return treeSum, treeCount
    @staticmethod
    def __toList(node):
        if node.left:
            leftList = BTCalc.__toList(node.left)
        else:
            leftList = []
        if node.right:
            rightList = BTCalc.__toList(node.right)
        else:
            rightList = []
        return leftList + [node.val] + rightList
    @staticmethod
    def __quickselect(valueList, k):
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
            return BTCalc.__quickselect(left, k)
        elif len(left) + len(middle) > k:
            return pivot
        else:
            return BTCalc.__quickselect(right, k - len(left) - len(middle))


