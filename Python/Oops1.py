class employee:
    def __init__(self):
        print("class before intiated")
        self.name="nithin"
        self.salary=20000000
        self.company="Microsoft"
        print("class after intiated")

    def enjoy(self):
        print(f"{self.name} is enjoying the party")   

nithin=employee()

nithin.enjoy()
