#coding:utf-8
from django.contrib import admin
from models import Curso
from models import Semestre
from models import Estrutura
from models import EstruturaDisciplinaPeriodo
from models import Disciplina
from models import Periodo
from models import TurmaDisciplina
#from models import DisciplinaAluno
from models import Turma
from models import TurmaAluno
from models import Aluno
from models import Professor
from models import Horario
from models import TurmaDiscHorProf

class AdminCurso(admin.ModelAdmin):
	 list_display = ['cursoNome']
	 list_filter = []
	 search_fields = []

class AdminSemestre(admin.ModelAdmin):
	 list_display = ['semestreNome']
	 list_filter = []
	 search_fields = []
	 
class AdminEstrutura(admin.ModelAdmin):
	 list_display = ['estruturaAno','estruturaCurso']
	 list_filter = []
	 search_fields = []	 

class AdminEstruturaDisciplinaPeriodo(admin.ModelAdmin):
	 list_display = ['estdiscperEstrutura','estdiscperDisciplina','estdiscperPeriodo']
	 list_filter = []
	 search_fields = []	
	 
class AdminDisciplina(admin.ModelAdmin):
	 list_display = ['disciplinaNome','disciplinaDescricao']
	 list_filter = []
	 search_fields = []	
	 
class AdminPeriodo(admin.ModelAdmin):
	 list_display = ['periodoNome','periododescricao']
	 list_filter = []
	 search_fields = []	
	 
class AdminTurmaDisciplina(admin.ModelAdmin):
	 list_display = ['turmadiscTurma','turmadiscDisciplina','turmadiscEstruturaDisciplina']
	 list_filter = []
	 search_fields = []	
	 
class AdminDisciplinaAluno(admin.ModelAdmin):
	 list_display = []
	 list_filter = []
	 search_fields = []	
	 
class AdminTurma(admin.ModelAdmin):
	 list_display = ['turmaSemestre','turmaEstrutura','turmaDescricao']
	 list_filter = []
	 search_fields = []	
	 
class AdminTurmaAluno(admin.ModelAdmin):
	 list_display = ['turmaalunoTurma','turmaalunoAluno']
	 list_filter = []
	 search_fields = []	
	 
class AdminAluno(admin.ModelAdmin):
	 list_display = ['alunoNome','alunoSexo']
	 list_filter = []
	 search_fields = []	
	 
class AdminProfessor(admin.ModelAdmin):
	 list_display = ['professorNome','professorFormacao','professorSexo']
	 list_filter = []
	 search_fields = []	

class AdminHorario(admin.ModelAdmin):
	 list_display = ['horarioTime']
	 list_filter = []
	 search_fields = []	
	 
class AdminTurmaDiscHorProf(admin.ModelAdmin):
	 list_display = ['turmadischorprofProfessor','turmadischorprofHorario']
	 list_filter = []
	 search_fields = []	
	  
	 

admin.site.register(Curso,AdminCurso) 
admin.site.register(Semestre, AdminSemestre) 
admin.site.register(Estrutura,AdminEstrutura) 
admin.site.register(EstruturaDisciplinaPeriodo,AdminEstruturaDisciplinaPeriodo) 
admin.site.register(Disciplina, AdminDisciplina) 
admin.site.register(Periodo, AdminPeriodo) 
admin.site.register(TurmaDisciplina, AdminTurmaDisciplina) 
#admin.site.register(DisciplinaAluno, AdminDisciplinaAluno) 
admin.site.register(Turma, AdminTurma) 
admin.site.register(TurmaAluno, AdminTurmaAluno) 
admin.site.register(Aluno, AdminAluno) 
admin.site.register(Professor, AdminProfessor) 
admin.site.register(Horario, AdminHorario) 
admin.site.register(TurmaDiscHorProf, AdminTurmaDiscHorProf) 