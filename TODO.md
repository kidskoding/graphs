# Graphs Checklist

> 📖 Notes: [docs/00 Graphs MOC.md](<docs/00 Graphs MOC.md>) — Obsidian vault, wikilinked

---

## Tier 1 — Representation (highest-leverage, most-fumbled)

- [x] Adjacency list (`defaultdict(list)`) — default choice, `O(V+E)` space

~~- [ ] Adjacency matrix — only when dense or need `O(1)` edge lookup~~
- [ ] Edge list — input format, MST input
- [ ] **Building from input**: edge list → adj list. Directed adds one direction, undirected adds both.
- [ ] **Implicit graphs**: grid cells, word strings, lock states, board configs — neighbors generated on the fly
- [ ] 1-indexed vs 0-indexed traps

---

## Tier 2 — Traversal (the spine)

- [ ] DFS recursive
- [ ] DFS iterative w/ explicit stack (recursion limit)
- [ ] BFS w/ `deque`
- [ ] **`visited` placement** — mark when you *push*, not when you pop
- [ ] Connected components / counting
- [ ] Grid traversal: 4-dir + 8-dir neighbor gen, bounds check, in-place marking vs visited set
- [ ] Flood fill, island counting, island area, perimeter

---

## Tier 3 — BFS as shortest path

- [ ] BFS = shortest path on **unweighted** graphs
- [ ] Level-by-level BFS (`for _ in range(len(q))`)
- [ ] Path reconstruction via `parent` dict
- [ ] **Multi-source BFS** — seed queue with all sources at distance 0
- [ ] Bidirectional BFS (word ladder speedup)
- [ ] **0-1 BFS** — deque, `appendleft` for 0-weight edges

---

## Tier 4 — Ordering & structure

- [ ] Cycle detection, **undirected** — DFS with parent tracking
- [ ] Cycle detection, **directed** — 3-color (white/gray/black)
- [ ] Bipartite / 2-coloring (BFS or DFS)
- [ ] **Topological sort — Kahn's (BFS + in-degree)**
- [ ] **Topological sort — DFS postorder**
- [ ] Kahn's as cycle detector (leftover nodes = cycle)
- [ ] DAG longest path / DP over topo order

---

## Tier 5 — Union-Find (DSU)

- [ ] `find` with path compression
- [ ] `union` by rank/size
- [ ] Counting components incrementally
- [ ] Cycle detection on undirected via union
- [ ] Applications: redundant connection, accounts merge, equations satisfiability

---

## Tier 6 — Weighted shortest path

- [ ] **Dijkstra** — heap; why it breaks on negative edges; lazy deletion (stale entries)
- [ ] Dijkstra path reconstruction
- [ ] **Modified-state Dijkstra** — state = `(node, extra_dim)` e.g. k-stops left, obstacles removed
- [ ] Dijkstra variants where relax op isn't `+`: max-probability (`*`), min-effort (`max`), widest path
- [ ] **Bellman-Ford** — negative edges, negative-cycle detection, `V-1` relaxations
- [ ] **Floyd-Warshall** — all-pairs, `O(V³)`, tiny graphs only

---

## Tier 7 — Trees as graphs

- [ ] Rooting an undirected tree, parent tracking
- [ ] Tree diameter (2× BFS, or DFS returning depth)
- [ ] **LCA** — binary lifting
- [ ] Rerooting / DP on tree
- [ ] Convert binary tree → undirected graph, then BFS (distance-K problems)

---

## Tier 8 — MST

- [ ] **Kruskal** (sort edges + DSU)
- [ ] **Prim** (heap)
- [ ] When each wins (sparse → Kruskal, dense → Prim)
- [ ] Critical / pseudo-critical edges

---

## Tier 9 — Advanced structure

- [ ] **SCC** — Tarjan (one pass, lowlink) or Kosaraju (two DFS)
- [ ] Condensation graph → DAG → topo sort on it
- [ ] **Bridges & articulation points** — Tarjan lowlink
- [ ] **Eulerian path/circuit** — Hierholzer, degree conditions
- [ ] Hamiltonian path → NP-hard, means bitmask DP not greedy

---

## Tier 10 — Hard tier

- [ ] **Bitmask + BFS/Dijkstra** — state includes visited-set bitmask
- [ ] **Max flow** — Dinic's / Edmonds-Karp; min-cut = max-flow
- [ ] **Bipartite matching** — Kuhn's / Hopcroft-Karp, or model as flow
- [ ] A* (know it exists)

---

## Meta-skill — recognizing a graph problem

Problems are not labeled "graph". Triggers:

| Prompt says | Reach for |
|---|---|
| shortest / fewest steps / minimum moves | BFS |
| shortest with costs | Dijkstra |
| is it possible to order / prerequisites / dependencies | topological sort |
| groups / merge / connected / same set | Union-Find |
| reach every node with min cost | MST |
| transform A into B one step at a time | implicit graph BFS |
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
