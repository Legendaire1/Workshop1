def string_bits(str):
  counter = 0
  answer = ""
  while counter < len(str):
    answer += str[counter]
    counter += 2
  return answer
