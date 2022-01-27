#Initializations with Variables
str1 = "blank" 
mood = "blank"
User_Name = "blank"


#Code
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
A Chatbot by TR77 / Thanks to: Theroy, helloworld, Maybe Lindow
v0.2.7
""")
User_Name = input("Enter your name: ")
print("Hello " + User_Name + """. 
Tonic is a simple Python chatbot made in order to test things such as boolean logic
and variable definition.
(Also remember to speak to the bot in lowercase, without punctuation.)""")
while (str1 != "quit"): # You need an exit condition here
    str1 = input("Say something: ")
    #"hello" //////////////////////////////////////////
    if "hello" in str1:
        print("Hi " + User_Name + "! (I read this as the 'hello' greeting.")
    #"hi" //////////////////////////////////////////
    if "hi" in str1:
        print("Hi " + User_Name + "! (I read this as the 'hi' greeting.")
    #"how are you?" //////////////////////////////////////////
    if "how are you" in str1:
        print("good, how about you? (I read this as you asking 'how are you'.)")
        mood = input("Enter Mood: ")
        if "good" in mood:
            print("Nice to hear " + User_Name + "! (I read this as you being in a good mood.)")
        if "bad" in mood:
            print("I hope you feel better soon, " + User_Name + "! (I read this as you being in a bad mood.)")
    #"name length" //////////////////////////////////////////
    if "name length" in str1:
        print( "Your name is " + str(len(User_Name)) + " letters long. (I read this as you asking how long your name is.")