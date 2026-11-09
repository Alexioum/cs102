import unittest
from pathlib import Path

from src.lab3.sudoku import (
    check_solution,
    find_empty_positions,
    find_possible_values,
    generate_sudoku,
    get_block,
    get_col,
    get_row,
    group,
    read_sudoku,
    solve,
)

PUZZLES = Path(__file__).resolve().parents[2] / "src" / "lab3"


class SudokuTestCase(unittest.TestCase):
    def setUp(self):
        self.grid = read_sudoku(PUZZLES / "puzzle1.txt")

    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(group(["a", "b"], 1), [["a"], ["b"]])

    def test_get_row(self):
        self.assertEqual(get_row([["1", "2"], ["3", "."]], (1, 0)), ["3", "."])

    def test_get_col(self):
        self.assertEqual(get_col([["1", "2"], ["3", "."]], (0, 1)), ["2", "."])

    def test_get_block(self):
        self.assertEqual(get_block(self.grid, (4, 7)), [".", ".", "3", ".", ".", "1", ".", ".", "6"])

    def test_empty_positions(self):
        self.assertEqual(find_empty_positions(self.grid), (0, 2))
        self.assertIsNone(find_empty_positions(generate_sudoku(81)))

    def test_candidates(self):
        self.assertEqual(find_possible_values(self.grid, (0, 2)), {"1", "2", "4"})

    def test_solve_examples(self):
        for number in range(1, 4):
            with self.subTest(puzzle=number):
                grid = read_sudoku(PUZZLES / f"puzzle{number}.txt")
                clues = [(r, c, value) for r, row in enumerate(grid) for c, value in enumerate(row) if value != "."]
                solution = solve(grid)
                self.assertIsNotNone(solution)
                self.assertTrue(check_solution(solution))
                for row, col, value in clues:
                    self.assertEqual(solution[row][col], value)

    def test_unsolvable_restores_grid(self):
        self.grid[0][2] = "1"
        original = [row[:] for row in self.grid]
        self.assertIsNone(solve(self.grid))
        self.assertEqual(self.grid, original)

    def test_reject_invalid_solution(self):
        self.assertFalse(check_solution(self.grid))
        self.assertFalse(check_solution([list("123456789") for _ in range(9)]))
        self.assertFalse(check_solution([list("123456789"[i:] + "123456789"[:i]) for i in range(9)]))
        self.assertFalse(check_solution([["1"]]))
        grid = generate_sudoku(81)
        grid[0][0] = "0"
        self.assertFalse(check_solution(grid))
        self.assertIsNone(solve(grid))

    def test_generate(self):
        for count, filled in ((-1, 0), (0, 0), (40, 40), (81, 81), (1000, 81)):
            with self.subTest(count=count):
                grid = generate_sudoku(count)
                self.assertEqual(sum(value != "." for row in grid for value in row), filled)
                solution = solve(grid)
                self.assertIsNotNone(solution)
                self.assertTrue(check_solution(solution))
