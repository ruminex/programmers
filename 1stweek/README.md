1주차 스터디



 1. DFS를 구현하는 대표적인 두 가지 방법은 재귀 호출을 이용하는 것과 명시적인 스택(Stack) 자료구조를 사용하는 것입니다. 각 구현 방식의 장단점을 비교 설명해주세요

    · 재귀 호출 방식

    재귀 호출 방식의 경우에는 시스템 스택을 활용 하므로 명시적인 스택 사용 없이 구현이 가능합니다. 추가적으로 코드의 길이가 매우 간결해 진다는 장점이 있습니다.

    단점으로는 그래프가 깊고 크기가 매우 큰 경우에는, 시스템 재귀 호출 스택이 한계를 넘어서 스택 오버플로우가 생길 수 있습니다.

    · 명시적인 스택(Stack) 자료구조 사용 방식

    스택을 명시적으로 관리 함으로써, 스택 크기를 직접 제어할 수 있어서 메모리 관리에 더 용이하며, 시스템의 호출 스택한계에 영향을 받지 않습니다.

    단점으로는 재귀 방식에 비해서 코드가 길어지며, 관리해야 할 스택이 추가되므로 코드가 복잡해 질 수 있습니다.

    거기에 더해서 스택의 상태를 추적하고 관리해주는 코드를 직접적으로 구현해 주어야 합니다.



2. 방향 그래프(Directed Graph)에서 사이클(Cycle) 존재 여부를 판별하기 위해 DFS를 어떻게 활용할 수 있는지 구체적인 알고리즘을 설명해주세요

    방향 그래프를 DFS를 통해서 경로를 탐색하는 중, 사이클이 존재 하는지 아닌지를 판별하는 알고리즘으로는

    현재 탐색 경로상에 있는 노드를 다시 방문할 경우 사이클이 존재한다고 할 수 있습니다.

    이를 위해 노드를 다음 세 가지 상태 중 하나로 관리합니다:

    방문 전 (B = 0)

    현재 탐색 경로상에 있음 (V = 1)

    방문 완료 (E = 2)

    DFS를 활용한 사이클 판별 알고리즘 코드

       def has_cycle(n, graph):
           visited = [0] * n  # 0: B, 1: V, 2: E

       def dfs(node):
           if visited[node] == 1:
           return True  # 사이클 발견
       if visited[node] == 2:
           return False  # 이미 끝난 경로

       visited[node] = 1  # 방문 중
       for neighbor in graph[node]:
           if dfs(neighbor):
           return True

        visited[node] = 2  # 방문 완료
        return False

       for i in range(n):
           if visited[i] == 0:
           if dfs(i):
              return True

       return False




4. 재귀를 활용한 DFS에서 가장 최근의 노드로 돌아가는 백트래킹 동작이 어떤 방식으로 동작하는지 하나의 예를 들어 설명해주세요

    재귀를 활용한 DFS에서 백트래킹 동작은 호출된 재귀함수가 종료 되었을 때, 시스템 스택에 가장 최근에 호출 되었던 함수를 다시 불러와서 실행시키는 방식으로 이루어져 있습니다.

    재귀 함수 dfs를 구현하고

       def dfs(node, visited, graph):
           visited[node] = True
           print(f"Enter Node {node}")

       for neighbor in graph[node]:
           if not visited[neighbor]:
               dfs(neighbor, visited, graph)

       print(f"Exit Node {node}")  # 백트래킹 위치

    예제 그래프를 이런식으로 만들었다고 가정시

       graph = {
           0: [1, 2],
           1: [0, 3],
           2: [0],
           3: [1]
       }
       visited = [False] * 4

    이런식으로 결과물이 나오게 됩니다.

       Enter Node 0
       Enter Node 1
       Enter Node 3
       Exit Node 3
       Exit Node 1
       Enter Node 2
       Exit Node 2
       Exit Node 0



풀어볼 문제

1. 깊이 우선 탐색 순회(몸 풀기 문제)

2. [네트워크(프로그래머스)](https://school.programmers.co.kr/learn/courses/30/lessons/43162)

   [정답](https://github.com/ruminex/programmers/blob/main/network.py)

4. [전력망을 둘로 나누기(프로그래머스)](https://school.programmers.co.kr/learn/courses/30/lessons/86971)

5. [양궁 대회(프로그래머스)](https://school.programmers.co.kr/learn/courses/30/lessons/92342)
