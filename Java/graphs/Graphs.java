package graphs;

import java.util.*;

public class Graphs {
    private Map<Integer, List<Integer>> adjList;

    public Graphs() {
        adjList = new HashMap<>();
    }

    public void addVertex(int vertex) {
        adjList.putIfAbsent(vertex, new ArrayList<>());
    }

    public void addEdge(int v1, int v2) {
        addVertex(v1);
        addVertex(v2);
        adjList.get(v1).add(v2);
        adjList.get(v2).add(v1);

    }

    public void display() {
        for(int i : adjList.keySet()) {
            System.out.println(i + " -> " + adjList.get(i));
        }
    }

    public void bfs(int start) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();

        visited.add(start);
        queue.add(start);

        while (!queue.isEmpty()) {
            int current = queue.poll();   // dequeue from front
            System.out.print(current + " ");

            for (int neighbour : adjList.get(current)) {
                if (!visited.contains(neighbour)) {
                    visited.add(neighbour);
                    queue.add(neighbour);
                }
            }
        }
    }
}