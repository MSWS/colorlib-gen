

class CharGroup:
    def __init__(self, depth : int, children : dict):
        self.depth = depth
        self.children = children

    def get_size(self):
        size = 0
        for (_, child) in self.children.items():
            if isinstance(self.children, dict):
                size = size + child.get_size()
            else:
                size = size + 1

    def get_max_depth(self):
        depth = self.depth
        for (_, child) in self.children.items():
            if isinstance(self.children, dict):
                max(depth, child.get_max_depth())

    def __repr__(self):
        return '{' + str(self.depth) + ': ' + str(self.children) + '}'

    def __str__(self):
        return '{' + str(self.depth) + ': ' + str(self.children) + '}'
        