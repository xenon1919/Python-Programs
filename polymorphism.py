class Birds:  
    def intro1(self):  
        print("There are multiple types of birds in the world.")  
    def flight1(self):  
        print("Many of these birds can fly but some cannot.")  
  
class sparrow1(Birds):  
    def flight1(self):  
        print("Sparrows are the bird which can fly.")  
      
class ostrich1(Birds):  
    def flight1(self):  
        print("Ostriches are the birds which cannot fly.")  
      
obj_birds = Birds()  
obj_spr1 = sparrow1()  
obj_ost1 = ostrich1()  
  
obj_birds.intro1()  
obj_birds.flight1()  
  
obj_spr1.intro1()  
obj_spr1.flight1()  
  
obj_ost1.intro1()  
obj_ost1.flight1()