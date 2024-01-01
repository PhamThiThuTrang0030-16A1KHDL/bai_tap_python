from xml.dom import minidom

doc = minidom.parse('sample.xml')

staff_elements = doc.getElementsByTagName('staff')

for staff in staff_elements:
    name = staff.getElementsByTagName('name')[0]
    print(name.firstChild.data)
