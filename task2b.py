# Minimum colour set
colours = ["Red", "Green", "Blue", "Yellow"]

# Approximate neighbouring relationships
neighbors = {
    "Westlands": ["Dagoretti North", "Starehe", "Roysambu"],
    "Dagoretti North": ["Westlands", "Dagoretti South"],
    "Dagoretti South": ["Dagoretti North", "Langata"],
    "Langata": ["Dagoretti South", "Kibra", "Embakasi South"],
    "Kibra": ["Langata", "Starehe"],
    "Roysambu": ["Westlands", "Kasarani"],
    "Kasarani": ["Roysambu", "Ruaraka", "Mathare"],
    "Ruaraka": ["Kasarani", "Mathare", "Starehe"],
    "Embakasi South": ["Langata", "Embakasi East", "Embakasi West"],
    "Embakasi North": ["Embakasi Central", "Ruaraka"],
    "Embakasi Central": ["Embakasi North", "Embakasi East"],
    "Embakasi East": ["Embakasi Central", "Embakasi South"],
    "Embakasi West": ["Embakasi South", "Makadara"],
    "Makadara": ["Embakasi West", "Kamukunji"],
    "Kamukunji": ["Makadara", "Starehe"],
    "Starehe": ["Westlands", "Kamukunji", "Kibra", "Ruaraka"],
    "Mathare": ["Kasarani", "Ruaraka"]
}

assigned = {}

# Check validity
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

regions = list(neighbors.keys())

if solve(regions):
    print("Nairobi Sub-County Colouring:")
    for region, colour in assigned.items():
        print(region, "->", colour)
else:
    print("No solution found")