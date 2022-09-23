def string_match(a, b):
  string1 = str(a)
  string2 = str(b)
  counter = 0
  answer = 0
  while counter < len(string1)-1:
    if string1[counter:counter+2] == string2[counter:counter+2]:
      answer+=1
    counter+=1
  return answer
