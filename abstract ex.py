from abc import ABCMeta , abstractmethod
class Personne (metaclass = ABCMeta) :
    def __init__(self , code , nom , prenom , age) :
        self._code = code
        self._nom = nom
        self._prénom = prenom 
        self._age = age

    def getCode(self) :
        return self._code
    
    def getnom(self) :
        return self._nom
    
    def getPrenom(self) :
        return self._prenom
    
    def getAge(self) :
        return self._age

    def setCode(self,value):
            self._code = value

    def setNom(self,value):
            self._nom = value

    def setPrenom(self,value):
            self._prenom = value

    def setAge(self,value):
            self._age = value

    @abstractmethod
    def ToString(self) :
          pass
        #   print(f"le code est : {self._code} , le prénom est : {self._prénom} , le nom est : {self._nom} , l'age est : {self._age}")
    
    @abstractmethod
    def Equals (self , Pers) :
          pass
        #   if self._code == Pers._code :
        #         return True
        #   else : 
        #         return False
        
class Employé(Personne) :
    nbr = 0
    def __init__(self, code, nom, prenom, age , grade):
            super().__init__(code, nom, prenom, age)
            self.grade = grade
            Employé.nbr += 1

    def getGrade(self) :
             return self.grade

    def setGrade(self,value):
            self.grade= value

    def ToString(self):
         print(f"le code est : {self._code} , le prénom est : {self._prenom} , le nom est : {self._nom} , l'age est : {self._age} , la grade est : {self.grade}" )

    def Equals(self, Pers):
        return self._code == Pers._code
            
class élève(Personne) :
    nbrr = 0
    def __init__(self, code, nom, prenom, age , niveau , moyenne):
            super().__init__(code, nom, prenom, age )
            self.niveau  = niveau
            self.moyenne = moyenne
            élève.nbrr += 1

    def getNiveau(self) :
             return self.niveau

    def setNiveau(self,value):
            self.niveau = value

    def getMoyenne(self) :
             return self.moyenne

    def setMoyenne(self,value):
            self.moyenne = value

    def ToString(self):
         print(f"le code est : {self._code} , le prénom est : {self._prenom} , le nom est : {self._nom} , l'age est : {self._age} , le niveau  est : {self.niveau} , la moyenne est : {self.moyenne}" )

    def Equals(self, Pers):
            if self._code == Pers._code :
                return True
            else : 
                 return False
            
emp1 = Employé(1,"amine" , "jamal" , 19 , 5 )
emp2 = Employé(1,"amine" , "jamal" , 19 , 5 )
emp3 = Employé(1,"amine" , "jamal" , 19 , 5 )
print(emp2.ToString())
print(emp1.Equals(emp3))
print(emp3.nbr)

ele1 = élève(2,"ayoub" ,"raoui" , 19, 6, 19.5)
ele2 = élève(2,"ayoub" ,"raoui" , 19, 6, 19.5)
ele3 = élève(2,"ayoub" ,"raoui" , 19, 6, 19.5)

print(ele2.ToString())
print(ele1.Equals(ele3))
print(ele3.nbrr)


          


  