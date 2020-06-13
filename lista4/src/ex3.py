import random


'''
Tree node representation
'''
class Node:
    def __init__(self, key, childs = []):
        super().__init__()
        self.key = key
        self.childs = []
        assert isinstance(childs, list)
        if len(childs) > 0:
            for child in childs:
                self.add_child(child)
    

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.key)+"\n"
        for child in self.childs:
            ret += child.__repr__(level+1)
        return ret


    def add_child(self, child):
        assert isinstance(child, Node)
        self.childs.append(child)



'''
generate random tree with given height and number of child, deafult 3
'''
def rand_tree(h, nchilds=3):
   
    def rec_tree(level):
        if level < h:
            return Node(random.randint(1,1000), [rec_tree(level+1) for _ in range(random.randint(1,nchilds))])
        else:
            return  Node(random.randint(1,1000))
    
    assert h >= 0
    return rec_tree(0)



'''
depth first search
'''
def dfs(root):
    yield root.key
    for child in root.childs:
        for node in dfs(child):
            yield node



'''
breadth first search
'''
def bfs(root):
    queue = []
    queue.append(root)

    while(len(queue) > 0):
        n = queue[0]
        yield  n.key
        queue.pop(0)
        queue += n.childs

t = rand_tree(2)
print(t)
print(list(dfs(t)))
print(list(bfs(t)))