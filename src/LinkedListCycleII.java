import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * @author: flametest
 * @date: 2021/5/6
 * @time: 4:42 PM
 * @description: 142. Linked List Cycle II
 */

class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
     val = x;
     next = null;
  }
}

public class LinkedListCycleII {
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }
        List<ListNode> all = new ArrayList<>();
        while (head.next != null) {
            all.add(head);
            head = head.next;
            if (all.contains(head)) {
                return head;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        LinkedListCycleII l = new LinkedListCycleII();
        ListNode a = new ListNode(3);
        a.next = new ListNode(2);
        a.next.next = new ListNode(0);
        ListNode b = new ListNode(-4);
        a.next.next.next = b;
        b.next = a.next;
        System.out.println(l.detectCycle(a));
        System.out.println(l.detectCycle(null));
    }
}