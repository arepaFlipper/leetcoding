# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def depth_first_search(node):
            if not node:
                res.append("#")
                return 
            value = str(node.val)
            res.append(value)
            depth_first_search(node.left)
            depth_first_search(node.right)

        depth_first_search(root)
        return ",".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        self.i = 0

        def depth_1st_search():
            if values[self.i] == "#":
                self.i += 1
                return None
            
            value = int(values[self.i])
            node = TreeNode(value)
            self.i += 1
            node.left = depth_1st_search()
            node.right = depth_1st_search()

            return node
        return depth_1st_search()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
