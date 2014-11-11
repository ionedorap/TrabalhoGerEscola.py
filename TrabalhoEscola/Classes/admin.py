#coding:utf-8
from django.contrib import admin
from models import Curso
from models import Semestre
from models import Estrutura
from models import EstruturaDisciplinaPeriodo
from models import Disciplina
from models import Periodo
from models import TurmaDisciplina
from models import DisciplinaAluno
from models import Turma
from models import TurmaAluno
from models import Aluno
from models import Professor
from models import Horario
from models import TurmaDisciplina_X_HorarioProfessor

class AdminCurso(admin.ModelAdmin):
	 list_display = ['Nome','Turno']
	 list_filter = []
	 search_fields = ['Nome']

class AdminSemestre(admin.ModelAdmin):
	 list_display = ['Ano','Semestre']
	 list_filter = []
	 search_fields = []
	 
class AdminEstrutura(admin.ModelAdmin):
	 list_display = ['Ano','Curso']
	 list_filter = []
	 search_fields = []	 

class AdminEstruturaDisciplinaPeriodo(admin.ModelAdmin):
	 list_display = ['Estrutura','Disciplina','Periodo']
	 list_filter = []
	 search_fields = []	
	 
class AdminDisciplina(admin.ModelAdmin):
	 list_display = ['Nome','Descricao']
	 list_filter = []
	 search_fields = []	
	 
class AdminPeriodo(admin.ModelAdmin):
	 list_display = ['Descricao','Periodo', 'Identificacao']
	 list_filter = []
	 search_fields = []	
	 
class AdminTurmaDisciplina(admin.ModelAdmin):
	 list_display = ['Turma','Disciplina','EstruturaDisciplina']
	 list_filter = []
	 search_fields = []	
	 
class AdminDisciplinaAluno(admin.ModelAdmin):
	 list_display = ['TurmaAluno','Disciplina','Descricao']
	 list_filter = []
	 search_fields = []	
	 
class AdminTurma(admin.ModelAdmin):
	 list_display = ['Nome','AnoInicio','Semestre','Estrutura','Descricao']
	 list_filter = []
	 search_fields = []	
	 
class AdminTurmaAluno(admin.ModelAdmin):
	 list_display = ['Turma','Aluno']
	 list_filter = []
	 search_fields = []	
	 
class AdminAluno(admin.ModelAdmin):
	 list_display = ['Nome','Sexo']
	 list_filter = []
	 search_fields = []	
	 
class AdminProfessor(admin.ModelAdmin):
	 list_display = ['Nome','Formacao','Sexo']
	 list_filter = []
	 search_fields = []	

class AdminHorario(admin.ModelAdmin):
	 list_display = ['Turno','Comeco','Fim']
	 list_filter = []
	 search_fields = []	
	 
class AdminTurmaDisciplina_X_HorarioProfessor(admin.ModelAdmin):
	 list_display = ['Professor','Horario', 'Disciplina','Turma']
	 list_filter = []
	 search_fields = []	
	  
	 

admin.site.register(Curso,AdminCurso) 
admin.site.register(Semestre, AdminSemestre) 
admin.site.register(Estrutura,AdminEstrutura) 
admin.site.register(EstruturaDisciplinaPeriodo,AdminEstruturaDisciplinaPeriodo) 
admin.site.register(Disciplina, AdminDisciplina) 
admin.site.register(Periodo, AdminPeriodo) 
admin.site.register(TurmaDisciplina, AdminTurmaDisciplina) 
admin.site.register(DisciplinaAluno, AdminDisciplinaAluno) 
admin.site.register(Turma, AdminTurma) 
admin.site.register(TurmaAluno, AdminTurmaAluno) 
admin.site.register(Aluno, AdminAluno) 
admin.site.register(Professor, AdminProfessor) 
admin.site.register(Horario, AdminHorario) 
admin.site.register(TurmaDisciplina_X_HorarioProfessor, AdminTurmaDisciplina_X_HorarioProfessor) 