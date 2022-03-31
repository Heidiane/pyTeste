import pytest

from aula import Aula

def test_sem_aula_no_dia():
    aula = Aula("Aulas no dia", 0)
    assert aula.aula_dia == 0

def test_uma_aula_no_dia():
    aula = Aula("Aulas no dia", 1)
    assert aula.aula_dia == 1

def test_duas_aula_no_dia():
    aula = Aula("Aulas no dia", 1)
    aula.add_aula()
    assert aula.aula_dia == 2
