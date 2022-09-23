def last2(str):
  substring = str[len(str) - 2 :]
  answer = 0
  counter = 0
  while counter < len(str) - 2:
    if substring == str[counter: counter + 2]:
      answer += 1
    counter += 1
  return answer