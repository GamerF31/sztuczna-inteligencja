def resolution(KB, alpha):
    clauses = KB + [negate(alpha)]
    new = set()

    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]

        for (ci, cj) in pairs:
            resolvent = resolve(ci, cj)
            if not resolvent:
                return True
            new.add(frozenset(resolvent))

        if new.issubset(set(map(frozenset, clauses))):
            return False

        for clause in new:
            if clause not in clauses:
                clauses.append(list(clause))


def negate(clause):
    # Negate the given clause
    return [-literal for literal in clause]


def resolve(ci, cj):
    # Resolve two clauses
    resolvent = set(ci).union(set(cj))
    for literal in ci:
        if -literal in cj:
            resolvent.remove(literal)
            resolvent.remove(-literal)
    return list(resolvent)


# Example usage
KB = [[1, 2], [-1, 3], [-2, -3]]
alpha = [3]
print(resolution(KB, alpha))  # Output: True or False depending on the KB and alpha
