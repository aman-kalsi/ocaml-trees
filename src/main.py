from collections import deque

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_depth(self):
        r = self.root

        def get_d(n):
            if not n:
                return 0

            return 1 + max(get_d(n.left), get_d(n.right)) 

        return get_d(r)

    def __str__(self):
        queue = deque([self.root])
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


def main():
    n = Node(1, Node(2, Node(4), Node(5)), Node(3))
    t = Tree(n)
    print(str(t))
    print(t.get_depth())

if __name__ == "__main__":
    main()
