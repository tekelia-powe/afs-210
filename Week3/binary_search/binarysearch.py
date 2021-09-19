class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def balanced_tree(nums):
    
    if not nums:
        return None
    #find mid point of array
    mid_val = len(nums)//2
    #set node to midpoint
    node = Node(nums[mid_val])
    '''determining if value should be placed on left or right of node
    left side < node
    right side > node
    '''
    node.left = balanced_tree(nums[:mid_val])
    node.right = balanced_tree(nums[mid_val+1:])
    return node

def OrderNode(node): 
    if not node: 
        return      
    print(node.val)
    OrderNode(node.left) 
    OrderNode(node.right)   
    
output = balanced_tree([1, 2, 3, 4, 5, 6, 7])
OrderNode(output)