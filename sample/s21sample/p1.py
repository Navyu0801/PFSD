class User:
    counter =0
    def init(self,n,c):
        self.name=n
        self.city=c
        User.counter = User.counter+1
    def display(self):
            print("name:",self.name)
            print("city",self.city)
            print("counter:",User.counter)

ob1 =User("keerthi","Vijayawada")
ob2 =User("Vennela","guntur")
ob1.display()
ob2.display()