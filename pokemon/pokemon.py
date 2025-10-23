import random
try:
    pokemon = []
    all_pokemon_f = open("pokemon.txt")
    all_pokemon = all_pokemon_f.readlines()
    for line in all_pokemon:
        if line.startswith("Number"):
            continue
        number, name = line.strip().split(",")
        pokemon.append((int(number), name))

    completed_pokemon_f = open("completed_pokemon.txt", "a+")
    completed_pokemon = completed_pokemon_f.readlines()
    for line in completed_pokemon:
        number, name = line.strip().split(",")
        pokemon.remove((int(number), name))

    pokemon = random.sample(pokemon, len(pokemon))
    for number, name in pokemon:
        input(f"#{number:03d}: {name}")
        completed_pokemon_f.write(f"{number:03d},{name}\n")
finally:
    all_pokemon_f.close()
    completed_pokemon_f.close()