def solution(n, computers):
    visited = [False] * n 
    network_count = 0

    def dfs(node):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_count += 1

    return network_count
