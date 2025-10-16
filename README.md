# 2nd_round_set_A
# Q1 — AVL tree (range sum)

- File: avl_tree.py
- Test: test_avl.py

Concept:
Augment each AVL node with subtree_sum, subtree_min and subtree_max.
Maintain metadata on insertions and rotations so range queries can:
- Skip whole subtrees outside [L,R]
- Use subtree_sum for whole-subtree inclusion

How to run:
python3 q1_avl/test_avl.py
