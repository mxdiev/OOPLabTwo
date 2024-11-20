import time
from FileProcessor.FileProcessor import FileProcessor
from Statistics.Statistics import Statistics

class Application: #основной класс
    
    def __init__(self):
        self.file_processor = FileProcessor()
        self.statistics = Statistics()
    
    def run(self):
        while True:
            #ввод пути к файлу
            file_path = input("Введите путь до файла  с расширением (или '0' для завершения): ").strip()
            if file_path.lower() == "0":
                print("Завершение работы приложения.")
                break
                  
            start_time = time.time() #старт таймера
            data = self.file_processor.process_file(file_path) #получение данных в переменную data
            duplicates = self.statistics.find_duplicates(data) #поиск повторяющихся элементов
            floor_stats = self.statistics.count_buildings_by_floors(data) #подсчет домов по этажности
            end_time = time.time() - start_time #конец таймера
            
            print("\nСводная статистика:")
            print("\n1. Дублирующиеся записи:")
            for record, count in duplicates.items():
                print(f"Запись: {record}, Повторений: {count}")
            
            print("\n2. Количество зданий по этажности в каждом городе:")
            for city, floors in floor_stats.items():
                print(f"{city}: {dict(floors)}")
            
            print(f"\n3. Время выполнения задачи: {end_time:.2f} секунд\n")


if __name__ == "__main__":
    app = Application()
    app.run()
