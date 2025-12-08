import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def load_users_data():

    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
                'user_id': int(user_elem.find('user_id').text),
                'name': user_elem.find('name').text,
                'age': int(user_elem.find('age').text),
                'weight': int(user_elem.find('weight').text),
                'fitness_level': user_elem.find('fitness_level').text,
                'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл users.xml не найден")
        return []


def load_workouts_data():

    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id': int(workout_elem.find('user_id').text),
                'date': workout_elem.find('date').text,
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': float(workout_elem.find('distance').text),
                'calories': int(workout_elem.find('calories').text),
                'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
                'intensity': workout_elem.find('intensity').text
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл workouts.xml не найден")
        return []


def get_stats(users, workouts):

    total_workouts = len(workouts)
    total_users = len(users)
    total_calories = sum(workout['calories'] for workout in workouts)
    total_time_hours = sum(workout['duration'] for workout in workouts) / 60.0
    total_distance = sum(workout['distance'] for workout in workouts)

    print("ОБЩАЯ СТАТИСТИКА")
    print("=" * 60)
    print(f"Всего тренировок: {total_workouts}")
    print(f"Всего пользователей: {total_users}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time_hours:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
    print()


def analyze_user_activity(users, workouts):

    for user in users:
        user['workouts'] = [w for w in workouts if w['user_id'] == user['user_id']]

    user_stats = []
    for user in users:
        user_workouts = user['workouts']
        if user_workouts:
            total_workouts = len(user_workouts)
            total_calories = sum(w['calories'] for w in user_workouts)
            total_time = sum(w['duration'] for w in user_workouts) / 60.0
            user_stats.append({
                'name': user['name'],
                'fitness_level': user['fitness_level'],
                'workouts': total_workouts,
                'calories': total_calories,
                'time_hours': total_time
            })

    user_stats.sort(key=lambda x: x['calories'], reverse=True)

    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i, stat in enumerate(user_stats[:3], 1):
        print(f"{i}. {stat['name']} ({stat['fitness_level']}):")
        print(f"   Тренировок: {stat['workouts']}")
        print(f"   Калорий: {stat['calories']}")
        print(f"   Время: {stat['time_hours']:.1f} часов")
        print()

    return user_stats


def analyze_workout_types(workouts):

    workout_types = {}
    for workout in workouts:
        workout_type = workout['type']
        if workout_type not in workout_types:
            workout_types[workout_type] = {
                'count': 0,
                'total_duration': 0,
                'total_calories': 0
            }
        workout_types[workout_type]['count'] += 1
        workout_types[workout_type]['total_duration'] += workout['duration']
        workout_types[workout_type]['total_calories'] += workout['calories']

    total_workouts = len(workouts)

    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for workout_type, stats in workout_types.items():
        percentage = (stats['count'] / total_workouts) * 100
        avg_duration = stats['total_duration'] / stats['count']
        avg_calories = stats['total_calories'] / stats['count']

        print(f"{workout_type}: {stats['count']} тренировок ({percentage:.1f}%)")
        print(f"   Средняя длительность: {avg_duration:.0f} мин")
        print(f"   Средние калории: {avg_calories:.0f} ккал")

    print()
    return workout_types


def find_user_workouts(users, user_name):

    user = next((u for u in users if u['name'].lower() == user_name.lower()), None)
    if user:
        return user['workouts']
    return []


def analyze_user(users, user_name, workouts):

    user = next((u for u in users if u['name'].lower() == user_name.lower()), None)
    if not user:
        print(f"Пользователь {user_name} не найден")
        return

    user_workouts = user['workouts']
    if not user_workouts:
        print(f"У пользователя {user_name} нет тренировок")
        return

    total_workouts = len(user_workouts)
    total_calories = sum(w['calories'] for w in user_workouts)
    total_time = sum(w['duration'] for w in user_workouts) / 60.0
    total_distance = sum(w['distance'] for w in user_workouts)
    avg_calories_per_workout = total_calories / total_workouts

    type_counts = {}
    for workout in user_workouts:
        workout_type = workout['type']
        type_counts[workout_type] = type_counts.get(workout_type, 0) + 1

    favorite_type = max(type_counts, key=type_counts.get)

    print(f"ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user['name']}")
    print("=" * 60)
    print(f"Возраст: {user['age']} лет, Вес: {user['weight']} кг")
    print(f"Уровень: {user['fitness_level']}")
    print(f"Тренировок: {total_workouts}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
    print(f"Средние калории за тренировку: {avg_calories_per_workout:.0f}")
    print(f"Любимый тип тренировки: {favorite_type}")
    print()


def visualize_data(users, workouts, workout_types):

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    labels = list(workout_types.keys())
    sizes = [workout_types[type_]['count'] for type_ in labels]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Распределение по типам тренировок')

    plt.subplot(1, 3, 2)
    user_names = [user['name'] for user in users]
    user_calories = []
    for user in users:
        user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]
        user_calories.append(sum(w['calories'] for w in user_workouts))

    plt.bar(user_names, user_calories, color='skyblue')
    plt.title('Активность пользователей по калориям')
    plt.xlabel('Пользователи')
    plt.ylabel('Калории')
    plt.xticks(rotation=45, ha='right')

    plt.subplot(1, 3, 3)
    type_names = list(workout_types.keys())
    type_avg_calories = [workout_types[type_]['total_calories'] / workout_types[type_]['count']
                         for type_ in type_names]

    plt.bar(type_names, type_avg_calories, color='lightgreen')
    plt.title('Эффективность тренировок по типам')
    plt.xlabel('Тип тренировки')
    plt.ylabel('Средние калории')
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))

    user_calories_sorted = sorted(zip(user_names, user_calories),
                                  key=lambda x: x[1], reverse=True)[:5]

    sorted_names, sorted_calories = zip(*user_calories_sorted)

    plt.bar(sorted_names, sorted_calories, color=['gold', 'silver', 'brown', 'skyblue', 'lightgreen'])
    plt.title('Сравнение пользователей по общим затраченным калориям (ТОП-5)')
    plt.xlabel('Пользователи')
    plt.ylabel('Калории')

    for i, v in enumerate(sorted_calories):
        plt.text(i, v + 50, str(v), ha='center')

    plt.tight_layout()
    plt.show()


def main():
    users = load_users_data()
    workouts = load_workouts_data()

    if not users or not workouts:
        print("Ошибка загрузки данных. Проверьте наличие файлов users.xml и workouts.xml")
        return

    for user in users:
        user['workouts'] = [w for w in workouts if w['user_id'] == user['user_id']]

    get_stats(users, workouts)

    user_stats = analyze_user_activity(users, workouts)

    workout_types = analyze_workout_types(workouts)

    analyze_user(users, "Анна", workouts)

    print("Поиск тренировок пользователя 'Анна':")
    anna_workouts = find_user_workouts(users, "Анна")
    print(f"Найдено {len(anna_workouts)} тренировок")
    print()

    visualize_data(users, workouts, workout_types)

if __name__ == "__main__":
    main()
