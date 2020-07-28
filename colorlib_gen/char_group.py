

class CharGroup:
    def __init__(self, depth : int, children : dict):
        self.depth = depth
        self.children = children

    def get_size(self) -> int:
        size = 0
        for (_, child) in self.children.items():
            if isinstance(child, CharGroup):
                size = size + child.get_size()
            else:
                size = size + 1

        return size

    def get_max_depth(self) -> int:
        depth = self.depth
        for (_, child) in self.children.items():
            if isinstance(child, CharGroup):
                max(depth, child.get_max_depth())

        return depth

    def sort(self):
        sizes = []
        for (_, child) in self.children.items():
            if isinstance(child, CharGroup):
                sizes.append(child.get_size())
                child.sort()
            else:
                sizes.append(1)

        s = sorted(zip(sizes, self.children.items()),
                   key=lambda pair: pair[0],
                   reverse=True)
        self.children = {key: value for _, (key, value) in s}

    def __repr__(self):
        return '(' + str(self.depth) + ': ' + str(self.children) + ')'

    def __str__(self):
        return '(' + str(self.depth) + ': ' + str(self.children) + ')'
