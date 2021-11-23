
/**
 * @author: flametest
 * @date: 2020/11/13
 * @time: 18:59
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
