from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)

    for a in graph:
        graph[a].sort(reverse=True)

    route = []
    stack = ["ICN"]
    while stack:
        cur = stack[-1]
        if graph[cur]:
            stack.append(graph[cur].pop())
        else:
            route.append(stack.pop())

    return route[::-1]