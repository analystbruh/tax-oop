from dataclasses import dataclass
from typing import List, Dict
from enum import Enum

class TaxCategory(Enum):
    SINGLE = 1
    MARRIED_FILING_JOINTLY = 2
    MARRIED_FILING_SEPARATELY = 3
    HEAD_OF_HOUSEHOLD = 4

@dataclass
class Tax:
    year: int
    percentage: int
    min_income: int
    max_income: int
    category: TaxCategory

@dataclass
class IncomeRange:
    min: int
    max: int

class Bracket(Dict):
    def __init__(self, taxes: List[Tax]):
        for tax in taxes:
            self[tax.percentage] = IncomeRange(tax.min_income, tax.max_income)

@dataclass
class Brackets:
    taxes: List[Tax]
    def tax_bracket(self, yr: int, category: TaxCategory) -> Bracket:
        tax_year = filter(lambda tax: tax.year == yr and tax.category == category, self.taxes)
        return Bracket(tax_year)

def tax_liability(income: int, year: int, tax_brackets: Brackets, category: TaxCategory) -> float:
    taxes = tax_brackets.tax_bracket(year, category)
    tax = 0
    for percentage, income_range in taxes.items():
        if income <= income_range.max and income >= income_range.min:
            tax += (income - income_range.min) * percentage / 100
        elif income >= income_range.max:
            tax += (income_range.max - income_range.min) * percentage / 100
    return tax

big_income: int = 99999*99999