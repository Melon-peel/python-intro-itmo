import openpyxl
from datetime import datetime


class Test1Results:
    # Class attribute for the deadline
    deadline = "2024-10-28 23:59:59"

    def __init__(self, student_id, file_path="test_1.xlsx"):
        """
        Initialize with the Excel file and student ID (ИСУ).

        :param file_path: path to the .xlsx file
        :param student_id: student ID (номер ИСУ)
        """
        self.file_path = file_path
        self.student_id = student_id
        self.data = self._load_data()  # метод для загрузки данных из файла

        # your code here
        self.grade = ...  # оценка студента с номером ИСУ student_id; это сумма баллов за все 20 вопросов
        self.timestamp = ...  # время сдачи теста студента с номером ИСУ student_id
    def _load_data(self):
        """
        Load data from the Excel file using openpyxl.
        """

        data = []
        # your code here
        # дока в помощь! https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
        # и ещё можно посмотреть вот на это https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/

        # data - это список словарей, каждый из которых выглядит следующим образом:
        # {"ФИО": str, "ИСУ": int,"timestamp": datetime.datetime, "grade": int}
        # для удобства метод конвертации строки в объект типа datetime.datetime реализован за вас как статический метод класса

        return data

    @staticmethod
    def str_to_timestamp(str_):
        return datetime.strptime(str_, "%Y-%m-%d %H:%M:%S")

    def is_late(self):
        """
        Check if the student's submission was late.

        :returns: True if self.timestamp > is past the Test1Results.deadline or False otherwise
        """

        # your code here

        deadline_datetime = ...
        submission_datetime = ...

        return submission_datetime > deadline_datetime


# Пример использования
if __name__ == "__main__":
    test_results = Test1Results("test_1.xlsx", ...)  # попробуйте любой номер ИСУ из доступных в таблице

    print(f"Grade for student {test_results.student_id}: {test_results.grade}")

    is_late = test_results.is_late()
    print(f"Was the submission late? {'Yes' if is_late else 'No'}")
