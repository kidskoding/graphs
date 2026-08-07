# representing graphs via adjacency lists

def build_adj_list(n: int, edges: list[list[int]], directed: bool=False) -> list[list[int]]:
    res = [[] for _ in range(n)]

    for (u, v) in edges:
        res[u].append(v)
        if not directed:
            res[v].append(u)

    return res
