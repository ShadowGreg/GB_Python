import random as rnd


def generate_list(start: int, end: int, volume: int = 10) -> list:
    quantity = rnd.randrange(start, end)
    output_data = []
    for _ in range(quantity + 1):
        output_data.append(rnd.randrange(volume))
    return output_data


def generate_float(start: int, end: int, volume: int = 10) -> list:
    quantity = rnd.randrange(start, end)
    output_data = []
    for _ in range(quantity + 1):
        output_data.append(round((volume - float(rnd.randrange(volume)) / (1 + rnd.randrange(volume))), 2))
    return output_data
