import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

/**
 * Copyright@www.zzcrowd.com.
 *
 * @author: Jun Jiang
 * @date: 2019-06-01
 * @time: 19:02
 * @description:
 */
public class LRUCache {
    private int capacity;
    private List<Integer> list;
    private Map<Integer, Integer> map;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.list = new LinkedList<>();
        this.map = new HashMap<>();
    }

    public int get(int key) {
        int value = -1;
        if (this.map.containsKey(key)) {
            value = this.map.get(key);
            int i = this.list.indexOf(key);
            if (i != -1) {
                this.list.remove(i);
                this.list.add(0, key);
            }
        }
        return value;
    }

    public void put(int key, int value) {
        if (this.map.containsKey(key)) {
            int i = this.list.indexOf(key);
            this.list.remove(i);
        } else {
            if (this.list.size() >= this.capacity) {
                int removedKey = this.list.remove(this.capacity - 1);
                this.map.remove(removedKey);
            }
        }

        this.list.add(0, key);
        this.map.put(key, value);
    }

    @Override
    public String toString() {
        return "LRUCache{" +
                "capacity=" + capacity +
                ", list=" + list +
                ", map=" + map +
                '}';
    }

    public static void main(String[] args) {
        LRUCache obj = new LRUCache(2);
        obj.put(2, 1);
        obj.put(2, 2);
        obj.get(2);
        obj.put(1, 1);
        obj.put(4, 1);
        obj.get(2);
    }
}
