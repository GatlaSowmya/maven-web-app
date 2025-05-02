from lxml import etree

def clean_pom(pom_path):
    try:
        tree = etree.parse(pom_path)

        # Ensure that there are no extra newline characters or broken tags
        for elem in tree.iter():
            if elem.tail:
                # Remove extra whitespace characters (newlines and tabs)
                elem.tail = elem.tail.strip()

        # Write the cleaned XML back to the file
        tree.write(pom_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        print("✅ pom.xml cleaned and formatted successfully")
    except etree.XMLSyntaxError as e:
        print(f"❌ Error cleaning pom.xml: {e}")

# Call the clean_pom function to clean the POM file
clean_pom('pom.xml')
