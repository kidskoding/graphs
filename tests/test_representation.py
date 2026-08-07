"""Tests for Tier 1 — building an adjacency list from an edge list.

You implement `impl/representation.py`. These tests say what it has to do.

Run:  pytest

Neighbor lists are compared sorted — order never matters for correctness,
only membership does.
"""

import pytest

import impl.representation as rep

# Not-yet-written functions skip instead of blowing up collection.
build_adj = getattr(rep, "build_adj_list", None)
build_adj_map = getattr(rep, "build_adj_map", None)

needs_build_adj = pytest.mark.skipif(build_adj is None, reason="build_adj_list not written yet")
needs_build_adj_map = pytest.mark.skipif(
    build_adj_map is None, reason="build_adj_map not written yet"
)


def _norm(adj):
    """Normalize for comparison: sort each neighbor list."""
    if isinstance(adj, dict):
        return {k: sorted(v) for k, v in adj.items()}
    return [sorted(v) for v in adj]


# ---------------------------------------------------------------------------
# build_adj(n, edges, directed=False) -> list[list[int]]
# ---------------------------------------------------------------------------


@needs_build_adj
def test_undirected_adds_both_directions():
    # edge [0,1] must appear in BOTH node 0's list and node 1's list
    assert _norm(build_adj(3, [[0, 1], [1, 2]])) == [[1], [0, 2], [1]]


@needs_build_adj
def test_isolated_node_still_exists():
    # node 3 has no edges. It must still be there as an empty list, not missing.
    # If this fails you'll undercount connected components in Tier 2.
    adj = build_adj(4, [[0, 1], [1, 2]])
    assert len(adj) == 4
    assert adj[3] == []


@needs_build_adj
def test_no_edges_at_all():
    assert build_adj(3, []) == [[], [], []]


@needs_build_adj
def test_directed_adds_one_direction():
    adj = build_adj(3, [[0, 1], [1, 2]], directed=True)
    assert _norm(adj) == [[1], [2], []]


@needs_build_adj
def test_directed_two_cycle_keeps_both_edges():
    # [0,1] and [1,0] are two distinct directed edges. Don't collapse them.
    assert _norm(build_adj(2, [[0, 1], [1, 0]], directed=True)) == [[1], [0]]


@needs_build_adj
def test_parallel_edges_are_kept():
    # Same edge twice = two edges. A list keeps both; a set would silently drop one
    # and break any algorithm that counts degree.
    assert build_adj(2, [[0, 1], [0, 1]])[0] == [1, 1]


@needs_build_adj
def test_self_loop():
    # Undirected self-loop: decide what you want, but be consistent.
    # This asserts the common convention — appended once per direction.
    adj = build_adj(2, [[0, 0]])
    assert adj[0] == [0, 0]


@needs_build_adj
def test_star_graph():
    adj = build_adj(4, [[0, 1], [0, 2], [0, 3]])
    assert _norm(adj) == [[1, 2, 3], [0], [0], [0]]


# ---------------------------------------------------------------------------
# build_adj_map(edges, directed=False) -> dict-like
# ---------------------------------------------------------------------------


@needs_build_adj_map
def test_map_string_labels():
    adj = build_adj_map([["JFK", "SFO"], ["SFO", "LAX"]])
    assert _norm(adj) == {
        "JFK": ["SFO"],
        "SFO": ["JFK", "LAX"],
        "LAX": ["SFO"],
    }


@needs_build_adj_map
def test_map_directed_sink_is_still_a_key():
    # "b" only ever appears as a destination. It must still be a key, otherwise
    # `for node in adj` skips it and your node count is wrong.
    adj = build_adj_map([["a", "b"]], directed=True)
    assert set(adj) == {"a", "b"}
    assert adj["a"] == ["b"]
    assert adj["b"] == []


@needs_build_adj_map
def test_map_tuple_keys():
    # Grid cells as nodes — this is why you can't always use a list.
    adj = build_adj_map([[(0, 0), (0, 1)], [(0, 1), (1, 1)]])
    assert _norm(adj)[(0, 1)] == [(0, 0), (1, 1)]


@needs_build_adj_map
def test_map_empty_input():
    assert len(build_adj_map([])) == 0


@needs_build_adj_map
def test_map_does_not_grow_when_read():
    # defaultdict TRAP: `adj[missing]` INSERTS an empty list. If your code reads
    # that way while iterating you get "dictionary changed size during iteration".
    # Reading an existing key must not change the size.
    adj = build_adj_map([["a", "b"]])
    before = len(adj)
    _ = adj["a"]
    assert len(adj) == before


# ---------------------------------------------------------------------------