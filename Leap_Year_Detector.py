#Leap-year Detector !
year = int(input("Which year do you want to check? \n"))

if year % 4 == 0 :
  if year % 100 == 0: 
    if year % 400 == 0:
      print("It is a Leap year.")

    else:
      print("Not a Leap year.")

  else:
    print("It is a leap year.")  


else:
  print("Not a leap year.")


