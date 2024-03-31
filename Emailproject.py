email = input("Enter Your Email adderss :-  ")
k, j, d = 0, 0, 0
if len(email) >= 6:
   if email[0].isalpha():
      if ('@' in email) and (email.count('@')==1):
          if (email[-4]=='.') ^ (email[-3]=='.'):
              for i in email:
                      if i==i.isspace():
                          k=1
                      elif i.isalpha():
                          if i==i.upper():
                              j = 1
                      elif i.isdigit():
                          continue
                      elif i == "_" or i == "." or i == "@":
                          continue
                      else:
                          d = 1

              if k == 1 or j == 1 or d == 1:
                  print('Wrong email 5 email does not have any  space and uppercase characters')
              else:
                  print('Right Email')
          else:
              print("Wrong email 4 email has only 4 or 3 characters after '.'")
      else:
          print("Wrong email 3 email has only one '@'")
   else:
       print("Wrong email 2 Starting character is only alphabet")
else:
    print("Wrong email 1 your email has at least 6 characters")