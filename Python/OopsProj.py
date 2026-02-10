class Chatbook:
    #Static variable
    #we can access static variable without creating objects
    #And access using class name

    __user_id=1
    def __init__(self):
        self.id=Chatbook.__user_id
        Chatbook.__user_id+=1
        self.__name="Deafault user"
        self.username=""
        self.password=""
        self.isloggedin=False
        # self.menu()
    @staticmethod  
    def get_id():
        return Chatbook.__user_id
    
    @staticmethod  
    def set_id(val):
        Chatbook.__user_id=val    

    def get_name(self):
        return self.__name

    def set_name(self,name):
         self.__name=name    

    def menu(self):
        user_input=int(input("""Welcome to chatbook!How would you like to proceed?
        Press 1 to signup
        Press 2 to signin
        Press 3 to write a post
        Press 4 to message a friend
        Press any to exit\n"""
        ))
        if user_input==1:
            self.signin()
        elif user_input==2:
            self.signup()
        elif user_input==3:
            self.writepost()
        elif user_input==4:
            pass
        else :
            exit()


    def signin(self):
        uname=input("Enter username: ")
        pwd=input("Enter password: ")
        self.username=uname
        self.password=pwd
        print(f"hello {self.username} your are signed in successfully\n")
        self.menu()

    def signup(self):
        if(self.username=="" and self.password==""):
            print("Please signin first")
        else:
            uname=input("Enter your name: ") 
            pwd=input("Enter your password: ")  
            if(uname==self.username and pwd==self.password):
                print("Sign up successfully\n")
            else:
                print("Invalid credentials\n")
        self.isloggedin=True        
        self.menu()
        

    def writepost(self):
        if(self.isloggedin==True):
            post=input("Enter your post here : ")
            print(f" {post} Posted successfully")
        else:
            print("Signup to post something")     
        self.menu()    



# obj=Chatbook()  
    
