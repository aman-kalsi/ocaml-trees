from collections import deque

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_depth(self, n):
        if not n:
            return 0

        return 1 + max(self.get_depth(n.left), self.get_depth(n.right)) 

    def print_helper(self, n):
        queue = deque([n])
        s = []

        while queue:
            size = len(queue)
            
            for _ in range(size):
                cur = queue.popleft()
                s.append(str(cur.val))
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            s.append('\n')

        return ''.join(s)

    def __str__(self):
        return self.print_helper(self.root)

def main():
    n = Node(1, Node(2, Node(4), Node(5)), Node(3))
    t = Tree(n)
    print(str(t))
    print(t.get_depth(t.root))

if __name__ == "__main__":
    main()
