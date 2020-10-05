q1 = input('''Hello! Do you want to convert:
A: Celsius to Fahrenheit
B: Fahrenheit to Celsius 
''')
if q1 == "A":
  q2 = int(input("Please enter the Celsius temperature: "))
  fah = (q2*1.8) + 32
  print('{} degree Celsius is equal to {} degree Fahrenheit'.format(q2,fah))

else:
  q2 = int(input("Please enter the Fahrenheit temperature: "))
  cel = (q2-32)*5/9
  print('{} degree Fahrenheit is equal to {} degree Celsius'.format(q2,cel))
