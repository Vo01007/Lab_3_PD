import os
import random
import shutil

# Путь к исходному датасету
source_directory = 'D:\\LABS\\Lab_PD\\Lab 2\\dataset'
classes = ["polar_bear", "brown_bear"]
# Путь к новой копии датасета
target_directory = 'D:\\LABS\\Lab_PD\\Lab 3\\datasetL3_1'

# Создаем новую директорию для копии датасета
os.makedirs(target_directory, exist_ok=True)

# Получаем список файлов из исходного датасета


for class_name in classes:
    class_source_directory = os.path.join(source_directory, class_name)
    files = os.listdir(class_source_directory)
    for filename in files:
        # Генерируем случайный номер от 0 до 10000
        random_number = random.randint(0, 10000)
        
        # Создаем новое имя файла
        new_filename = os.path.join(target_directory, f"{random_number}.jpg")
        
        # Копируем файл с новым именем
        shutil.copy(os.path.join(class_source_directory ,filename), new_filename)
