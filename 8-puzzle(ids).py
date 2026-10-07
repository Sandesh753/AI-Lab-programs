GOAL1 = (0, 1, 2,
         3, 4, 5,
         6, 7, 8)

GOAL2 = (1, 2, 3,
         4, 5, 6,
         7, 8, 0)

def inversions(state):
    arr = [x for x in state if x != 0]
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

def is_solvable(start):
    start_inv = inversions(start)
    goal1_inv = inversions(GOAL1)
    goal2_inv = inversions(GOAL2)
    return (start_inv % 2 == goal1_inv % 2 or
            start_inv % 2 == goal2_inv % 2)

def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)
    row = zero_pos // 3
    col = zero_pos % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_pos], new_state[new_pos] = \
                new_state[new_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))

    return neighbors

def depth_limited_search(state, depth, path):
    if state == GOAL1 or state == GOAL2:
        return path

    if depth == 0:
        return None

    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = depth_limited_search(
                neighbor, depth - 1, path + (neighbor,)
            )
            if result is not None:
                return result

    return None

def ids(start):
    depth = 0

    while True:
        result = depth_limited_search(start, depth, (start,))

        if result is not None:
            return result

        depth += 1

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()

print("Enter the puzzle values.")
print("Use 0 for the blank space.")

values = tuple(map(int, input("Enter 9 values: ").split()))

if len(values) != 9:
    print("Error: Enter exactly 9 values.")
    exit()

if set(values) != set(range(9)):
    print("Error: Use each number from 0 to 8 exactly once.")
    exit()

start = values

if not is_solvable(start):
    print("\nThis puzzle is NOT solvable.")
    print("No solution exists for either goal state.")
    exit()

print("\nINITIAL STATE")
print_puzzle(start)

print("========== IDS ==========")

solution = ids(start)

print("Number of moves:", len(solution) - 1)

for i, state in enumerate(solution):
    print("Step", i)
    print_puzzle(state)