def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    lines = []

    def snapshot():
        lines.append(" ".join(str(r) for r in rods))

    def move(disk_count, src, dst, aux):
        if disk_count == 0:
            return
        move(disk_count - 1, src, aux, dst)
        rods[dst].append(rods[src].pop())
        snapshot()
        move(disk_count - 1, aux, dst, src)

    snapshot()
    move(n, 0, 2, 1)
    return "\n".join(lines)