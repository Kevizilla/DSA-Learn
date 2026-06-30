package graphs;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

 class Graphs {
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
}