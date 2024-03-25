import random
import matplotlib.pyplot as plt
from collections import defaultdict
from tabulate import tabulate


MATH_PROB = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}


def simulate_dice_rolls(num: int):
    results = defaultdict(int)

    for _ in range(num):
        roll = random.randint(1, 6) + random.randint(1, 6)
        results[roll] += 1

    return {key: value / num for key, value in results.items()}


def plot_probabilities(prob: dict) -> None:
    x_values, y_values = zip(*sorted(prob.items()))

    plt.figure(figsize=(10, 6))
    plt.bar(x_values, y_values, color="skyblue")
    plt.xticks(range(2, 13))
    plt.xlabel("Total Dice Value")
    plt.ylabel("Probability")
    plt.title("Probability Distribution of Dice Roll Sums")
    plt.grid(axis="y", linestyle="--")
    plt.show()


if __name__ == "__main__":
    num = 1000000
    probabilities = simulate_dice_rolls(num)

    data = []
    for total in range(2, 13):
        probability = probabilities.get(total, 0) * 100
        data.append([total, probability, MATH_PROB[total]])

    print(
        tabulate(
            data,
            headers=["Total", "Монте-Карло (%)", "Probability (%)"],
            tablefmt="pipe",
        )
    )
    plot_probabilities(probabilities)
