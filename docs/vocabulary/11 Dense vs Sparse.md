---
aliases: ["Dense vs Sparse"]
tier: 0
tags: [graphs, tier0, vocabulary, complexity]
---

# Dense vs Sparse

How many edges are there, relative to how many *could* be there?

---

## Maximum edges in a simple graph

| | Max edges |
|---|---|
| Undirected | `V(V-1)/2` ≈ `V²/2` |
| Directed | `V(V-1)` ≈ `V²` |

(Both assume a [[09 Self-Loops and Multi-Edges|simple graph]] — no self-loops, no parallel edges.)

- **Sparse**: `E` is roughly proportional to `V`. Most real graphs. Road networks, social
  graphs, [[10 Trees|trees]], grids. A 4-directional grid has `E ≈ 4V` no matter how big it gets.
- **Dense**: `E` is close to `V²`. Every-vertex-connects-to-most-others. A **complete
  graph** (`K_n`, everything connected to everything) is maximally dense.

---

## Why you care — it decides your representation

| | Adjacency list | Adjacency matrix |
|---|---|---|
| Space | `O(V + E)` | `O(V²)` — always, even for 1 edge |
| Find all neighbors of `u` | `O(deg(u))` | `O(V)` — must scan the whole row |
| Check "is there an edge `u→v`?" | `O(deg(u))` | **`O(1)`** |
| Best for | **sparse** (i.e. almost always) | dense, or heavy edge-existence queries |

**Default to an adjacency list.** In interview problems it's right ~90% of the time.

Reach for a matrix when:
- the input *arrives* as a matrix (e.g. `isConnected[i][j]` in "Number of Provinces"),
- `V` is small (≤ 500),
- or the algorithm needs `O(1)` edge lookups (Floyd-Warshall).

---

## The complexity trap

BFS/DFS is `O(V + E)` with an adjacency list — but **`O(V²)` with a matrix**. Visiting
each vertex forces a scan of its entire `V`-length row, whether or not those edges exist.

On a sparse graph with `V = 10⁵`, that's the difference between instant and never
finishing:

```
adjacency list:   V + E   =  100,000 + 200,000    ≈  3 × 10⁵    ✅
adjacency matrix: V²      =  10,000,000,000       ≈  10¹⁰       ❌
```

A matrix would also need ~10 GB of memory. This is not a theoretical concern.

---

## Related

- [[02 Vertex and Edge|Vertex and Edge]] — the `V` and `E` notation
- [[08 Degree|Degree]] — average degree is `2E/V` for undirected graphs
- Tier 1 Representation — the actual code for building each

---

⬆️ [[00 Vocabulary Index|Tier 0 - Vocabulary]] · ⬅️ [[10 Trees|Trees]] · ➡️ [[12 Implicit Graphs|Implicit Graphs]]
