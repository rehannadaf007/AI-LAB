def solve_8_queens():
    # Board size
    N = 8
    
    # Tracking sets for O(1) constraint verification
    cols = set()        # Tracks occupied columns
    diag1 = set()       # Tracks positive diagonals (row + col)
    diag2 = set()       # Tracks negative diagonals (row - col)
    
    # Store the column position for each row: index = row, value = col
    current_assignment = [-1] * N
    all_solutions = []

    def backtrack(row):
        # Base case: If all rows are assigned, a valid configuration is found
        if row == N:
            all_solutions.append(list(current_assignment))
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            # Constraint Checklist: Verify if the position is safe
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue  # Constraint violated, skip this position

            # Forward Phase: Apply constraints and assign value
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            current_assignment[row] = col

            # Move to the next variable (row)
            backtrack(row + 1)

            # Backtrack Phase: Remove constraints and clear assignment
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
            current_assignment[row] = -1

    # Initiate backtracking search from the first row
    backtrack(0)
    return all_solutions

def print_board(solution):
    """Helper function to visually print the chessboard grid"""
    for col in solution:
        row_str = [" . "] * 8
        row_str[col] = " Q "
        print("".join(row_str))
    print("\n" + "="*24 + "\n")

# Run the solver
solutions = solve_8_queens()

print(f"Total valid configurations found: {len(solutions)}\n")
print("First configuration matrix layout:")
print_board(solutions[0])
