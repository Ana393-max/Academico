from django.contrib import admin
from .models import (
    Cidade,
    Ocupacao,
    Pessoa,
    InstituicaoEnsino,
    AreaSaber,
    Curso,
    Turno,
    Disciplina,
    Matricula,
    Avaliacao,
    Frequencia,
    Turma,
    Ocorrencia,
    CursoDisciplina,
    AvaliacaoTipo,
)

# Registro dos modelos no admin
admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Curso)
admin.site.register(Turno)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turma)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(AvaliacaoTipo)
