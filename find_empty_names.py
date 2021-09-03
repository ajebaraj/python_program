import os
import xml.etree.ElementTree as ET

path = 'C:\\Users\\jebar\\OneDrive\\Desktop\\indo_auto_data\\blister\\'


def empty_names(path):
	files = os.listdir(path)
	for file in files:
		if file.endswith('.xml'):
			tree = ET.parse(path+file)
			root = tree.getroot()
			l = [elt.tag for elt in root.iter()]
			if 'name' not in l:
				print(path+file)
				# os.remove(path+file)

				# sp = file.split('.')
				# print(path+sp[0]+'.'+sp[1]+'.jpg')
				# os.remove(path+sp[0]+'.'+sp[1]+'.jpg')
				# print(path+file.split('.')[0]+'.jpg')
					

empty_names(path)