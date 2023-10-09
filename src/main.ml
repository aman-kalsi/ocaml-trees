type tree = 
| Leaf
| Node of int * tree * tree

let rec print_tree t level =
match t with
| Leaf -> "L\n"
| Node (v, l, r) -> let next_level = level+1 in string_of_int v ^ "\n" ^ print_tree l next_level ^ print_tree r next_level

let mx a b = if a > b then a else b

let rec tree_depth t =
match t with
| Leaf -> 0
| Node (v, l, r) -> let ltd = tree_depth l in let rtd = tree_depth r in 1 + mx ltd rtd

let t = Node(1, Node(2, Node(4, Leaf, Leaf), Node(5, Leaf, Leaf)), Node(3, Node(6, Leaf, Node(7, Leaf, Leaf)), Leaf))
let depth = tree_depth t

let _ = let str_depth = string_of_int depth in print_endline str_depth

