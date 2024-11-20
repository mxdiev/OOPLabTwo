from collections import defaultdict, Counter
#используем модифицированный словарь defaultdict и счетчик количества повторений Counter.

class Statistics: #вычисление статистики
    
    def find_duplicates(self, data):
        counter = Counter((d["city"], d["street"], d["house"], d["floor"]) for d in data)
        duplicates = {i: j for i, j in counter.items() if j > 1}
        return duplicates


    
    def count_buildings_by_floors(self, data):
        #лямбда-функция для инициализации словаря
        city_stats = defaultdict(lambda: defaultdict(int))
        for record in data:
            city = record["city"]
            floor = record["floor"]
            city_stats[city][floor] += 1
        return city_stats
