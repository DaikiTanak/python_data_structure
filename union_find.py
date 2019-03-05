class UnionFind():
    def __init__(self, size):
        # self.parent holds a list of idx for parant node of i-th node
        # if i-th node is a root, self.parent[i] holds the - (number of nodes) in the parent.
        # if self.parent[i] = j, j-th node is a paranet of i-th node. 
        self.parent = [-1 for _ in range(size)]
        
        # self.height holds a list of trees' heights
        self.height = [0] * (size)
        
    def find(self, i):
        """
        Search for i-th node's parent.
        Args : 
            i : index of target node.
        Return :
            index of root of target node
        """ 
        
        if self.parent[i] < 0:
            # root node
            return i
        else:
            # if not root, search by the parent's node
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]     
        
    def unite(self, i, j):
        """
        Unite two parents
        Args : 
            i, j : indices of target nodes.
        """ 
        # search roots
        i = self.find(i)
        j = self.find(j)
        
        if self.height[i] < self.height[j]:
            self.parent[j] += self.parent[i]
            self.parent[i] = j
            
        else:
            self.parent[i] += self.parent[j]
            self.parent[j] = i
            if self.height[i] == self.height[j]:
                self.height[i] += 1
       
    def size(self, i):
        """
        Get num of nodes in same parent
        Args : 
            i : index of target node.
        """
        return - self.find(i)
