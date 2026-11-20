import numpy as np
import matplotlib.pyplot as plt

def update(prior: float, likelihood_if_true: float, likelihood_if_false: float, evidence_seen: bool) -> float:
    if not evidence_seen:
        likelihood_if_true = 1 - likelihood_if_true
        likelihood_if_false = 1 - likelihood_if_false
    evidence = (likelihood_if_true * prior) + (likelihood_if_false * (1 - prior))
    return (likelihood_if_true * prior) / evidence

def show_chart(min_prevalence: float, max_prevalence: float, how_many: int, likelihood_if_true: float, likelihood_if_false: float) -> None:
    belief_list: list[float] = []
    prevalence = np.linspace(min_prevalence, max_prevalence, how_many)
    for value in prevalence:
        p_sick = update(value, likelihood_if_true, likelihood_if_false, True)
        belief_list.append(p_sick)
    plt.plot(prevalence, belief_list)
    plt.xlabel("Prevalence"); plt.ylabel("P(Sick | Positive)")
    plt.show()

prior = 0.02
results = [True, True, False, True, True]
number_of_tests: list[int] = [0]
belief_list: list[float] = [prior]
print(f"Before tests: {prior}")
for i, result in enumerate(results):
    prior = update(prior, 0.9, 0.1, result)
    belief_list.append(prior)
    number_of_tests.append(i + 1)
    print(f"After test {i+1} ({'positive' if result else 'negative'}): {prior:.2f}")
plt.plot(number_of_tests, belief_list)
plt.xlabel("Number of tests"); plt.ylabel("Probability of being sick")
plt.show()

show_chart(0.001, 0.5, 200, 0.9, 0.1)