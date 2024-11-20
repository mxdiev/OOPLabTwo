import csv

class CSVFileProcessor: #обработка CSV файла
    
    def process(self, file_path):
        data = []
        csvfile = open(file_path, newline='', encoding='utf-8')
        reader = csv.DictReader(csvfile, delimiter=';')
             
        for row in reader:
            data.append({
                "city": row["city"],
                "street": row["street"],
                "house": int(row["house"]),
                "floor": int(row["floor"])
             })
        return data