import random
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  quotesCntToPrint = 3
  last = 25
  rnd = random.randint(0,last - 2)

  # use the argument "end" to specify the end of line string and print with
  # space
  # below is printing without space

  #refer https://realpython.com/python-print/#preventing-line-breaks
  #Note: Looping over lines in a text file preserves their own newline
  #characters,
  #which combined with the print() function’s default behavior will result in a
  #redundant newline character:

  print("`" + quotes[rnd].rstrip() + "`") #rstrip() to strip out new line from the line read from the text file
  print("`" + quotes[rnd + 1].rstrip() + "`")
  print("`" + quotes[rnd + 2].rstrip() + '`')#,end = '' add param to remove new line when printing

  # below is printing with empty line after each
  #print(quotes[rnd])
  #print(quotes[rnd + 1])
  #print(quotes[rnd + 2])

  f = open("demofile.txt", "a")
  f.write('\n' + input())
  f.close()
if __name__ == "__main__":
  primary()
  

import os
if os.path.exists("demofile1.txt"):
  os.remove("demofile1.txt")
else:
  print("The file does not exist")
