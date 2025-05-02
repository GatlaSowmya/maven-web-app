import xml.dom.minidom

# Load the existing pom.xml
with open('pom.xml', 'r') as file:
    xml_content = file.read()

# Parse and prettify (fix indentation)
dom = xml.dom.minidom.parseString(xml_content)
pretty_xml_as_string = dom.toprettyxml(indent="  ")

# Remove extra blank lines introduced by toprettyxml()
pretty_xml_lines = [line for line in pretty_xml_as_string.split('\n') if line.strip() != '']
pretty_xml_as_string = '\n'.join(pretty_xml_lines)

# Save back to pom.xml
with open('pom.xml', 'w') as file:
    file.write(pretty_xml_as_string)

print("✅ pom.xml has been auto-formatted and indentation fixed!")
