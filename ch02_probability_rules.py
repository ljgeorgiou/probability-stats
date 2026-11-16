import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=0)

# Dice Rolling
rolls = rng.integers(1, 7, 200_000)
print(f"5 or 6: {np.mean((rolls == 5) | (rolls == 6))}")
print(f"not a 1: {np.mean(rolls > 1)}")
print(f"odd or greater than 3: {np.mean((rolls % 2 == 1) | (rolls > 3))}")

# Coin Flip
first = rng.random(200_000) < 0.5
second = rng.random(200_000) < 0.5
third = rng.random(200_000) < 0.5
print(f"at least one head: {np.mean(first | second)}")
print(f"three heads: {np.mean(first & second & third)}")

# Drawing 2 Cards from a 52-card deck
first_draw = rng.integers(0, 52, 200_000)
second_draw = rng.integers(0, 52, 200_000)
print(f"both aces, putting the first back: {np.mean((first_draw < 4) & (second_draw < 4))}")

both_aces = 0
for _ in range(200_000):
    picks = rng.choice(52, size=2, replace=False)
    if picks[0] < 4 and picks[1] < 4:
        both_aces += 1
print(f"both aces, keeping the first out: {both_aces / 200_000}")

# Birthday Problem
def shared_birthday_probability(room_size: int, trials: int = 20_000) -> float:
    matches: int = 0
    for _ in range(trials):
        room = rng.integers(0, 365, size=room_size)
        if len(np.unique(room)) < room_size:
            matches += 1
    return matches / trials

print(f"For a room of 23 people, the probability of at least one shared birthday is {shared_birthday_probability(23)}")

probabilities: list[float] = []
room_size_list: list[int] = list(range(5, 61))
smallest_room_half: int | None = None
smallest_room_nearly_1: int | None = None
for size in room_size_list:
    matches_probability = shared_birthday_probability(size)
    probabilities.append(matches_probability)
    if matches_probability >= 0.5 and smallest_room_half is None:
        smallest_room_half = size
    if matches_probability >= 0.99 and smallest_room_nearly_1 is None:
        smallest_room_nearly_1 = size
print(f"Smallest room where the probability passes 0.5: {smallest_room_half}")
print(f"Smallest room where the probability passes 0.99: {smallest_room_nearly_1}")
plt.plot(room_size_list, probabilities)
plt.xlabel("Room Size")
plt.ylabel("Probability of Shared Birthday")
plt.title("Birthday Problem")
plt.show()