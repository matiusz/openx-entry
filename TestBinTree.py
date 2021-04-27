import unittest

from BinTree import BTCalc, BTNode

class TestBinTree(unittest.TestCase):
    def setUp(self):
        self.root = BTNode(5)
        self.root.left = BTNode(3)
        self.root.right = BTNode(7)
        self.root.left.left = BTNode(2)
        self.root.left.right = BTNode(5)
        self.root.right.left = BTNode(1)
        self.root.right.right = BTNode(0)
        self.root.right.right.left = BTNode(2)
        self.root.right.right.right = BTNode(8)
        self.root.right.right.right.right = BTNode(5)
    def test_treeSum(self):
        self.assertEqual(BTCalc.treeSum(self.root), 38)
    def test_treeAverage(self):
        self.assertEqual(BTCalc.treeAverage(self.root), 3.8)
    def test_treeMedianOdd(self):
        self.root.right.right.right.right = None
        self.assertEqual(BTCalc.treeMedian(self.root), 3)
    def test_treeMedianEven(self):
        self.assertEqual(BTCalc.treeMedian(self.root), 4)

    def test_leafSumAndAverage(self):
        self.root.left = None
        self.root.right = None
        self.assertEqual(BTCalc.treeSum(self.root), 5)
        self.assertEqual(BTCalc.treeAverage(self.root), 5)
    def test_leafMedian(self):
        self.root.left = None
        self.root.right = None
        self.assertEqual(BTCalc.treeMedian(self.root), 5)
if __name__ == '__main__':
    unittest.main()