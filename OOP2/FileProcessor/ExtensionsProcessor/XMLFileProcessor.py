import xml.etree.ElementTree as ET

class XMLFileProcessor: #обработка XML файла
    
    def process(self, file_path):
        data = []
        tree = ET.parse(file_path)
        root = tree.getroot()
        #добавление элементов к дереву
        for item in root.findall("item"):
            data.append({
                "city": item.get("city"),
                "street": item.get("street"),
                "house": int(item.get("house")),
                "floor": int(item.get("floor"))
            })
        return data