from lxml import etree

# Load broken pom.xml
parser = etree.XMLParser(recover=True)
tree = etree.parse('pom.xml', parser)

# Write fixed and pretty pom.xml
tree.write('pom.xml', pretty_print=True, xml_declaration=True, encoding='UTF-8')
print("✅ pom.xml fixed and formatted")
