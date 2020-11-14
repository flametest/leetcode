import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * @author: flametest
 * @date: 2020/11/14
 * @time: 17:38
 * @description: 128. Longest Consecutive Sequence
 */
public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        int maxResult = 0;
        Set<Integer> numSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        for (int num : nums) {
            int result = 1;
            while(true) {
                if (!numSet.contains(num + 1)) {
                    break;
                }
                num += 1;
                result += 1;
            }
            maxResult = Math.max(maxResult, result);
        }
        return maxResult;
    }

    public static void main(String[] args) {
        LongestConsecutiveSequence obj = new LongestConsecutiveSequence();
        int[] nums1 = new int[] {100, 4, 200, 1, 3, 2};
        int[] nums2 = new int[] {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};
        System.out.println(obj.longestConsecutive(nums1));
        System.out.println(obj.longestConsecutive(nums2));
    }
}
