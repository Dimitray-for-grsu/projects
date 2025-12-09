import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def read_users_file():
    try:
        xml_tree = ET.parse('users.xml')
        users_list = []
        for u in xml_tree.getroot().findall('user'):
            person = {
                'user_id': int(u.find('user_id').text),
                'name': u.find('name').text,
                'age': int(u.find('age').text),
                'weight': int(u.find('weight').text),
                'fitness_level': u.find('fitness_level').text,
                'workouts': []
            }
            users_list.append(person)
        return users_list
    except FileNotFoundError:
        print("Файл users.xml не найден")
        return []


def read_workouts_file():
    try:
        xml_tree = ET.parse('workouts.xml')
        workouts_list = []
        for w in xml_tree.getroot().findall('workout'):
            session = {
                'workout_id': int(w.find('workout_id').text),
                'user_id': int(w.find('user_id').text),
                'date': w.find('date').text,
                'type': w.find('type').text,
                'duration': int(w.find('duration').text),
                'distance': float(w.find('distance').text),
                'calories': int(w.find('calories').text),
                'avg_heart_rate': int(w.find('avg_heart_rate').text),
                'intensity': w.find('intensity').text
            }
            workouts_list.append(session)
        return workouts_list
    except FileNotFoundError:
        print("Файл workouts.xml не найден")
        return []


def display_overall_stats(user_data, workout_data):
    total_sessions = len(workout_data)
    total_people = len(user_data)
    burned = sum(item['calories'] for item in workout_data)
    hours_spent = sum(item['duration'] for item in workout_data) / 60.0
    sum_distance = sum(item['distance'] for item in workout_data)

    print("ОБЩАЯ СТАТИСТИКА")
    print("=" * 60)
    print(f"Всего тренировок: {total_sessions}")
    print(f"Всего пользователей: {total_people}")
    print(f"Сожжено калорий: {burned}")
    print(f"Общее время: {hours_spent:.1f} часов")
    print(f"Пройдено дистанции: {sum_distance:.1f} км")
    print()


def evaluate_user_activity(user_data, workout_data):
    for person in user_data:
        person['workouts'] = [x for x in workout_data if x['user_id'] == person['user_id']]

    summary_list = []
    for person in user_data:
        sessions = person['workouts']
        if sessions:
            entry = {
                'name': person['name'],
                'fitness_level': person['fitness_level'],
                'workouts': len(sessions),
                'calories': sum(s['calories'] for s in sessions),
                'time_hours': sum(s['duration'] for s in sessions) / 60.0
            }
            summary_list.append(entry)


    def calories_key(item):
        return item['calories']

    summary_list.sort(key=calories_key, reverse=True)

    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    counter = 1
    for record in summary_list[:3]:
        print(f"{counter}. {record['name']} ({record['fitness_level']}):")
        print(f"   Тренировок: {record['workouts']}")
        print(f"   Калорий: {record['calories']}")
        print(f"   Время: {record['time_hours']:.1f} часов")
        print()
        counter += 1

    return summary_list


def evaluate_workout_kinds(workout_data):
    kinds_dict = {}

    for session in workout_data:
        t = session['type']
        if t not in kinds_dict:
            kinds_dict[t] = {
                'count': 0,
                'total_duration': 0,
                'total_calories': 0
            }
        kinds_dict[t]['count'] += 1
        kinds_dict[t]['total_duration'] += session['duration']
        kinds_dict[t]['total_calories'] += session['calories']

    total = len(workout_data)

    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for t, info in kinds_dict.items():
        percent = info['count'] / total * 100
        avg_dur = info['total_duration'] / info['count']
        avg_cal = info['total_calories'] / info['count']

        print(f"{t}: {info['count']} тренировок ({percent:.1f}%)")
        print(f"   Средняя длительность: {avg_dur:.0f} мин")
        print(f"   Средние калории: {avg_cal:.0f} ккал")
    print()

    return kinds_dict


def search_user_workouts(user_data, user_name):
    target = None
    for p in user_data:
        if p['name'].lower() == user_name.lower():
            target = p
            break

    if target:
        return target['workouts']
    return []


def inspect_user(user_data, user_name):
    target = None
    for p in user_data:
        if p['name'].lower() == user_name.lower():
            target = p
            break

    if not target:
        print(f"Пользователь {user_name} не найден")
        return

    sessions = target['workouts']
    if not sessions:
        print(f"У пользователя {user_name} нет тренировок")
        return

    total = len(sessions)
    burned = sum(x['calories'] for x in sessions)
    hours = sum(x['duration'] for x in sessions) / 60.0
    distance = sum(x['distance'] for x in sessions)
    avg = burned / total

    type_counter = {}
    for s in sessions:
        t = s['type']
        type_counter[t] = type_counter.get(t, 0) + 1

    
    def frequency_key(item):
        return item[1]

    favorite = sorted(type_counter.items(), key=frequency_key, reverse=True)[0][0]

    print(f"ДЕТАЛЬНЫЙ АНАЛИЗ ПОЛЬЗОВАТЕЛЯ: {target['name']}")
    print("=" * 60)
    print(f"Возраст: {target['age']} лет, Вес: {target['weight']} кг")
    print(f"Уровень: {target['fitness_level']}")
    print(f"Тренировок: {total}")
    print(f"Сожжено калорий: {burned}")
    print(f"Общее время: {hours:.1f} часов")
    print(f"Пройдено дистанции: {distance:.1f} км")
    print(f"Средние калории: {avg:.0f}")
    print(f"Любимый тип тренировки: {favorite}")
    print()


def show_plots(user_data, workout_data, kinds):
    plt.figure(figsize=(15, 5))

    
    plt.subplot(1, 3, 1)
    labels = list(kinds.keys())
    values = [kinds[k]['count'] for k in labels]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Типы тренировок')

    plt.subplot(1, 3, 2)
    names = [p['name'] for p in user_data]
    calories = []
    for p in user_data:
        sessions = [w for w in workout_data if w['user_id'] == p['user_id']]
        calories.append(sum(s['calories'] for s in sessions))

    plt.bar(names, calories, color='skyblue')
    plt.title('Калории по пользователям')
    plt.xticks(rotation=45, ha='right')

    plt.subplot(1, 3, 3)
    tnames = list(kinds.keys())
    avg_vals = [kinds[k]['total_calories'] / kinds[k]['count'] for k in tnames]
    plt.bar(tnames, avg_vals, color='lightgreen')
    plt.title('Средние калории по типам')
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()

    
    plt.figure(figsize=(10, 6))

    combined = list(zip(names, calories))

    def kcal_key(item):
        return item[1]

    combined_sorted = sorted(combined, key=kcal_key, reverse=True)[:5]

    top_names = [x[0] for x in combined_sorted]
    top_values = [x[1] for x in combined_sorted]

    plt.bar(top_names, top_values)
    plt.title("ТОП-5 по калориям")

    for i, v in enumerate(top_values):
        plt.text(i, v + 50, str(v), ha='center')

    plt.tight_layout()
    plt.show()




user_storage = read_users_file()
workout_storage = read_workouts_file()

if not user_storage or not workout_storage:
    print("Ошибка загрузки данных")
else:
    for p in user_storage:
        p['workouts'] = [x for x in workout_storage if x['user_id'] == p['user_id']]

    display_overall_stats(user_storage, workout_storage)
    user_summary = evaluate_user_activity(user_storage, workout_storage)
    categories = evaluate_workout_kinds(workout_storage)

    inspect_user(user_storage, "Анна")

    print("Поиск тренировок пользователя Анна:")
    found = search_user_workouts(user_storage, "Анна")
    print(f"Найдено тренировок: {len(found)}\n")

    show_plots(user_storage, workout_storage, categories)
