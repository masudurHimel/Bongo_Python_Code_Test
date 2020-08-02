class Node:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent

def lca(node1, node2):
    """ 
    Finds and Prints the least common ancestor between two nodes (Node Types)

    Parameters: 
    node1 (__main__.Node): subject node1 
    node2 (__main__.Node): subject node2

    Performance analysis:
    1.  Time Complexity : O(n), Linear Time Complexity
    2. Space Complexity: O(1), Constant Space Complexity
    ** Explanation can be found on the "Task_3_Performance_Analysis.pdf" file**

    Returns: 
    Node.value (int,float,str,list etc): Returns the Least Common Ancestor's value
    """

    if not isinstance(node1, Node) or not isinstance(node2, Node):
        raise TypeError("Passed Arguement must be Node type !")

    node1_depth = find_depth(node1)
    node2_depth = find_depth(node2)
    
    if node1_depth > node2_depth:
        i = node1_depth - node2_depth
        while i !=0:
            node1 = node1.parent
            i -=1
    else:
        i = node2_depth - node1_depth
        while i !=0:
            node2 = node2.parent
            i -=1
    
    while(1):
        if (node1.value == node2.value):
            return node1.value
        elif (node1 == None or  node2 == None):
            return "Not Found"
        node1 = node1.parent
        node2 = node2.parent

    
    
def find_depth(target_node):
    """ 
    Finds the depth of a node (Node Type) in the tree

    Parameters: 
    target_node (__main__.Node): targeted node to find the depth

    Returns: 
    int: returns the depth of the passed node in the tree
    """
    depth = 0
    while target_node.parent is not None:
        depth+=1
        target_node = target_node.parent
    return depth


if __name__ == '__main__':
    root = Node(1, None)
    node2 = Node(2,root)
    node3 = Node(3,root)
    node4 = Node(4,node2)
    node5 = Node(5,node2)
    node6 = Node(6,node3)
    node7 = Node(7,node3)
    node8 = Node(8,node4)
    node9 = Node(9,node4)

    print(lca(node3,node7))
