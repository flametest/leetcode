import java.util.Objects;

/**
 * @author: flametest
 * @date: 2022/03/10
 * @time: 23:00
 * @description: 28. Implement strStr()
 */

public class ImplementstrStr {
    public int strStr(String haystack, String needle) {
//        if (Objects.equals(needle, "")) {
//            return 0;
//        }
//        for (int i = 0; i < haystack.length(); i++) {
//            for (int j = i; j < haystack.length(); j++) {
//                String subStr = haystack.substring(i, j + 1);
//                if (subStr.equals(needle)) {
//                    return i;
//                }
//            }
//        }
//        return -1;


//        if (Objects.equals(needle, "")) {
//            return 0;
//        }
//        int i = 0, j = 0;
//        int needleLen = needle.length();
//        while (i < haystack.length()) {
//            if (haystack.indexOf(i) == needle.indexOf(0)) {
//                int end = Math.min(i + needleLen, haystack.length());
//                String subStr = haystack.substring(i, end);
//                if (subStr.equals(needle)) {
//                    return i;
//                }
//            }
//            i++;
//        }
//        return -1;

        if (Objects.equals(needle, "")) {
            return 0;
        }

        int i = 0, j = needle.length();
        while (j <= haystack.length()) {
            String subStr = haystack.substring(i, j);
            if (subStr.equals(needle)) {
                return i;
            }
            i++;
            j++;
        }
        return -1;
    }

    public static void main(String[] args) {
        String haystack = "hello", needle = "ll";
        ImplementstrStr s = new ImplementstrStr();
        System.out.println(s.strStr(haystack, needle));
        String a = "a", b = "a";
        System.out.println(s.strStr(a, b));
        String c = "aaaaa", d = "bba";
        System.out.println(s.strStr(c, d));
    }
}
