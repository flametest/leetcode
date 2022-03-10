import java.util.ArrayList;
import java.util.List;

/**
 * @author: flametest
 * @date: 2021/11/24
 * @time: 23:00
 * @description: 54.Spiral Matrix
 */

public class SpiralMatrix {
//    public List<Integer> spiralOrder(int[][] matrix) {
//        List<Integer> result = new ArrayList<>();
//        int rowL = 0, rowH = matrix.length;
//        int colL = 0, colH = matrix[0].length;
//        int i = 0, j = 0;
//        int rc = 0, cc = 1;
//        while (true) {
//            result.add(matrix[i][j]);
//            System.out.println(result);
//            if (i == rowL && j == colH - 1) {
//                rowL++;
//                rc = 1;
//                cc = 0;
//            } else if (i == rowH - 1 && j == colH - 1) {
//                colH--;
//                rc = 0;
//                cc = -1;
//            } else if (i == rowH - 1 && j == colL) {
//                rc = -1;
//                cc = 0;
//                rowH--;
//            } else if (i == rowL && i != 0 && j == colL) {
//                rc = 0;
//                cc = 1;
//                colL++;
//            }
//            if (rc == 0 && cc == 1) {
//                j++;
//            } else if (rc == 1 && cc == 0) {
//                i++;
//            } else if (rc == 0 && cc == -1) {
//                j--;
//            } else if (rc == -1 && cc == 0) {
//                i--;
//            }
//
//            if (rowL > rowH || colL > colH) {
//                break;
//            }
//        }
//
//        return result;
//    }

    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        Integer minX = 0;
        Integer minY = 0;
        Integer maxX = matrix.length;
        Integer maxY = matrix[0].length;
        while (minX < maxX && minY < maxY) {
            int i = 0, j = 0;
            for (j = minY; j < maxY; j++) {
                result.add(matrix[minX][j]);
            }
            minX++;
            for (i = minX; i < maxX; i++) {
                result.add(matrix[i][maxY - 1]);
            }
            maxY--;
            if (i == maxX && j - 1 == maxY && (minX < maxX && minY < maxY)) {
                for (int k = maxY - 1; k >= minY; k--) {
                    result.add(matrix[maxX - 1][k]);
                }
                maxX--;
                for (int l = maxX - 1; l >= minX; l--) {
                    result.add(matrix[l][minY]);
                }
                minY++;
            }
        }
//        System.out.println(result);
        return result;
    }

    public static void main(String[] args) {
        SpiralMatrix solution = new SpiralMatrix();
        int[][] matrix = new int[][]{
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
        };
        System.out.println(solution.spiralOrder(matrix));
    }
}
