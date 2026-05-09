# Available colours
colours = ["Red", "Green", "Blue"]

# Define neighbouring regions
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "QLD"],
    "SA": ["WA", "NT", "QLD", "NSW", "VIC"],
    "QLD": ["NT", "SA", "NSW"],
    "NSW": ["QLD", "SA", "VIC"],
    "VIC": ["SA", "NSW"],
    "TAS": []
}

# Store assigned colours
assigned = {}

# Function to check if colour assignment is valid
def is_valid(region, colour):
    for neighbour in neighbors[region]:
        if neighbour in assigned and assigned[neighbour] == colour:
            return False
    return True

# Backtracking algorithm
def solve(regions):
    if len(assigned) == len(regions):
        return True

    region = regions[len(assigned)]

    for colour in colours:
        if is_valid(region, colour):
            assigned[region] = colour

            if solve(regions):
                return True

            del assigned[region]

    return False

# Solve the CSP
regions = list(neighbors.keys())

if solve(regions):
    print("Colour Assignment:")
    for region, colour in assigned.items():
        print(region, "->", colour)
else:
    print("No solution found")