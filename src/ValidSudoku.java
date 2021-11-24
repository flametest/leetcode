import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author: flametest
 * @date: 2021/11/23
 * @time: 23:06
 * @description: 36. Valid Sudoku
 */

public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, List<Character>> rowMap = new HashMap<>();
        Map<Integer, List<Character>> colMap = new HashMap<>();
        for (int column = 0; column < board.length; column += 3) {
            for (int row = 0; row < board[column].length; row += 3) {
                List<Character> block = new ArrayList<>();
                for (int i = row; i < row + 3; i++) {
                    for (int j = column; j < column + 3; j++) {
                        char item = board[i][j];
                        if (item == '.') {
                            continue;
                        }
                        rowMap.computeIfAbsent(i, k -> new ArrayList<>());
                        colMap.computeIfAbsent(j, k -> new ArrayList<>());
                        if (block.contains(item) || rowMap.get(i).contains(item) || colMap.get(j).contains(item)) {
                            return false;
                        }
                        rowMap.get(i).add(item);
                        colMap.get(j).add(item);
                        block.add(item);
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        ValidSudoku solution = new ValidSudoku();
        char[][] board1 = new char[][]{
                {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                {'.', '.', '.', '.', '8', '.', '.', '7', '9'},
        };
//        System.out.println(solution.isValidSudoku(board1));
        char[][] board2 = new char[][]{
                {'8', '3', '.', '.', '7', '.', '.', '.', '.'},
                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                {'.', '.', '.', '.', '8', '.', '.', '7', '9'},
        };
//        System.out.println(solution.isValidSudoku(board2));
        char[][] board3 = new char[][]{
                {'.', '.', '4', '.', '.', '.', '6', '3', '.'},
                {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'5', '.', '.', '.', '.', '.', '.', '9', '.'},
                {'.', '.', '.', '5', '6', '.', '.', '.', '.'},
                {'4', '.', '3', '.', '.', '.', '.', '.', '1'},
                {'.', '.', '.', '7', '.', '.', '.', '.', '.'},
                {'.', '.', '.', '5', '.', '.', '.', '.', '.'},
                {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'.', '.', '.', '.', '.', '.', '.', '.', '.'}
        };
        System.out.println(solution.isValidSudoku(board3));
    }
}
