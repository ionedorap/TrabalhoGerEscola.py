#coding:utf-8
from django.db import models

SEMESTRE = [
      
      ('1','1°'),
      ('2','2°'),
      ('3','3°'),
      ('4','4°'),
      ('5','5°'),
      ('6','6°'),
      ('7','7°'),
      ('8','8°',),
      ('9','9°',),
      ('10','10°'),
      ('11','11°'),
      ('12','12°'),
      ('Dependência','Dependência')

]

SEXO = [

	('Masculino','Masculino'),
	('Feminino','Feminino')
	
]

class Curso(models.Model):
	cursoNome = models.CharField('Nome',max_length=100,null=True)
	
	
	
class Semestre(models.Model):
	semestreNome = models.CharField('Escolha o Semestre',max_length=1,choices=SEMESTRE,null=True)
	
	

class Estrutura(models.Model):
	estruturaAno = models.DateField('Ano de Criação',null=True)
	estruturaCurso = models.ForeignKey(Curso,verbose_name="Curso",null=True)
	
	def __unicode__(self):
		return self.Curso.cursoNome
		

		
class Turma(models.Model):
	turmaSemestre = models.ForeignKey(Semestre,verbose_name="Semestre",null=True)
	turmaEstrutura = models.ForeignKey(Estrutura,verbose_name="Estrutura",null=True)
	turmaDescricao = models.CharField('Descrição da Turma',max_length=100,null=True)

	def __unicode__(self):
		return "%s - %s" % (self.Semestre.semestreDescricao,self.Estrutura.estruturaAno)
		
		
		
class Disciplina(models.Model):
	disciplinaNome = models.CharField('Nome',max_length=100,null=True)
	disciplinaDescricao = models.CharField('Descrição da Disciplina',max_length=100,null=True)
	

class Periodo(models.Model):
	periodoNome = models.CharField('Período',max_length=100,null=True)
	periododescricao = models.CharField('descrição do Período',max_length=100,null=True)

	

class EstruturaDisciplinaPeriodo(models.Model):
	estdiscperEstrutura = models.ForeignKey(Estrutura,verbose_name="Estrutura",null=True)
	estdiscperDisciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	estdiscperPeriodo = models.ForeignKey(Periodo,verbose_name="Periodo",null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Estrutura.estruturaAno,  self.Disciplina.disciplinaNome,  self.Periodo.periodoNome)
	


class TurmaDisciplina(models.Model):
	turmadiscTurma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	turmadiscDisciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	turmadiscEstruturaDisciplina = models.ForeignKey(EstruturaDisciplinaPeriodo,verbose_name="Estrutura Disciplina Período",null=True)
	#turmadiscTurmaDiscHorProf = models.ForeignKey(TurmaDiscHorProf,verbose_name="Turma Disciplina Horario Professor",null=False)
	# Aqui em cima quero pegar a chave primária da classe TurmaDiscHorProf 
	
	
	def __unicode__(self):
		return "%s - %s" % (self.Turma.turmaDescricao,  self.Disciplina.disciplinaNome,  self.Periodo.periodoNome)
	
		
	
class Aluno(models.Model):
	alunoNome = models.CharField('Nome do Aluno',max_length=100,null=True)
	alunoSexo = models.CharField('Sexo',max_length=10,choices=SEXO,null=True)
	
	
	
	
class TurmaAluno(models.Model):
	turmaalunoTurma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	turmaalunoAluno = models.ForeignKey(Aluno,verbose_name="Aluno",null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Turma.turmaDescricao,self.Aluno.alunoNome)
	
	

	#class DisciplinaAluno(models.Model):
	#disciplinaalunoTurmaAluno = models.ForeignKey(TurmaAluno,verbose_name="Turma Aluno",null=True)
	#disciplinaalunoTurma = models.ForeignKey(Turma,verbose_name="Turma",null=False)
	#aqui preciso pegar a chave primária tbm

	#def __unicode__(self):
	#	return "%s - %s" % (self.TurmaAluno.)
	
	#class Meta:
	#	unique_together = ("TurmaAluno")
	

	
class Professor(models.Model):
	professorNome = models.CharField('Nome do Professor',max_length=100,null=True)
	professorFormacao = models.CharField('Formação',max_length=100,null=True)
	professorSexo = models.CharField('Sexo',max_length=10,choices=SEXO,null=True)
	

class Horario(models.Model):
	horarioTime = models.TimeField('Data Fim da inscricao',null=True)
	
	
	
class TurmaDiscHorProf(models.Model):
	turmadischorprofProfessor = models.ForeignKey(Professor,verbose_name="Professor",null=True)
	turmadischorprofHorario = models.ForeignKey(Horario,verbose_name="Horario",null=True)
	#turmadischorprofTurmaDisciplina = models.ForeignKey(Eventos,verbose_name="Turma Disciplina",null=False)
	
	def __unicode__(self):
		return "%s - %s" % (self.Professor.professorNome,  self.Horario.horarioTime)
