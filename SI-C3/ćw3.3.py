class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}

    def is_consistent(self, var, value):
        for (var2, constraint) in self.constraints[var]:
            if var2 in self.assignment:
                if not constraint(value, self.assignment[var2]):
                    return False
        return True

    def select_unassigned_variable(self):
        # Minimum Remaining Values (MRV) heuristic
        unassigned_vars = [var for var in self.variables if var not in self.assignment]
        mrv_var = min(unassigned_vars, key=lambda var: len([val for val in self.domains[var] if self.is_consistent(var, val)]))
        return mrv_var

    def backtrack(self):
        if len(self.assignment) == len(self.variables):
            return self.assignment

        var = self.select_unassigned_variable()
        for value in self.domains[var]:
            if self.is_consistent(var, value):
                self.assignment[var] = value
                result = self.backtrack()
                if result:
                    return result
                del self.assignment[var]
        return None

    def solve(self):
        return self.backtrack()


# Define variables
variables = ['X1', 'X2', 'X3']

# Define domains
domains = {
    'X1': ['R', 'B', 'G'],
    'X2': ['R'],
    'X3': ['G']
}

# Define constraints
constraints = {
    'X1': [('X2', lambda x, y: x != y), ('X3', lambda x, y: x != y)],
    'X2': [('X1', lambda x, y: x != y), ('X3', lambda x, y: x != y)],
    'X3': [('X1', lambda x, y: x != y), ('X2', lambda x, y: x != y)]
}

# Create CSP instance
csp = CSP(variables, domains, constraints)

# Solve CSP
solution = csp.solve()
print("Solution:", solution)
