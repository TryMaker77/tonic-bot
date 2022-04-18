#Tonic-Bot
#Initializations with Variables
str1 = "blank" 
mood = "blank"
User_Name = "blank"
num1 = int()
num2 = int()
qasked = 0

print("""
 ________                   __                   _______               __
/        |                 /  |                 /       \             /  |    
$$$$$$$$/______   _______  $$/   _______        $$$$$$$  |  ______   _$$ |_   
   $$ | /      \ /       \ /  | /       |______ $$ |__$$ | /      \ / $$   |  
   $$ |/$$$$$$  |$$$$$$$  |$$ |/$$$$$$$//      |$$    $$< /$$$$$$  |$$$$$$/   
   $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |     $$$$$$/ $$$$$$$  |$$ |  $$ |  $$ | __ 
   $$ |$$ \__$$ |$$ |  $$ |$$ |$$ \_____        $$ |__$$ |$$ \__$$ |  $$ |/  |
   $$ |$$    $$/ $$ |  $$ |$$ |$$       |       $$    $$/ $$    $$/   $$  $$/ 
   $$/  $$$$$$/  $$/   $$/ $$/  $$$$$$$/        $$$$$$$/   $$$$$$/     $$$$/  
A Chatbot by TR7
v0.3.5
""")
User_Name = input("Enter your name: ")
print("Hello " + User_Name + """. 
Tonic is a simple Python chatbot made in order to test things such as boolean logic
and variable definition.
(Also remember to speak to the bot in lowercase, without punctuation.)""")
while (str1 != "quit"):
    str1 = input("Say something: ")
    #"hello" //////////////////////////////////////////
    if "hello" in str1:
        print("Hi " + User_Name + "! (I read this as the 'hello' greeting.")
        int(qasked) + 1
    #"hi" //////////////////////////////////////////
    if "hi" in str1:
        print("Hi " + User_Name + "! (I read this as the 'hi' greeting.")
        int(qasked) + 1
    #"how are you?" //////////////////////////////////////////
    if "how are you" in str1:
        print("good, how about you? (I read this as you asking 'how are you'.)")
        int(qasked) + 1
        mood = input("Enter Mood: ")
        if "good" in mood:
            print("Nice to hear " + User_Name + "! (I read this as you being in a good mood.)")
        if "bad" in mood:
            print("I hope you feel better soon, " + User_Name + "! (I read this as you being in a bad mood.)")
        if "alright" in mood:
            print("Good to hear -- hopefully it gets even better! (I read this as you being in a so-so mood.)")
    #"name length" //////////////////////////////////////////
    if "name length" in str1:
        print( "Your name is " + str(len(User_Name)) + " letters long. (I read this as you asking how long your name is.)")
        int(qasked) + 1
    #"question count"
    if "question count" in str1:
        print("You have asked me " + str(qasked) + " questions total. (I read this as you asking how many questions you asked.)")
        qasked + 1
    #Math Functions
    #"Multiply" //////////////////////////////////////////
    if "multiply" in str1:
        num1 =  int(input("Enter your first number: "))
        num2 =  int(input("Enter your second number: "))
        multiply = num1 * num2
        print(multiply)
        qasked + 1
    #"Divide" //////////////////////////////////////////
    if "divide" in str1:
        num1 =  int(input("Enter your first number: "))
        num2 =  int(input("Enter your second number: "))
        divide = num1 / num2
        print(divide)
        qasked + 1
    #"add" //////////////////////////////////////////
    if "add" in str1:
        num1 =  int(input("Enter your first number: "))
        num2 =  int(input("Enter your second number: "))
        add = num1 + num2
        print(add)
        qasked + 1
    #"Subtract" //////////////////////////////////////////
    if "subtract" in str1:
        num1 =  int(input("Enter your first number: "))
        num2 =  int(input("Enter your second number: "))
        subtract = num1 - num2
        print(subtract)
        qasked + 1
