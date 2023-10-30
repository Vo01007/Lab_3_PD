import os
import csv

# Указать путь к корневой директории датасета
dataset_root = 'D:\\LABS\\Lab_PD\\Lab 2\\dataset'
project_root = 'D:\\LABS\\Lab_PD\\Lab 3'

# Создать\\открыть файл аннотации
with open('annotations.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['D:\\LABS\\Lab_PD\\Lab 2\\dataset', '..\\lab_2\\dataset', 'polar_bear'])

    for root, dirs, files in os.walk(dataset_root):
        for file in files:
            if file.endswith('.jpg'):
                absolute_path = os.path.join(root, file)
                relative_path = os.path.relpath(absolute_path, project_root)
                label = os.path.basename(root)
                writer.writerow([absolute_path, relative_path, label])