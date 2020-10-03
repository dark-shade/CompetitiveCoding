"""184 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        fringe = [[root, str(root.val)]]
        
        p_path = ""
        q_path = ""
        
        nodes = {}
        
        while fringe:
            curr, path = fringe.pop(0)
            nodes[curr.val] = curr
            
            if len(p_path) == 0 and str(p.val) in path.split(','):
                p_path = path
                
            if len(q_path) == 0 and str(q.val) in path.split(','):
                q_path = path
                
            if len(p_path) > 0 and len(q_path) > 0:
                p_list = p_path.split(',')
                q_list = q_path.split(',')
                p_set = set(p_list)
                q_set = set(q_list)
                
                max_ind = -1
                
                for n in p_set & q_set:
                    n_ind = p_list.index(n)
                    
                    if n_ind > max_ind:
                        max_ind = n_ind
                        
                return nodes[int(p_list[max_ind])]
                    
            
            if curr.left:
                fringe.append([curr.left, path + "," + str(curr.left.val)])
                
            if curr.right:
                fringe.append([curr.right, path + "," + str(curr.right.val)])
"""
""" 116 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        fringe = [[root, [root.val]]]
        
        p_path = ""
        q_path = ""
        
        nodes = {}
        
        while fringe:
            curr, path = fringe.pop(0)
            nodes[curr.val] = curr
            
            if len(p_path) == 0 and p.val in path:
                p_path = path
                
            if len(q_path) == 0 and q.val in path:
                q_path = path
                
            if len(p_path) > 0 and len(q_path) > 0:
                p_set = set(p_path)
                q_set = set(q_path)
                
                max_ind = -1
                
                for n in p_set & q_set:
                    n_ind = p_path.index(n)
                    
                    if n_ind > max_ind:
                        max_ind = n_ind
                        
                return nodes[int(p_path[max_ind])]
                    
            
            if curr.left:
                fringe.append([curr.left, path + [curr.left.val]])
                
            if curr.right:
                fringe.append([curr.right, path + [curr.right.val]])
"""
"""96 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        fringe = [[root, [root.val]]]
        
        p_path = ""
        q_path = ""
        
        nodes = {}
        
        while fringe:
            curr, path = fringe.pop(0)
            nodes[curr.val] = curr
            
            if len(p_path) == 0 and p.val in path:
                p_path = path
                
            if len(q_path) == 0 and q.val in path:
                q_path = path
                
            if len(p_path) > 0 and len(q_path) > 0:
                p_set = set(p_path)
                q_set = set(q_path)
                
                max_ind = -1
                
                for n in p_set & q_set:
                    n_ind = p_path.index(n)
                    
                    if n_ind > max_ind:
                        max_ind = n_ind
                        
                return nodes[int(p_path[max_ind])]
                    
            
            if curr.left and curr.val > min(p.val,q.val):
                fringe.append([curr.left, path + [curr.left.val]])
                
            if curr.right and curr.val < max(p.val,q.val):
                fringe.append([curr.right, path + [curr.right.val]])
"""
"""112 ms but 17.9 MB instead of 18 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        fringe = [[root, [root.val]]]
        
        p_path = ""
        q_path = ""
        
        while fringe:
            curr, path = fringe.pop(0)
            
            if len(p_path) == 0 and p.val in path:
                p_path = path
                
            if len(q_path) == 0 and q.val in path:
                q_path = path
                
            if len(p_path) > 0 and len(q_path) > 0:
                p_set = set(p_path)
                q_set = set(q_path)
                
                max_ind = -1
                
                for n in p_set & q_set:
                    n_ind = p_path.index(n)
                    
                    if n_ind > max_ind:
                        max_ind = n_ind
                        
                return TreeNode(int(p_path[max_ind]))
                    
            
            if curr.left and curr.val > min(p.val,q.val):
                fringe.append([curr.left, path + [curr.left.val]])
                
            if curr.right and curr.val < max(p.val,q.val):
                fringe.append([curr.right, path + [curr.right.val]])
"""
"""120 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        fringe = [[root, [root.val]]]
        
        p_path = ""
        q_path = ""
        
        while fringe:
            curr, path = fringe.pop(0)
            
            if len(p_path) == 0 and p.val in path:
                p_path = path
                
            if len(q_path) == 0 and q.val in path:
                q_path = path
                
            if len(p_path) > 0 and len(q_path) > 0:
                max_ind = -1
                
                for i, n in enumerate(p_path):
                    if n in q_path and max_ind < i:
                        max_ind = i
                        
                return TreeNode(int(p_path[max_ind]))
                    
            
            if curr.left and curr.val > min(p.val,q.val):
                fringe.append([curr.left, path + [curr.left.val]])
                
            if curr.right and curr.val < max(p.val,q.val):
                fringe.append([curr.right, path + [curr.right.val]])
"""
"""100 ms and 17.8 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
                
            elif root.val < p.val and root.val < q.val:
                root = root.right

            else:
                return root
"""