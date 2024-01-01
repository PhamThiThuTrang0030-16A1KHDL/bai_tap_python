import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse('sample.xml')
    root = doc.documentElement
    print(root.tagName)
    children = root.childNodes
    for child in children:
        if child.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            print(child.tagName)

if __name__ == '__main__':
    main()
