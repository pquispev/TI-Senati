class Persona:
    def __init__(self, nombre, genero, dni, fecha_nacimiento, peso, altura,):
        self._nombre = nombre
        self._genero = genero
        self._dni = dni
        self._fecha_nacimento = fecha_nacimiento
        self._peso = peso
        self._altura = altura
    
    def edad(self):
        return 15
    
class Alumno(Persona):
    def __init__(self, nombre, genero, dni, fecha_nacimiento, peso, altura, id_estudiante, email):
        super().__init__(nombre, genero, dni, fecha_nacimiento, peso, altura)
        self._id_estudiante = id_estudiante
        self._email = email
    
    def info(self):
        print(f"{self._nombre} {self._dni} {self._id_estudiante}")
        

juan = Alumno("Juan", "m", "222222", "10/10/2000", "71", "180", "023233", "juan@senati.pe")
juan.info()
    