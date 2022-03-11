import java.util.ArrayList;
import java.util.List;

public class StringToInteger {
    public int myAtoi(String s) {
        double result = 0.0;
        StringBuffer buffer = new StringBuffer();
        for (int i = 0; i < s.length(); i++) {
            Character e = s.charAt(i);
            if ('0' <= e && e <= '9' ||
                    ((e == '+' || e == '-') && buffer.length() == 0)) {
                buffer.append(e);
            } else {
                if (e != ' ') {
                    break;
                } else if (e == ' ' && buffer.length() != 0) {
                    break;
                }
            }

        }
//        System.out.println(buffer);
        int sign = 1;
        for (int i = 0; i < buffer.length(); i++) {
            char c = buffer.charAt(i);
            if (c == '-') {
                sign = -1;
                continue;
            }
            if (c == '+') {
                sign = 1;
                continue;
            }
            int d = Integer.parseInt(String.valueOf(buffer.charAt(i))) * sign;
            result = result * 10 + d;
            if (result > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }
            if (result < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
        }

        return (int) result;
    }

    public static void main(String[] args) {
        StringToInteger s = new StringToInteger();
        System.out.println(s.myAtoi("42"));
        System.out.println(s.myAtoi("   -42"));
        System.out.println(s.myAtoi("4193 with words"));
        System.out.println(s.myAtoi("words and 987"));
        System.out.println(s.myAtoi("-91283472332"));
        System.out.println(s.myAtoi("+-12"));
        System.out.println(s.myAtoi("00000-42a1234"));
        System.out.println(s.myAtoi("   +0 123"));
    }
}
