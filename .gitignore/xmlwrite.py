from xml.dom import minidom

doc = minidom.Document()

root = doc.createElement('html')
doc.appendChild(root)

leaf = doc.createElement('head')
script = doc.createElement('script')
leaf.appendChild(script)

style=doc.createElement('style')
leaf.appendChild(style)
root.appendChild(leaf)
leaf = doc.createElement('body')
div=doc.createElement('div')
para=doc.createElement('p')
div.appendChild(para)
leaf.appendChild(div)
root.appendChild(leaf)
xml_str = doc.toprettyxml(indent="  ")
with open("Sample.xml", "w") as f:
    f.write(xml_str)