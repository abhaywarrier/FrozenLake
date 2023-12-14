def generate_custom_map(size, num_potholes):
    assert size >= 4, "Size must be at least 4"
    assert num_potholes < (size ** 2) - 3, "Too many potholes for the given size"

    # Create a map with all frozen tiles
    custom_map = np.full((size, size), 'F')

    # Set the starting point and the goal
    custom_map[0, 0] = 'S'
    custom_map[size - 1, size - 1] = 'G'

    # Randomly place potholes
    pothole_indices = np.random.choice(range(size*size), num_potholes, replace=False)
    row_indices, col_indices = np.unravel_index(pothole_indices, (size, size))
    custom_map[row_indices, col_indices] = 'H'

    return custom_map.tolist()