---
aliases: ["Vocabulary Self-Check"]
tier: 0
tags: [graphs, tier0, vocabulary, self-check]
type: quiz
---

# Vocabulary Self-Check

Cover the answers. If you can't do these cold, reread the linked note.

---

1. A connected undirected graph has 10 vertices and 9 edges. What is it, necessarily?

2. Why do you need BFS instead of DFS to find a shortest path in an unweighted graph?

3. Why is `A → B → A` a cycle in a directed graph but not in an undirected one?

4. You're given an undirected graph and told to count "groups of friends". What's the
   one line beginners forget?

5. `V = 100,000`, `E = 200,000`. Adjacency list or matrix? Why?

6. What does in-degree 0 mean, and which algorithm cares?

7. When is a topological sort impossible?

8. Sum of all degrees in an undirected graph with 7 edges?

---

## Answers

> [!success]- 1. Tree
> A **tree**. Connected + `V-1` edges ⟹ acyclic. See [[10 Trees|Trees]].

> [!success]- 2. BFS explores in rings
> BFS explores in rings of increasing distance, so the first time it reaches a vertex,
> it did so via the fewest edges. DFS plunges down one branch and can reach a vertex by
> a long route first. See [[04 Weighted vs Unweighted|Weighted vs Unweighted]].

> [!success]- 3. Edge reuse
> Undirected `A→B→A` reuses the *same edge*, which isn't allowed in a cycle. Directed
> uses two distinct edges (`A→B` and `B→A`). This is why undirected cycle detection
> skips the parent vertex. See [[06 Cyclic vs Acyclic and DAGs|Cyclic vs Acyclic and DAGs]].

> [!success]- 4. The outer loop
> `for v in range(n): if v not in visited:` — without it you only explore one component.
> See [[07 Connectivity and Components|Connectivity and Components]].

> [!success]- 5. Adjacency list
> **Adjacency list.** A matrix would need `10¹⁰` cells (~10 GB); the list needs ~300k
> entries. It also keeps traversal at `O(V+E)` instead of `O(V²)`. See [[11 Dense vs Sparse|Dense vs Sparse]].

> [!success]- 6. A source
> Nothing points to it — it's a **source**. **Kahn's algorithm** for topological sort
> repeatedly removes in-degree-0 vertices. See [[08 Degree|Degree]].

> [!success]- 7. When there's a cycle
> When the directed graph contains a cycle — i.e. it isn't a DAG. Topo sort exists
> **iff** DAG. See [[06 Cyclic vs Acyclic and DAGs|Cyclic vs Acyclic and DAGs]].

> [!success]- 8. 14
> `14`. Handshake lemma: sum of degrees = `2E`. See [[08 Degree|Degree]].

---

## Round 2 — harder

9. Every edge in a weighted graph has weight `1`. Which algorithm, and why not the obvious one?

10. You have a binary tree and need all nodes at distance `K` from some target node. Why
    can't you just recurse with the `left`/`right` pointers?

11. `n = 18` and the problem says "visit every city exactly once". What does `n = 18` tell you?

12. Why does Bellman-Ford run one extra relaxation round beyond `V-1`?

> [!success]- 9. BFS
> **BFS**, not Dijkstra. Uniform weights means the graph is effectively unweighted —
> Dijkstra gives the same answer with an unnecessary `log V` and more code to get wrong.
> See [[04 Weighted vs Unweighted|Weighted vs Unweighted]].

> [!success]- 10. The answer travels upward
> Some qualifying nodes are *above* the target (ancestors and their other subtrees).
> `left`/`right` only go down. Convert the tree to an undirected adjacency list — adding
> a parent edge for every node — then BFS. See [[10 Trees|Trees]].

> [!success]- 11. Bitmask DP
> "Visit every vertex exactly once" is a **Hamiltonian path** — NP-hard. `n ≤ ~20` is the
> signature of **bitmask DP** (`2ⁿ` states). If `n` were 10⁵, the intended answer would
> be something else entirely. See [[13 Graph Glossary|Graph Glossary]].

> [!success]- 12. Negative-cycle detection
> After `V-1` rounds every shortest path is final (a path has at most `V-1` edges). If
> anything *still* improves on round `V`, a **negative cycle** exists and no shortest
> path is well-defined. See [[05 Paths Walks and Cycles|Paths Walks and Cycles]].

---

⬆️ [[00 Vocabulary Index|Tier 0 - Vocabulary]] · 📖 [[13 Graph Glossary|Graph Glossary]]
