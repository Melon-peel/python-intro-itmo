# Домашнее задание №2

## Формат сдачи

--To be specified--

Под каждое задание отведен отдельный файл (например, `task_1.py` для задания №1).
Используйте заготовки внутри этих файлов для своего решения


## Дедлайн и алгоритм оценивания

**Жёсткий дедлайн**
31.12.2024 23:59

**Максимальный балл:** 16 баллов


# Задачи

## Задача 1. Чаепитие (4 балла)

Вам нужно реализовать набор классов для симуляции взаимодействия с чашкой чая.

### Класс `Sugar` (1 балл)

- Конструктор принимает единственный аргумент kind, который может принимать значения: "brown" или "white"
- Если при создании объектов класса Sugar был передан некорректный тип сахара, должно вызываться исключение ValueError с текстом "Invalid sugar type" 
- Реализуйте в классе Sugar статический метод `_validate_kind`, который бы вызывался внутри конструктора для проверки типа сахара

### Класс `Tea` (1 балл)

- Конструктор принимает единственный аргумент kind, который может принимать значения: "black" или "green"
- Если при создании объектов класса Tea был передан некорректный тип сахара, должно вызываться исключение ValueError с текстом "Invalid tea type" 
- Реализуйте в классе Tea статический метод `_validate_kind`, который бы вызывался внутри конструктора для проверки типа чая

### Класс `TeaCup` (2 балла)
#### Налить/вылить (1 балл) 

- Конструктор класса уже реализован в `task_1.py`
- Метод `pour_water(amount=None)`:
  - Если amount не указан, чашка должна быть полностью заполнена (уровень fullness становится равен 1).
  - Если amount указан, он должен быть float в диапазоне [0; 1] и добавлять указанное количество к текущему уровню fullness.
  - Если в результате выполнения метода уровень fullness превышает 1, должно выбрасываться исключение BaseTeaException с текстом "Attempt to pour too much water".

- Метод `drink(amount=None)`:
  - Если amount не указан, содержимое чашки должно быть выпито полностью (уровень fullness становится равен 0).
  - Если amount указан, он должен быть float в диапазоне [0; 1] и уменьшать уровень fullness.
  - Если в результате выполнения метода уровень fullness становится меньше 0, должно выбрасываться исключение BaseTeaException с текстом "Attempt to drink beyond available amount".

- Метод `is_full()`
  - Возвращает True, если fullness == 1, иначе False.

**Важно**. 
- Для методов `drink` и `pour_water` исключения вызываются до изменения значения атрибута объекта
- Когда весь чай выпивается методом drink (т.е. fullness=0), все атрибуты возвращаются к значениям по умолчанию (fullness -> 0, sweetness -> 0, tea -> None)

#### Добавление сахара/чая (1 балл)

- Перегрузка оператора сложения (+):
  - Объекты класса TeaCup должны поддерживать добавление сахара (Sugar) или чая (Tea) через сложение
  - При добавлении сахара увеличивает `self.sweetness` на 1. 
  - При добавлении чая присваивает атрибуту `tea` значение `kind` чая. Будем считать, что, если чай уже был добавлен, каждое новое добавление просто ведёт к перезаписи старого значения 
  - При попытке выполнить сложение с объектами неподходящих типов должно вызываться исключение `TypeError` с текстом "Can only add Sugar or Tea to a TeaCup"

- Перегрузка оператора вычитания (+):
  - Объекты класса TeaCup должны поддерживать удаление сахара (Sugar) через вычитание
  - При удалении сахара уменьшает self.sweetness на 1.
  - При попытке выполнить вычитание с объектами неподходящих типов должно вызываться исключение `TypeError` с текстом "Can only subtract Sugar from TeaCup"
  - При попытке удалить из чашки такое количество сахара, которое бы привело к self.sweetness < 0 вызывается исключение `ValueError` с текстом "Amount of sugar can't be negative"  

---

## Задача 2. Парсер конфига (4 балла)

Необходимо реализовать класс `CustomConfigParser`, который будет служить парсером конфигурационных файлов формата .configus (позже мы ещё вернёмся к теме чтения/записи конфигов)\ 
Класс должен обеспечивать чтение, модификацию, удаление и запись конфигурационных данных. 

Каждый файл конфигурации состоит из секций, заголовки которых записаны в квадратных скобках `[SectionName]`, и набора пар ключ-значение внутри секций (`key = value`). Вот пример содержания такого файла:

```
[server]
host = localhost
port = 8080
ssl = false

[empty section]

[database]
name = mydb
username = myuser
password = mypassword
```
__Как устроен данный формат (что считается валидным и как происходит обработка)__:
- Заголовок [a.k.a. название секции] (текст внутри квадратных скобок) может быть любой строкой из [A-z ] (латиница в любом регистре и пробельный символ)
- Секция может быть пустой (как в примере выше)
- Ключи быть любой строкой из [A-z0-9] (латиница в любом регистре, цифры от 0 до 9)
- Значения могут быть любыми символами, кроме знака равно (т.е. запись вида `key = value value` валидна)
- Пары ключ-значение идут сразу после заголовков (т.е. на следующей же строчке)
- Пустая строка перед заголовком обязательна

__Класс должен быть способен выполнять следующие операции__:
- Чтение конфигурационного файла (формат .configus) и преобразование его в словарь.
- Получение, установка, удаление значений.
- Добавление и удаление секций.
- Запись конфигурационных данных в файл.

С точки зрения реализации это означает, что у класса должны быть реализованы следующие методы:
- `__init__` (реализацию смотри в шаблоне внутри `task_2.py`)
- `read(self, filepath)`, который:
  - принимает на вход путь до файла и считывает его, записывая содержимое внутрь self._config
  - если файл не найден, должно вызываться исключение `FileNotFoundError` с текстом "File X not found", где X - указанный путь до файла 
  - если возникли проблемы при чтении конфига, должно вызываться исключение ValueError(f"Invalid line in config file: {line}"), где line - это строчка, при парсинге которой возникли проблемы
- `get(self, section, key)`, который ведёт себя как метод `get` у словарей в Python:
  - проверяет существование секции и ключа
  - возвращает значение ключа, если оно найдено
  - бросает исключение KeyError, если секция или ключ отсутствуют.
- `set(self, section, key, value)`, который устанавливает или обновляет пару ключ-значение в указанной секции:
  - если секция отсутствует, она создаётся, и в неё добавляются пары ключ-значение
  - обновляет значение ключа (при его наличии) или добавляет его в указанную секцию
- `add_section(self, section)`, который добавляет новую (пустую) секцию
- `remove_section(self, section)`:
  - удаляет указанную секцию из конфигурации (при наличии)
  - бросает исключение KeyError, если секция отсутствует
- `remove_option(self, section, key)`:
  - удаляет ключ-значение, если секция и ключ существуют
  - бросает исключение KeyError, если секция или ключ отсутствуют
- `write(self, filepath)`:
  - форматирует данные _config под требуемый формат .configus
  - записывает каждую секцию и её содержимое:
    - заголовок секции в квадратных скобках [SectionName]
    - пары ключ-значение (key = value)
    - пустую строку после каждой секции

---

## Задача 3. Сжатие JPEG-изображений

В этом задании вам необходимо реализовать класс `JPEGCompressor`, предназначенный для сжатия JPEG-изображений с использованием библиотеки `Pillow`.

Этот класс должен включать методы для загрузки, сжатия и сохранения изображения. Ниже представлены требования к функциональности каждого метода.

__Описание класса__ (шаблон класса можно найти в `task_3.py`)

- `__init__(self)` (1 балл)
  - инициализирует объект класса, задавая атрибут для хранения изображения (`image`) и уровень качества (`quality`) 
  - изначально изображение не загружено, и атрибут `image` должен быть равен `None`
  - качество изображения по умолчанию должно отвечать отсутствию сжатия (`quality = 100`)
- `load(self, filepath)` - метод для загрузки изображения (1 балл)
  - аргумент `filepath` (str) - путь к изображению в формате JPEG
  - в методе должна быть реализована проверка существования файла по указанному пути. Если файл не существует, выбросить `FileNotFoundError`.
  - далее происходит попытка открыть файл с помощью библиотеки `Pillow` 
    - если файл не является изображением или его формат отличается от JPEG, выбросить `TypeError`.
    - если изображение успешно загружено, сохранить его в атрибуте объекта
- `compress(self, quality)` - метод для установки уровня сжатия для изображения (1 балл)
  - аргумент `quality` (int) отвечает за степень сохранения исходного качества изображения (от `0` до `95`), где `0` — максимальное сжатие, `95` — максимальное.
  - метод должен проверять, что изображение загружено. Если изображение отсутствует, выбросить `FileNotFoundError`
  - метод должен проверять, что уровень сжатия находится в диапазоне от `0` до `95`. Если значение выходит за пределы диапазона, выбросить `ValueError`
  - метод устанавливает уровень сжатия (`self.quality`) согласно переданному аргументу. Сам процесс сжатия должен находиться в методе `save`

**Прим.** 95 не случайно является максимальным уровнем качества (смотри quality в [документации](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg))

- `save(self, file_path)` - сохранение изображения с заданным уровнем сжатия в файл 
  - аргумент `filepath` (str) - путь для сохранения изображения
  - метод должен проверять, что изображение загружено. Если изображение отсутствует, выбросить `FileNotFoundError`
  - метод сохраняет изображение в формате JPEG с применением ранее установленного уровня сжатия (детали смотри в `task_3.py`)

---

## Задача 4. Анализ результатов теста (4 балла)


Вам предстоит реализовать класс `Test1Results`, который позволит работать с Excel-файлом, содержащим оценки за ваш первый тест.
Для выполнения задания вам нужно установить стороннюю библиотеку Openpyxl, запустив:

```pip install openpyxl``` у себя в терминале/командной строке

Класс должен обеспечивать следующие возможности:

- Инициализация экземпляра класса, при которой выполняется:
  - загрузка данных из excel-файла
  - подсчет финальной оценки
  - извлечение временной метки сдачи (timestamp)
- Возможность вызова метода `is_late`, отвечающего за проверку того, был ли тест отправлен после дедлайна
   
Шаблон для вашего решения находится в файле `task_4.py`

**Примечание**. Использовать библиотеку `pandas` нельзя.