print("Hello and welcome to MACS PLACE! Please enter your First and Last name")
userinput = input("Please type your Full name below.")
birth_day_month = input("Please enter your birthday below. Use the format MM/DD") 
birth_year = int(input("Please enter your birth month below. Use the format 0000"))
if birth_year >= 1946 and birth_year <= 1964:
    print("Oh! it looks like you are a baby boomer. Looking good Grandma or Grandpa!")
if birth_year >= 1965 and birth_year <= 1980:
    print("Well hello Mr. or Mrs. Gen X. I hope you are doing well!")
if birth_year >= 1981 and birth_year <= 1996: 
    print("How yall doing Millenials? Welcome!")
if birth_year >= 1997 and birth_year <= 2012:
    print("Hey there Gen Z! Hope yall are staying trendy!")
if birth_year >= 2013:
    print("Hey Alpha! Welcome to the future!")
if birth_year <= 1945 or birth_year >= 2013:
    print("Error, please enter an appropriate year.")
sucker_socials = int(input("Please enter your social security number below."))
if sucker_socials >= 0:
    print("Thank you for your cooperation.")
print("youve been scamed. welcome to MACS PLACE!")
