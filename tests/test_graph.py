"""Tests for impl/graph.py — the Graph class + GraphNode.

Run:  pytest

NOTE: these construct nodes as `GraphNode("a")`. Right now `GraphNode` is bare
annotations with no `__init__`, so every test errors with TypeError until you
give it one. That's the first fix.
"""

from impl.graph import Graph
from impl.graph_node import GraphNode


def _nodes(*vals):
    return [GraphNode(v) for v in vals]


# ---------------------------------------------------------------------------
# GraphNode
# ---------------------------------------------------------------------------


def test_node_stores_its_value():
    assert GraphNode("a").val == "a"


def test_distinct_nodes_with_same_value_are_different_keys():
    # Default identity hashing. Two nodes both holding "a" are two separate
    # vertices. If you add __eq__ without __hash__, this breaks and the node
    # becomes unhashable — dict keys stop working entirely.
    g = Graph()
    a1, a2 = GraphNode("a"), GraphNode("a")
    g.add_node(a1)
    g.add_node(a2)
    assert len(g.adj) == 2


# ---------------------------------------------------------------------------
# add_node
# ---------------------------------------------------------------------------


def test_add_node_creates_empty_neighbor_list():
    g = Graph()
    (a,) = _nodes("a")
    g.add_node(a)
    assert g.adj[a] == []


def test_add_node_twice_does_not_wipe_edges():
    # Re-adding an existing node must be a no-op. If add_node unconditionally
    # assigns [], this silently deletes every edge on that node.
    g = Graph()
    a, b = _nodes("a", "b")
    g.add_node(a)
    g.add_node(b)
    g.add_edge(a, b)
    g.add_node(a)
    assert g.adj[a] == [b]


# ---------------------------------------------------------------------------
# add_edge
# ---------------------------------------------------------------------------


def test_add_edge_undirected_adds_both_directions():
    g = Graph()
    a, b = _nodes("a", "b")
    g.add_node(a)
    g.add_node(b)
    g.add_edge(a, b)
    assert g.adj[a] == [b]
    assert g.adj[b] == [a]


def test_add_edge_directed_adds_one_direction():
    g = Graph(directed=True)
    a, b = _nodes("a", "b")
    g.add_node(a)
    g.add_node(b)
    g.add_edge(a, b)
    assert g.adj[a] == [b]
    assert g.adj[b] == []


def test_add_edge_rejects_unknown_node():
    g = Graph()
    a, b = _nodes("a", "b")
    g.add_node(a)  # b never added
    try:
        g.add_edge(a, b)
    except KeyError:
        pass
    else:
        raise AssertionError("expected KeyError for edge to an unadded node")


def test_add_edge_does_not_silently_create_nodes():
    # The `in` check must not be a defaultdict read that inserts the key.
    g = Graph()
    a, b = _nodes("a", "b")
    g.add_node(a)
    try:
        g.add_edge(a, b)
    except KeyError:
        pass
    assert b not in g.adj, "failed edge left a phantom node behind"
    assert len(g.adj) == 1


# ---------------------------------------------------------------------------
# remove_edge
# ---------------------------------------------------------------------------


def test_remove_edge_undirected_removes_both_directions():
    g = Graph()
    a, b = _nodes("a", "b")
    g.add_node(a)
    g.add_node(b)
    g.add_edge(a, b)
    g.remove_edge(a, b)
    assert g.adj[a] == []
    assert g.adj[b] == []


def test_remove_edge_directed_removes_one_direction():
    g = Graph(directed=True)
    a, b = _nodes("a", "b")
    g.add_node(a)
    g.add_node(b)
    g.add_edge(a, b)
    g.add_edge(b, a)
    g.remove_edge(a, b)
    assert g.adj[a] == []
    assert g.adj[b] == [a], "removing a->b must not touch b->a"


# ---------------------------------------------------------------------------
# remove_node
# ---------------------------------------------------------------------------


def test_remove_node_drops_the_node_and_all_references():
    g = Graph()
    a, b, c = _nodes("a", "b", "c")
    for n in (a, b, c):
        g.add_node(n)
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.remove_node(a)
    assert a not in g.adj
    assert g.adj[b] == []
    assert g.adj[c] == []


def test_remove_node_clears_incoming_edges_in_directed_graph():
    # b -> a. Removing a must not leave a dangling reference in b's list.
    g = Graph(directed=True)
    a, b = _nodes("a", "b")
    g.add_node(a)
    g.add_node(b)
    g.add_edge(b, a)
    g.remove_node(a)
    assert g.adj[b] == []


def test_remove_node_clears_parallel_edges():
    # a-b added twice. list.remove() deletes only the FIRST match, so a single
    # pass leaves one dangling reference to a deleted node behind.
    g = Graph()
    a, b = _nodes("a", "b")
    g.add_node(a)
    g.add_node(b)
    g.add_edge(a, b)
    g.add_edge(a, b)
    g.remove_node(a)
    assert g.adj[b] == [], f"dangling refs to removed node: {g.adj[b]}"


# ---------------------------------------------------------------------------