# 2nd_round_set_A
# Q1 — AVL tree (range sum)

- File: avl_tree.py
- Test: test_avl.py

Concept:
Augment each AVL node with subtree_sum, subtree_min and subtree_max.
Maintain metadata on insertions and rotations so range queries can:
- Skip whole subtrees outside [L,R]
- Use subtree_sum for whole-subtree inclusion
  # Q2 — B-Tree simulation

- File: btree_sim.py
- Test: test_btree.py

Concept:
B-Tree stores multiple keys per node; tuned for disk pages.
Use case here: map chunk_id -> pointer (storage node/path).
In production use RocksDB/LMDB or dedicated index for persistent disk-backed mappings.





