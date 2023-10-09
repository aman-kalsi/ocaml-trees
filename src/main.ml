type tree = 
| Leaf
| Node of int * tree * tree

let rec string_of_tree t =
match t with
| Leaf -> "Leaf\n"
| Node (v, l, r) -> string_of_int v ^ "\n" ^ string_of_tree l ^ string_of_tree r

let rec sum_of_tree t = 
match t with
| Leaf -> 0
| Node (v, l, r) -> v + sum_of_tree(l) + sum_of_tree(r)

let a = Node (1, Node(2, Node(4, Leaf, Leaf), Leaf), Node(3, Leaf, Leaf))

let _ = print_endline(string_of_tree(a))
let _ = print_endline(string_of_int(sum_of_tree(a)))


