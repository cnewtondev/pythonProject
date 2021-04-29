#work on shortening accessive memory

def findClosestValue(tree, target):
    return findClosestHelper(tree, value, float("inf"))

def findClosestHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target -tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestHelper(tree.right, target, closest)
    else: 
        return closest
    