class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for x in range(9):
            for y in range(9):

                box_index = y//3 * 3 + x//3
                num = board[y][x]

                if num == ".":
                    continue

                if num in rows[y] or num in  columns[x] or num in boxes[box_index]:
                    return False
                rows[y].add(num)
                columns[x].add(num)
                boxes[box_index].add(num)
        return True

