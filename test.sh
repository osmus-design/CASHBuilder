#!/bin/bash

# Найти все файлы, соответствующие шаблону *.test.py
test_files=$(find . -type f -name "*.test.py")

# Проверить, найдены ли файлы
if [ -z "$test_files" ]; then
    echo "Нет файлов с тестами, соответствующих шаблону *.test.py"
    exit 1
fi

# Перебрать все найденные файлы и запустить тесты
for test_file in $test_files; do
    echo "Запуск тестов в файле: $test_file"
    python -m unittest $test_file
    if [ $? -ne 0 ]; then
        echo "Тесты в файле $test_file завершились с ошибкой"
        exit 1
    fi
done

echo "Все тесты успешно завершены"