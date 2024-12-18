class Gep:
    def __init__(self,id,hely,tipus,ipcim):
        self.id = id
        self.hely = hely
        self.tipus = tipus
        self.ipcim = tipus


    def __str__(self):
            return f"A legkisebb asztali gép azonosítója:: {self.id}, gyártási éve: {self.hely}"