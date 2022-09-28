import re


def find_names(line):
  pattern = r"(?:(?:(?:Mrs|Mr|Ms|Dr)[. ])(?:(?:[ ]*[A-Z]+[a-z]*)[.]?)+)|(?:(?:[ ]*[A-Z]+[a-z]*)[.]?)(?:(?:[ ]*[A-Z]+[a-z]*)[.]?)+"
  result = re.findall(pattern, line)
  return result


f = open("names.txt")
for line in f.readlines():
    result = find_names(line)
    if (len(result)>0):
        print(result)