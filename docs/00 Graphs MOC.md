---
aliases: ["Graphs MOC"]
tags: [graphs, moc]
type: map-of-content
---

# Graphs MOC

Map of content for graph mastery. Ground-up order — each tier needs the one before it.

**Tiers 0–6 are non-negotiable (~80% of interview graph questions). 7–8 next. 9–10 only if time remains.**

---

## Tiers

| Tier | Topic | Status |
|---|---|---|
| 00 | [[00 Vocabulary Index|Tier 0 - Vocabulary]] | 📝 written |
| 01 | Representation | ⬜ todo |
| 02 | Traversal | ⬜ todo |
| 03 | BFS as Shortest Path | ⬜ todo |
| 04 | Ordering and Structure | ⬜ todo |
| 05 | Union-Find | ⬜ todo |
| 06 | Weighted Shortest Path | ⬜ todo |
| 07 | Trees as Graphs | ⬜ todo |
| 08 | MST | ⬜ todo |
| 09 | Advanced Structure | ⬜ todo |
| 10 | Hard Tier | ⬜ todo |

---

## The meta-skill — recognizing a graph problem

Problems are not labeled "graph". Triggers:

| Prompt says | Reach for |
|---|---|
| shortest / fewest steps / minimum moves | BFS |
| shortest with costs | Dijkstra |
| is it possible to order / prerequisites / dependencies | topological sort |
| groups / merge / connected / same set | Union-Find |
| reach every node with min cost | MST |
| transform A into B one step at a time | [[12 Implicit Graphs|Implicit Graphs]] + BFS |
| grid + regions / spread | flood fill / multi-source BFS |
| "at most K of X" | state-augmented BFS/Dijkstra |

---

## Complexity — say these out loud in the interview

| Algorithm | Complexity |
|---|---|
| BFS / DFS | `O(V+E)` |
| Dijkstra (heap) | `O((V+E) log V)` |
| Bellman-Ford | `O(V·E)` |
| Floyd-Warshall | `O(V³)` |
| Union-Find | `O(α(n))` ≈ `O(1)` amortized |
| Kruskal | `O(E log E)` |
| Prim | `O(E log V)` |
| Grid | `V = R·C`, `E = 4·R·C` → `O(R·C)` |

See [[11 Dense vs Sparse|Dense vs Sparse]] for why representation choice can silently turn `O(V+E)` into `O(V²)`.

---

## Quick reference

- [[13 Graph Glossary|Graph Glossary]] — every term in one table
- [[14 Vocabulary Self-Check|Vocabulary Self-Check]] — test yourself cold
