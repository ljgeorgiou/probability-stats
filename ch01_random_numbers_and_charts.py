import numpy as np

rng = np.random.default_rng(seed=42)

def estimate(event_function, n: int) -> float:
    rolls = rng.integers(1, 7, size=n)
    return np.mean(event_function(rolls))

print(f"even: {estimate((lambda rolls: rolls % 2 == 0), 10_000)}")
print(f"greater than 4: {estimate((lambda rolls: rolls > 4), 10_000)}")
print("a six:")
for n in [10, 100, 1000, 10_000, 100_000]:
    print(f"n = {n}: {estimate((lambda rolls: rolls == 6), n)}")
print("As the number of dice rolls increases, the fraction of rolls that land on 6 settles towards 0.1667")