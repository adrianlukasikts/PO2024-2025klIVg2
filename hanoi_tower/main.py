def hanoi_solver(current: list[int], bufor: list[int], destination: list[int], n: int):
    if n == 0:
        return
    hanoi_solver(current, destination, bufor, n - 1)
    destination.append(current.pop())
    hanoi_solver(bufor, current, destination, n - 1)


# def harder_hanoi(current: list[int], bufor: list[int], destination: list[int], n: int):
#     if n == 0:
#         return
#     harder_hanoi(current, destination, bufor, n - 1)
#     harder_hanoi(bufor, current, destination, n - 1)
#     destination.append(current.pop())
#     harder_hanoi(current, bufor, destination, n - 1)

