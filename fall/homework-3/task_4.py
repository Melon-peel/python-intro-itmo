def calculate_distance(p1: tuple, p2: tuple) -> float:
    # квадратный корень можно посчитать как number ** 0.5
    # your code here
    return ...

def plan_route(houses):
    """Находит оптимальный маршрут для Санты."""
    if not houses:
        return "Нет домов для посещения!", 0

    # Начальная точка (Северный полюс)
    start = (0, 0)
    route = [start]
    total_distance = 0

    # Список доступных домов
    remaining_houses = houses.copy()

    current_position = start

    while remaining_houses:
        # Найти ближайший дом
        next_house = min(remaining_houses, key=lambda house: calculate_distance(current_position, house))
        # подсчет расстояния до следующего дома
        # your code here
        ...

        # добавление координат дома в маршрут и увеличение расстояния
        # your code here
        ...

    # Возврат на Северный полюс
    distance_to_pole = calculate_distance(current_position, start)
    route.append(start)
    total_distance += distance_to_pole

    return route, round(total_distance, 2)

# ---------------
# пример
houses = [(2, 3), (-1, 5), (4, -2)]
route, total_distance = plan_route(houses)
print("Дома: ", houses, end="\n\n")

route_formatted = route.copy()
route_formatted[0] = route_formatted[-1] = "Северный полюс"
route_formatted = " -> ".join([str(i) for i in route_formatted])
print("Рассчитанный маршрут:", route_formatted, end="\n\n", sep="\n")
print("Общее расстояние:", total_distance)
