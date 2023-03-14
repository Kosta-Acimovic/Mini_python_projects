def tower_of_hanoi(n1, start, end, extra):
    if n1 == 1:
        print(f"Move disk 1 from source {start} to destination {end}")
        return
    tower_of_hanoi(n1 - 1, extra, end, start)
    print(f"Move disk {n1} from source {start} to destination {end}")
    tower_of_hanoi(n1 - 1, extra, end, start)


n = 3

tower_of_hanoi(n, 'A', 'C', 'B')
