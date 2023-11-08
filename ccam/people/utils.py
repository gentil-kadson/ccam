import re


def clean_cpf(cpf: str) -> str:
    """
    Removes characters '.' and '-' from CPF number
    """
    return re.sub("[^0-9]", "", cpf)
