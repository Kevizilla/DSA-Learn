package hashmap;

import java.util.LinkedList;

public class HashMap {
    private LinkedList<Entry>[] buckets;  // array of linked lists
    private int capacity;

    HashMap(int capacity) {
        this.capacity = capacity;
        buckets = new LinkedList[capacity];
        for (int i = 0; i < capacity; i++) {
            buckets[i] = new LinkedList<>();
        }
    }

    private int hash(String key) {
        return Math.abs(key.hashCode() % capacity);
    }

    public void put(String key, int value) {
        int index = hash(key);
        for(Entry e : buckets[index]) {
            if(e.key.equals(key)){
                e.value = value;
                return;
            }
        }
        buckets[index].add(new Entry(key, value));
    }

    public int get(String key) {
        int index = hash(key);
        for(Entry e : buckets[index]) {
            if(e.key.equals(key)){
                return e.value;
            }
        }
        return -1;
    }

    public void remove(String key) {
        // TODO
    }
}
