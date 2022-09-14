from inventory_report.importer.importer import Importer
from xml.etree import ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        type = path.split(".")[1]
        if type == "xml":
            tree = ET.parse(path)
            root = tree.getroot()
            return [
                {child.tag: child.text for child in tags}
                for tags in root.findall("record")
            ]
        else:
            raise ValueError("Arquivo inválido")
