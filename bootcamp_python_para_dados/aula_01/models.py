from pydantic import BaseModel, PositiveFloat

class bonusUser(BaseModel):
    nome: str
    salario: PositiveFloat
    bonus: PositiveFloat
