class cop:
    def add(self,name,age,work,experience,designation):
        self.name=name
        self.age=age
        self.work=work
        self.experience=experience
        self.designation=designation
    def display(self):
        print("name is:" , self.name)
        print("age is:" , self.age)
        print("work is:" , self.work)
        print("experience is:" , self.experience)
        print("designation is:" , self.designation)
    def update(self,name,age,work,experience,designation):
        self.name = name
        self.age = age
        self.work = work
        self.experience = experience
        self.designation = designation
class mission(cop):
        def add_mission_details(self,mission):
            self.mission=mission
            print(self.mission)
obj=mission()
obj.add_mission_details("mission detection of bugs")
obj.add("harman dhindsa",19,"software engineer","two years","manager")
obj.display()
obj.update("jojo",20,"engineer","one year","associate registrar")
obj.display()
