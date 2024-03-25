def greedy_algorithm(items: dict, budget: int) -> dict:
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    selected_items, total_cost, total_calories = [], 0, 0
    for item_name, item_info in sorted_items:
        if (new_cost := total_cost + item_info["cost"]) <= budget:
            selected_items.append(item_name)
            total_cost, total_calories = (
                new_cost,
                total_calories + item_info["calories"],
            )

    return {"items": selected_items, "cost": total_cost, "calories": total_calories}


def dynamic_programming(items: dict, budget: int) -> dict:
    item_list = list(items.items())
    dp_matrix = [
        [{"calories": 0, "cost": 0, "items": []} for _ in range(budget + 1)]
        for _ in range(len(items) + 1)
    ]

    for i, (name, info) in enumerate(item_list, start=1):
        for j in range(1, budget + 1):
            without_item = dp_matrix[i - 1][j]
            with_item = (
                dp_matrix[i - 1][j - info["cost"]] if j >= info["cost"] else None
            )

            if (
                with_item
                and (with_item_calories := with_item["calories"] + info["calories"])
                > without_item["calories"]
            ):
                dp_matrix[i][j] = {
                    "calories": with_item_calories,
                    "cost": with_item["cost"] + info["cost"],
                    "items": with_item["items"] + [name],
                }
            else:
                dp_matrix[i][j] = without_item

    return dp_matrix[-1][-1]


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    algos = {"Greedy": greedy_algorithm, "Dynamic": dynamic_programming}

    for budget in [40, 100, 180]:
        print(f"\n\nResults with budget: {budget}\n\n")
        for name, algo in algos.items():
            result = algo(items, budget)
            print(f"{name} Algorithm:")
            print("Selected Items:", result["items"])
            print("Total Calories:", result["calories"])
            print("Total Cost:", result["cost"], "\n")
