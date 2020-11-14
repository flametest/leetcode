/**
 * @author: flametest
 * @date: 2020/11/13
 * @time: 22:41
 * @description: 279. Perfect Squares
 */
public class PerfectSquares {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        for (int i = 0; i <= n; i++) {
            dp[i] = i;
            for (int j = 1; j <= (int) Math.sqrt(i); j++) {
                dp[i] = Math.min(dp[i], 1 + dp[i - j*j]);
            }
        }
        return dp[n];
    }
    public static void main(String[] args) {
        PerfectSquares obj = new PerfectSquares();
        System.out.println(obj.numSquares(2));
        System.out.println(obj.numSquares(12));
        System.out.println(obj.numSquares(13));
    }
}
