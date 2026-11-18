import numpy as np
from numpy.typing import NDArray

def conditional(a: NDArray[np.bool_], b: NDArray[np.bool_]) -> float:
    return np.mean(a[b])

# Tea and Coffee Probabilities
rng = np.random.default_rng(0)
n = 200_000
like_tea = rng.random(n) < 120/200
coffee_given_tea = rng.random(n) < 80/120
coffee_given_non_tea = rng.random(n) < 30/80
like_coffee = np.where(like_tea, coffee_given_tea, coffee_given_non_tea)
print(f"P(Coffee) = {np.mean(like_coffee):.2f}")                  # 0.55
print(f"P(Coffee | Tea) = {conditional(like_coffee, like_tea):.2f}")   # 0.67
print(f"P(Tea | Coffee) = {conditional(like_tea, like_coffee):.2f}")  # 0.73

# Dog Owner and Daily Walks Probabilities
n = 100_000
own_dog = rng.random(n) < 3/10
daily_walks_given_dog = rng.random(n) < 5/6
daily_walks_given_no_dog = rng.random(n) < 3/7
daily_walks = np.where(own_dog, daily_walks_given_dog, daily_walks_given_no_dog)
print(f"P(Walks) = {np.mean(daily_walks):.2f}")                      # 0.55
print(f"P(Dog) = {np.mean(own_dog):.2f}")                            # 0.30
print(f"P(Walks | Dog) = {conditional(daily_walks, own_dog):.2f}")   # 0.83
print(f"P(Dog | Walks) = {conditional(own_dog, daily_walks):.2f}")   # 0.45
# P(Walks) = 0.55 but P(Walks | Dog) = 0.83, so knowing someone owns a dog changes
# the chance they walk daily. The traits are not independent: dog owners walk more.