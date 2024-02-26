
# План тестирования:

# Аттестационное тестирование
    - Начальное состояние: 
    - Действие: 
    - Ожидаемый результат:
        ```            
        Starting the Toyota Camry
        Engine(2000) started
        Driving the Toyota Camry
        Accelerating(2000) the engine
        Stopping the Toyota Camry
        Engine(2000) stopped
        ```                                  

# Блочные тесты

- Название класса: Engine
    - Название метода: start_engine
        - Входные данные: Ожидается объект Engine с параметром 2000.
        - Ожидаемый результат: Ожидается вывод "Engine(2000) started\n" при запуске метода start_engine().

- Название класса: Engine
    - Название метода: start_engine
        - Негативный тест
        - Входные данные: Ожидается объект Engine с параметром -150.
        - Ожидаемый результат: Ожидается вывод "Несуществующая машина\n" при запуске метода start_engine().

- Название класса: Engine
    - Название метода: accelerate
        - Входные данные: Ожидается объект Engine с параметром 2000.
        - Ожидаемый результат: Ожидается вывод "Accelerating(2000) the engine\n" при запуске метода accelerate().

- Название класса: Engine
    - Название метода: stop_engine
        - Входные данные: Ожидается объект Engine с параметром 2000.
        - Ожидаемый результат: Ожидается вывод "Engine(2000) stopped\n" при запуске метода stop_engine().


# Интеграционные тесты

- Название классов: Car, Engine
    - Название методов: start, start_engine
        - Входные данные: Ожидается объект Car с параметрами "Toyota", "Camry" и 2000.
        - Ожидаемый результат: Ожидается вывод "Starting the Toyota Camry\nEngine(2000) started\n" при запуске метода start().

- Название классов: Car, Engine
    - Название методов: drive, accelerate
        - Входные данные: Ожидается объект Car с параметрами "Toyota", "Camry" и 2000.
        - Ожидаемый результат: Ожидается вывод "Driving the Toyota Camry\nAccelerating(2000) the engine\n" при запуске метода drive().

- Название класов: Car, Engine
    - Название методов: stop, stop_engine
        - Входные данные: Ожидается объект Car с параметрами "Toyota", "Camry" и 2000.
        - Ожидаемый результат: Ожидается вывод "Stopping the Toyota Camry\nEngine(2000) stopped\n" при запуске метода stop().
