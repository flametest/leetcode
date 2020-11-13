import java.util.Arrays;
import java.util.stream.Collectors;

/**
 * @author: flametest
 * @date: 2020/11/13
 * @time: 20:01
 * @description: 48. Rotate Image
 */
public class RotateImage {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int start=0, end = n-1;
        System.out.println(start + " " + end);
        while (start < end) {
            for (int i = 0; i < n; i++) {
                int tmp = matrix[start][i];
                matrix[start][i] = matrix[end][i];
                matrix[end][i] = tmp;
            }
            start++;
            end--;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
    }
    public static void main(String[] args) {
        int[][] matrix0 = new int[][] {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[][] matrix1 = new int[][] {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
        int[][] matrix2 = new int[][] {{1}};
        int[][] matrix3 = new int[][] {{1, 2}, {3, 4}};
        RotateImage obj = new RotateImage();
        obj.rotate(matrix0);
        obj.rotate(matrix1);
        obj.rotate(matrix2);
        obj.rotate(matrix3);
        System.out.println(Arrays.stream(matrix0).map(Arrays::toString).collect(Collectors.toList()));
        System.out.println(Arrays.stream(matrix1).map(Arrays::toString).collect(Collectors.toList()));
        System.out.println(Arrays.stream(matrix2).map(Arrays::toString).collect(Collectors.toList()));
        System.out.println(Arrays.stream(matrix3).map(Arrays::toString).collect(Collectors.toList()));
    }
}
