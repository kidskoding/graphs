---
aliases: ["Implicit Graphs"]
tier: 0
tags: [graphs, tier0, vocabulary, core, pattern-recognition]
---

# Implicit Graphs

**The graph is never given to you.** There's no edge list, no adjacency input. You
generate neighbors on demand from a rule.

A huge fraction of interview graph problems are implicit graphs — and people fail to
see them, then flail at the problem as if it were something exotic.

---

## The four you'll actually meet

| Problem shape | Vertex is... | Edge is... |
|---|---|---|
| **Grid** | a cell `(r, c)` | a move to an adjacent cell |
| **Word Ladder** | a word | changing exactly one letter |
| **Open the Lock** | a 4-digit combination | turning one wheel one notch |
| **Sliding Puzzle** | a whole board configuration | one legal tile slide |

The vertex count can be enormous and you never materialize it. Open the Lock has 10,000
vertices; you never build a list of them. Sliding Puzzle has up to `9! = 362,880`.

---

## Same BFS. Only the neighbor function changes.

```python
# EXPLICIT — neighbors come from a prebuilt adjacency list
for nei in adj[node]:
    ...

# IMPLICIT (grid) — neighbors computed on the fly
for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        ...

# IMPLICIT (word ladder) — neighbors are generated strings
for i in range(len(word)):
    for ch in "abcdefghijklmnopqrstuvwxyz":
        nei = word[:i] + ch + word[i+1:]
        if nei in wordSet:
            ...
```

Everything else — the `deque`, the `visited` set, the level counting — is **identical**.
Once you see this, an entire tier of "hard" problems collapses into one template.

---

## How to spot one

The prompt describes **states and transformations**, not nodes and edges:

- "minimum number of **moves** to reach..."
- "**transform** word A into word B, one letter at a time"
- "fewest **steps** to get from start to target"
- "shortest **sequence of operations**"

If each step costs the same → it's **BFS** on an implicit graph
([[04 Weighted vs Unweighted|Weighted vs Unweighted]]). If steps have different costs → Dijkstra.

> **The tell:** you're being asked for a *minimum number of moves* through a space of
> *configurations*. That is a shortest-path problem on an unweighted implicit graph,
> every single time.

---

## The one extra thing implicit graphs need

Your `visited` set holds **states**, which must be hashable. For grids that's a tuple
`(r, c)`. For a board it's usually the flattened string. Get this wrong and you either
crash or revisit forever.

```python
visited = {(r, c)}          # grid
visited = {"123450"}        # board as string
visited = {(node, mask)}    # state-augmented — Tier 10
```

That last form — packing extra information into the state — is how "at most K obstacles
removed" and "collect all keys" problems work. The graph gains a dimension. Same BFS.

---

## Related

- [[01 What Is a Graph|What Is a Graph]] — "name the vertices, name the edges" matters most here
- [[04 Weighted vs Unweighted|Weighted vs Unweighted]] — uniform move cost → BFS, varying cost → Dijkstra
- [[11 Dense vs Sparse|Dense vs Sparse]] — implicit graphs are always traversed like adjacency lists

---

⬆️ [[00 Vocabulary Index|Tier 0 - Vocabulary]] · ⬅️ [[11 Dense vs Sparse|Dense vs Sparse]] · ➡️ [[13 Graph Glossary|Graph Glossary]]
