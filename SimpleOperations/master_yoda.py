def master_yoda(text):
  yoda_text =[]
  split_text = text.split(' ')
  for element in split_text[::-1]:
    yoda_text.append(element)
  return " ".join(yoda_text)
  
print(master_yoda("why dont you stay when you are so powerful"))