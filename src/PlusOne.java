import javax.swing.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author: flametest
 * @date: 2020/11/13
 * @time: 18:59
 * @description
 */
public class PlusOne {

    public int[] plusOne(int[] digits) {
        int length = digits.length;
        List<Integer> result = new ArrayList<>();
        int plusNumber = 1;
        for (int i = length - 1; i >= 0 ; i--) {
            int prevDigit = digits[i] + plusNumber;
            if (prevDigit > 9) {
                prevDigit = prevDigit % 10;
                plusNumber = 1;
            } else {
                plusNumber = 0;
            }
            result.add(0, prevDigit);
        }
        if (plusNumber != 0) {
            result.add(0, plusNumber);
        }
        return result.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        int[] digits0 = new int[] {4, 3, 2};
        int[] digits1 = new int[] {3, 2, 9};
        int[] digits2 = new int[] {5, 9, 9};
        int[] digits3 = new int[] {9};
        int[] digits4 = new int[] {};
        int[] digits5 = new int[] {9, 9, 9, 9, 9};
        PlusOne obj = new PlusOne();
        System.out.println(Arrays.toString(obj.plusOne(digits0)));
        System.out.println(Arrays.toString(obj.plusOne(digits1)));
        System.out.println(Arrays.toString(obj.plusOne(digits2)));
        System.out.println(Arrays.toString(obj.plusOne(digits3)));
        System.out.println(Arrays.toString(obj.plusOne(digits4)));
        System.out.println(Arrays.toString(obj.plusOne(digits5)));
    }
}
