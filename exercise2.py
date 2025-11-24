# 1. List of 10 delivery routes
routes = [
    "Nairobi-Westlands",
    "Nakuru-Lanet",
    "Nyeri-Karatina",
    "Mombasa-Nyali",
    "Kisumu-Milimani",
    "Eldoret-Iten",
    "Naivasha-MaiMahiu",
    "Nanyuki-Timau",
    "Thika-Ruiru",
    "Garissa-Dadaab"
]

print("Original Routes:", routes)

# 2. Append & Remove
routes.append("Kitale-Kapenguria")
routes.remove("Garissa-Dadaab")
print("\nAfter Append & Remove:", routes)

# 3. Sort and Reverse
routes.sort()
routes.reverse()
print("\nSorted & Reversed:", routes)

# 4. Count routes starting with 'N'
count_N = sum(route.startswith("N") for route in routes)
print("\nRoutes starting with 'N':", count_N)

# 5. List comprehension: routes > 10 characters
long_routes = [r for r in routes if len(r) > 10]
print("\nRoutes longer than 10 characters:", long_routes)
