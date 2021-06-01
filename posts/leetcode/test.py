class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:

    def __init__(self):
        self.data = ""
        self.index = 0

    def serialize(self, root):
        
        if root == None:
            return ""
        else:
            self.data = ""
            self._serialize(root)
            return self.data
    
    def _serialize(self, node):
        node_data = f"{node.label}:{len(node.neighbors)}"
        if self.data != "":
            self.data += ","
        self.data += f"{node.label}:{len(node.neighbors)}"
        for child in node.neighbors:
            self._serialize(child)

    def deserialize(self, data):
        if data == "":
            return None
        else:
            self.index = 0
            return self._deserialize(data)

    def _deserialize(self, data):
        # print(f"_deserialize: {data}, self.index: {self.index}")
        next_index = self.data.find(",", self.index)
        if next_index == -1:
            token = self.data[self.index:]
        else:
            token = self.data[self.index:next_index]
        assert ":" in token
        val, child_count = token.split(":")
        self.index = next_index + 1
        node = DirectedGraphNode(val)
        for i in range(int(child_count)):
            node.neighbors.append(self._deserialize(data))
        return node


root = DirectedGraphNode(1)
node2 = DirectedGraphNode(2)
node3 = DirectedGraphNode(3)
node4 = DirectedGraphNode(4)
node5 = DirectedGraphNode(5)
node6 = DirectedGraphNode(6)
node3.neighbors.append(node5)
node3.neighbors.append(node6)
root.neighbors.append(node2)
root.neighbors.append(node3)
root.neighbors.append(node4)

s = Solution()
print(s.serialize(root))
print(s.serialize(s.deserialize(s.serialize(root))))

