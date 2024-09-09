class NumberList:
    """Класс для работы со списком чисел."""
    
    def __init__(self, numbers):
        """Инициализация класса с заданным списком чисел."""
        self.numbers = numbers

    def calculate_average(self):
        """Вычисляет среднее значение чисел в списке."""
        return sum(self.numbers) / len(self.numbers)

class AverageComparator:
    """Класс для сравнения средних значений двух списков."""
    
    def __init__(self, list1, list2):
        """Инициализация класса с двумя списками."""
        self.list1 = NumberList(list1)  # Создание экземпляра NumberList для первого списка
        self.list2 = NumberList(list2)  # Создание экземпляра NumberList для второго списка

    def compare_averages(self):
        """Сравнивает средние значения двух списков и возвращает результат."""
        avg1 = self.list1.calculate_average()  # Вычисление среднего первого списка
        avg2 = self.list2.calculate_average()  # Вычисление среднего второго списка

        # Сравнение средних значений и возврат соответствующего сообщения
        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"

def get_list_from_input(prompt):
    """Получает список чисел от пользователя через ввод с клавиатуры."""
    return list(map(int, input(prompt).split()))  # Преобразует ввод в список целых чисел

# Получение списков от пользователя
list1 = get_list_from_input("Введите числа для первого списка, разделенные пробелом: ")
list2 = get_list_from_input("Введите числа для второго списка, разделенные пробелом: ")

# Создание экземпляра AverageComparator и вывод результата сравнения
comparator = AverageComparator(list1, list2)
print(comparator.compare_averages())
