class student:
    grade=9
    name="sam"

    def intro(self):
        print("hi iam student")
    
    def detail(self):
        print("my name is ",self.name)
        print("iam in grade",self.grade)

ob=student()
ob.intro()
ob.detail()