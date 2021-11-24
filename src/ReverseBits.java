
/**
 * @author: flametest
 * @date: 2021/11/23
 * @time: 21:59
 * @description: 190. Reverse Bits
 */
public class ReverseBits {
    public int reverseBits(int n) {
        String binaryN = String.format("%32s", Integer.toBinaryString(n)).replace(' ', '0');
        StringBuilder s = new StringBuilder(binaryN);
        String reversedBinaryN = s.reverse().toString();
        return Integer.parseUnsignedInt(reversedBinaryN, 2);
    }
    public static void main(String[] args) {
        ReverseBits r = new ReverseBits();
        System.out.println(r.reverseBits(43261596));
    }
}

// Another Solution
// https://leetcode.com/problems/reverse-bits/discuss/1559375/Java-beats-99

//public class Solution {
//    // you need treat n as an unsigned value
//    public int reverseBits(int n) {
//        int result = 0;
//        int lastBit;
//        for(int i = 0; i < 32; i++){
//            // get the last bit of n
//            lastBit = n & 1;
//            // shift n for new last bit
//            n >>= 1;
//            // shift result so previous last bit is at the front
//            result <<= 1;
//            // add result last bit
//            result |= lastBit;
//        }
//        return result;
//    }
//}
