import re

str = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."

print(re.search("Amy", str))

print(re.split("Amy", str))

print(re.findall("Amy", str))

# Patterns and character classes
