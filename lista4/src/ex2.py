import random


'''
random tree
format [parent, l_subtree, r_subtree]
'''
def rand_tree(h):


    def rec_tree(level):
        if level < h:
            x = random.random()
            level += 1

            if(x < 0.30):
                return [random.randint(0,1000), None, rec_tree(level)]
            elif(x < 0.60):
                return [random.randint(0,1000), rec_tree(level), None]
            else:
                return [random.randint(0,1000), rec_tree(level), rec_tree(level)]
                
        elif level == h:
            return [random.randint(0,1000), None, None]


    if h >= 0 and type(h) is int:
        return rec_tree(0)
    else:
        raise Exception("Tree height should be positiv integer number.")


'''
depth first search
'''
def dfs(tree):
    if tree:
        yield tree[0]
        for el in dfs(tree[1]):
            yield el
        for el in dfs(tree[2]):
            yield el


'''
breadth first search
'''
def bfs(tree):
    while tree != []:
        temp = []
        for el  in tree:
            if type(el) is list:
                temp += el
            elif el:
                yield  el
        tree = temp