from FileProcessor.ExtensionsProcessor.CSVFileProcessor import CSVFileProcessor
from FileProcessor.ExtensionsProcessor.XMLFileProcessor import XMLFileProcessor

class FileProcessor: 
    
    def __init__(self):
        self.xml_processor = XMLFileProcessor()
        self.csv_processor = CSVFileProcessor()

    #вызов методов для xml и csv в зависимости от расширения 
    def process_file(self, file_path):
        if file_path.endswith(".xml"): #проверка последних четырех символов
            return self.xml_processor.process(file_path)
        elif file_path.endswith(".csv"):
            return self.csv_processor.process(file_path)
        else:
            raise ValueError("Неподдерживаемый формат файла. Допустимы только XML и CSV.")