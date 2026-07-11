import graphs.Graphs;

class Test {
    public static void main(String[] args) {
        Graphs x = new Graphs();
        x.addEdge(0, 1);
        x.addEdge(0, 2);
        x.addEdge(1, 2);
        x.addEdge(2, 3);
        x.addEdge(3, 4);
        x.addEdge(4, 5);
        x.display();
        x.bfs(2);
    }
}
