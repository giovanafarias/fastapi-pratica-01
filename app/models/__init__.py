# Importa todos os modelos para que fiquem visíveis no pacote models 
from app.models.curso import Curso
from app.models.disciplina import Disciplina
from app.models.aluno import Aluno
from app.models.matricula import Matricula
from app.models.user import User, UserRole 

# Explicita o que o pacote exporta
__all__ = ["Curso", "Disciplina", "Aluno", "Matricula", "User", "UserRole"]