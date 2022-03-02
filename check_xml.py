import xml.etree.ElementTree as ET
import os
from random import sample
import shutil
import argparse

class CheckXML():
    def __init__(self):
        self.class_array = []
        self.class_dict = {}
        self.class_name_array = []
        self.copy = None

    def fix_xml(self, xml_path):
        for xml_file in os.listdir(xml_path):
            if xml_file[-4:] in ['.xml']:
                xml_name = xml_path + '' + '/' +'%s.xml' % (os.path.splitext(xml_file)[0])
                if os.path.exists(xml_name):
                    root = ET.parse(xml_name).getroot()
                    for obj in root.iter('object'):
                        class_name = obj.find('name').text
                        self.class_array.append(class_name)
                        if class_name not in self.class_name_array:
                            self.class_name_array.append(class_name)
                        if self.copy:
                            if class_name not in valid_class:
                                shutil.copy(os.path.join(xml_path, xml_file), unvalid_class_dir)
                        
    def count_object(self):
        for object in self.class_name_array:
            self.class_dict[object] = self.class_array.count(object)
        return self.class_dict


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--xml_path", required=True, help="path to your xml folder")
    ap.add_argument("-v", "--valid_classes", help="define valid classes",nargs='+')
    args = vars(ap.parse_args())

    xml_path = args['xml_path'] 

    valid_class=[]
    main = CheckXML()

    if args['valid_classes']:
        for object in args['valid_classes']:
            valid_class.append(object)
        main.copy = True    
        current_directory = os.getcwd()
        unvalid_class_dir = os.path.join(current_directory, r'unvalid_files')
        if not os.path.exists(unvalid_class_dir):
            os.makedirs(unvalid_class_dir) 
        print('All unvalid files are copied to unvalid_files folder')

    main.fix_xml(xml_path)
    print(main.count_object())