from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        for start, end in sorted(tickets, key = lambda x: x[1], reverse=True):
            graph[start].append(end)

        stack = ["JFK"]

        route = []

        while stack:
            current = stack[-1]

            # If there are still outgoing flights from this airport
            if graph[current]:
                # Pop the lexicographically smallest destination and move there
                next_airport = graph[current].pop()
                stack.append(next_airport)
            else:
                # If stuck (no outgoing flights left), add to route (post-order)
                route.append(stack.pop())

        # Reverse because we built the route backwards from the dead-ends
        return route[::-1]
