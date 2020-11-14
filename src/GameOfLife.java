import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @author: flametest
 * @date: 2020/11/14
 * @time: 13:53
 * @description:
 */
public class GameOfLife {
    public void gameOfLife(int[][] board) {
        int row = board.length;
        int column = row > 0 ? board[0].length : 0;
        System.out.println(row + "," + column);
        int[][] result = new int[row][column];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                int neighborNum = countNeighbors(i, j, board, row, column);
                System.out.println(i + "," + j + ":" + neighborNum);
                if (board[i][j] == 1) {
                    if (neighborNum < 2 || neighborNum > 3) {
                        result[i][j] = 0;
                    }
                    if (neighborNum == 2 || neighborNum == 3) {
                        result[i][j] = 1;
                    }
                }
                if (board[i][j] == 0 && neighborNum == 3) {
                    result[i][j] = 1;
                }
            }
        }
        for (int i = 0; i < row; i++) {
            board[i] = Arrays.copyOf(result[i], column);
        }
        System.out.println(Arrays.stream(board).map(Arrays::toString).collect(Collectors.toList()));
    }

    public int countNeighbors(int xPosition, int yPosition, int[][] board, int row, int column) {
        int neighborNum = 0;
        List<Integer> rowList = List.of(xPosition - 1, xPosition + 1, xPosition);
        List<Integer> columnList = List.of(yPosition - 1, yPosition + 1, yPosition);
        for (Integer xIdx : rowList) {
            for (Integer yIdx : columnList) {
                if (xIdx >= 0 && xIdx < row && yIdx >= 0 && yIdx < column
                        && (xIdx != xPosition || yIdx != yPosition)) {
                    if (board[xIdx][yIdx] == 1) {
                        neighborNum = neighborNum + 1;
                    }
                }
            }
        }
        return neighborNum;
    }
    public static void main(String[] args) {
        GameOfLife obj = new GameOfLife();
        int[][] board0 = new int[][] {{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
//        int[][] board1 = new int[][] {{0, 0, 0}, {1, 0, 1}, {0, 1, 1}, {0, 1, 0}};
        obj.gameOfLife(board0);
//        obj.gameOfLife(board1);
    }
}
