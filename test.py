import re

a = '#start #start_end #help #help_end'

pattern = re.compile(u'#')

print(pattern.search(a))