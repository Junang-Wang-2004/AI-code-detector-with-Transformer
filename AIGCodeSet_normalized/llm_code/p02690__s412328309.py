def f1(a1: int) -> Optional[Tuple[int, int]]:
    v1 = set((pow(x, 5) for v2 in range(MAX_SQ5 + 1)))
    for v3 in range(2 * MAX_SQ5 + 1):
        v4 = pow(v3, 5)
        if a1 - v4 in v1:
            return (int(pow(a1 - v4, 1 / 5)), -v3)
        if a1 + v4 in v1:
            return (int(pow(a1 + v4, 1 / 5)), v3)
    return None
