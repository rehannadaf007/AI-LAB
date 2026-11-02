import heapq

# Define the target configuration we want to achieve
GOAL_STATE = (1, 2, 3, 
              4, 5, 6, 
              7, 8, 0) # 0 represents the empty (blank) tile

def get_manhattan_distance(state):
    
    
    distance = 0
    for i in range(9):
        value = state[i]
        if value != 0: # Exclude the blank space from the calculation
            # Find current coordinates (row, col)
            current_row, current_col = divmod(i, 3)
            # Find target coordinates in GOAL_STATE
            target_idx = GOAL_STATE.index(value)
            target_row, target_col = divmod(target_idx, 3)
            
            distance += abs(current_row - target_row) + abs(current_col - target_col)
    return distance

def get_neighbors(state):
    
    
    neighbors = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)
    
    # Define possible movements: (row_change, col_change)
    moves = {
        'Up': (-1, 0),
        'Down': (1, 0),
        'Left': (0, -1),
        'Right': (0, 1)
    }
    
    for direction, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc
        
        # Check if the move stays inside the 3x3 boundary
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            
            # Create a new state by swapping the blank tile with the target tile
            state_list = list(state)
            state_list[blank_idx], state_list[new_blank_idx] = state_list[new_blank_idx], state_list[blank_idx]
            neighbors.append((tuple(state_list), direction))
            
    return neighbors

def solve_a_star(start_state):
    
   
    
    # Priority Queue elements format: (f_score, g_score, current_state, path_taken)
    # The path_taken stores tuples of (move_direction, resulting_state)
    start_h = get_manhattan_distance(start_state)
    open_set = [(start_h, 0, start_state, [])]
    
    # Keep track of states that have already been evaluated
    closed_set = set()
    
    while open_set:
        # Pop the state with the lowest f_score (g_score + h_score)
        f, g, current, path = heapq.heappop(open_set)
        
        # Goal check
        if current == GOAL_STATE:
            return path
            
        if current in closed_set:
            continue
            
        closed_set.add(current)
        
        # Explore adjacent moves
        for neighbor, direction in get_neighbors(current):
            if neighbor in closed_set:
                continue
                
            new_g = g + 1
            new_h = get_manhattan_distance(neighbor)
            new_f = new_g + new_h
            new_path = path + [(direction, neighbor)]
            
            heapq.heappush(open_set, (new_f, new_g, neighbor, new_path))
            
    return None # Return None if no solution exists

def print_board(state):
    for i in range(0, 9, 3):
        print(f" {state[i]} {state[i+1]} {state[i+2]} ")
    print("-" * 11)

# --- Execution Example ---
if __name__ == "__main__":
    # 0 represents the empty space
    initial_puzzle = (1, 2, 3, 
                      0, 4, 6, 
                      7, 5, 8)
    
    print("Initial State:")
    print_board(initial_puzzle)
    
    solution_path = solve_a_star(initial_puzzle)
    
    if solution_path:
        print(f"Solution Found in {len(solution_path)} moves!\n")
        for step, (move, state) in enumerate(solution_path, 1):
            print(f"Step {step}: Move Blank '{move}'")
            print_board(state)
    else:
        print("This puzzle layout is unsolvable.")
