def master_yoda(text):
  split_text = text.split()
  yoda_text = split_text[::-1]
    
  return " ".join(yoda_text)
  
print(master_yoda("May the force be with you"))
