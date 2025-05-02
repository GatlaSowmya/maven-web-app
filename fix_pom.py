import re

def fix_pom_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Fix common HTML entities like &gt; and replace them
    content = re.sub(r'&gt;', '>', content)

    # Ensure all tags are correctly formatted by removing extra newlines within tags
    content = re.sub(r'>\s+<', '><', content)

    # Write the cleaned content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

    print("✅ pom.xml cleaned and fixed")

# Fix the pom.xml
fix_pom_file('pom.xml')
