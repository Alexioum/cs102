"""Сравнение времени решения трёх пазлов."""

from multiprocessing import Process
from pathlib import Path
from threading import Thread
from time import perf_counter

from .sudoku import check_solution, read_sudoku, solve


def run_solve(filename: str) -> None:
    """Решить один пазл и вывести время."""
    grid = read_sudoku(Path(__file__).with_name(filename))
    start = perf_counter()
    solution = solve(grid)
    elapsed = perf_counter() - start
    correct = solution is not None and check_solution(solution)
    print(f"{filename}: {elapsed:.3f} с, верно: {correct}", flush=True)


def main() -> None:
    """Запустить три способа решения."""
    files = ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt")
    print("Последовательно", flush=True)
    start = perf_counter()
    for filename in files:
        run_solve(filename)
    print(f"Общее время: {perf_counter() - start:.3f} с", flush=True)

    for worker, name in ((Thread, "Потоки"), (Process, "Процессы")):
        print(name, flush=True)
        start = perf_counter()
        jobs = [worker(target=run_solve, args=(filename,)) for filename in files]
        for job in jobs:
            job.start()
        for job in jobs:
            job.join()
        print(f"Общее время: {perf_counter() - start:.3f} с", flush=True)


if __name__ == "__main__":
    main()
