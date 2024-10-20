from pydantic import PositiveFloat
from datetime import datetime
from typing import Dict
# from models import bonusUser
# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
def convert_number_to_positivefloat(number) -> PositiveFloat:
    try:
        return PositiveFloat(number)
    except:
        print('Por favor, insira um valor numérico positivo.')


# def calculate_bonus(salário: PositiveFloat, bonus: PositiveFloat):
#     try:
#         return salário * bonus
#     except:
#         raise TypeError('Por favor, insira o salário e o bônus em formato numérico.')
    
class bonusUser:
    def __init__(self, nome: str, salary: PositiveFloat, bonus_perc: PositiveFloat, year: int = datetime.now().year) -> None:
        self.nome: str = nome
        self.salary: PositiveFloat = salary
        self.bonus_perc: PositiveFloat = bonus_perc
        self.bonus_value: PositiveFloat = None
        self.year: int = year
    
    def __repr__(self) -> str:
        return f'{self.nome}, o seu bônus no ano de {self.year} será de R$ {self.bonus_value:.2f}.'
    
    def set_bonus_value(self) -> None:
        self.bonus_value = self.salary * self.bonus_perc
        
    
    def get_bonus_info(self) -> str:
        if self.bonus_value == None:
            self.set_bonus_value()
        return self.__repr__()
    
def get_data() -> dict:
    # Raw
    raw_name = input("Nome: ")
    raw_salary = input('Salário: ')
    raw_bonus_perc = input('Percentual de Bônus: ')
    
    # Formatted Numbers
    try:
        formatted_salary = convert_number_to_positivefloat(raw_salary)
        formatted_bonus_perc = convert_number_to_positivefloat(raw_bonus_perc)
    except:
        print("Por favor, insira um valor numérico positivo.")