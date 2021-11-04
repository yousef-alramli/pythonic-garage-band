from abc import ABC,abstractmethod

class Band :
    instances= []
    def __init__(self,name,members):
        self.name =name
        self.members = members

        Band.instances.append(self)

    def play_solo(self):
        return " solo"
    
    def play_solos(self):
        solos = []
        for i in self.members:
            solos += [i.play_solo()]
        return solos
    
    @classmethod
    def to_list(cls):
        return cls.instances



class Musician(Band):
    def __init__(self,name):
        self.name =name
        

    

class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        repr_value= repr(f"Guitarist instance. Name = {self.name}" )
        return repr_value.replace("'", "")

    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        # play_solos.append("face melting guitar solo")
        return "face melting guitar solo"
   

class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        repr_value= repr(f"Drummer instance. Name = {self.name}" )
        return repr_value.replace("'", "")

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        # play_solos.append("rattle boom crash")
        return "rattle boom crash"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        repr_value= repr(f"Bassist instance. Name = {self.name}" )
        return repr_value.replace("'", "")

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        # play_solos.append("bom bom buh bom")
        return "bom bom buh bom"




if __name__=="__main__":
    # yo = Guitarist("Joan Jett")
    # jos = Bassist("Joan ds")
    # jodfs = Drummer("sd Jett")
    # members = [yo,jos,jodfs]
    # jo = Band("soso",members)
    # print(x)
    y=len(Band.instances)
    print(y)
    print(Band.to_list()==[])
    pass
    
    