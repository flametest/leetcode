/**
 * Copyright@www.zzcrowd.com.
 *
 * @author: Jun Jiang
 * @date: 2019-06-01
 * @time: 20:36
 * @description:
 */
public class PeakElement {
    public int findPeakElement(int[] nums) {
        int idx = 0;
        int m = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (m < nums[i]) {
                m = nums[i];
                idx = i;
            }
            if ( i == 0 || i == nums.length) {
                continue;
            }
            if (nums.length >=3 && i > 1 && i < nums.length - 1) {
                if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
                    return i;
                }
            }
        }
        return idx;
    }

    public static void main(String[] args) {
        int[] nums = new int[] { -2147483648,-2147483647};
        PeakElement obj = new PeakElement();
        System.out.println(obj.findPeakElement(nums));
    }
}
