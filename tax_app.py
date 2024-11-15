from taxes import TaxCategory, Tax, Brackets, tax_liability, big_income

tax_brackets = Brackets([
    Tax(year=2024, percentage=10, min_income=0, max_income=11_600, category=TaxCategory.SINGLE),
    Tax(year=2024, percentage=12, min_income=11_601, max_income=47_150, category=TaxCategory.SINGLE),
    Tax(year=2024, percentage=22, min_income=47_151, max_income=100_525, category=TaxCategory.SINGLE),
    Tax(year=2024, percentage=24, min_income=100_526, max_income=191_950, category=TaxCategory.SINGLE),
    Tax(year=2024, percentage=32, min_income=191_951, max_income=243_725, category=TaxCategory.SINGLE),
    Tax(year=2024, percentage=35, min_income=243_762, max_income=609_350, category=TaxCategory.SINGLE),
    Tax(year=2024, percentage=37, min_income=609_351, max_income=big_income, category=TaxCategory.SINGLE),
    Tax(year=2024, percentage=10, min_income=0, max_income=23200, category=TaxCategory.MARRIED_FILLING_JOINTLY),
    Tax(year=2024, percentage=12, min_income=23_201, max_income=94_300, category=TaxCategory.MARRIED_FILLING_JOINTLY),
    Tax(year=2024, percentage=22, min_income=94_301, max_income=201_050, category=TaxCategory.MARRIED_FILLING_JOINTLY),
    Tax(year=2024, percentage=24, min_income=201_051, max_income=383_900, category=TaxCategory.MARRIED_FILLING_JOINTLY),
    Tax(year=2024, percentage=32, min_income=383_901, max_income=487_450, category=TaxCategory.MARRIED_FILLING_JOINTLY),
    Tax(year=2024, percentage=35, min_income=487_451, max_income=731_200, category=TaxCategory.MARRIED_FILLING_JOINTLY),
    Tax(year=2024, percentage=37, min_income=731_201, max_income=big_income, category=TaxCategory.MARRIED_FILLING_JOINTLY),
])
taxes1 = tax_liability(income=120_000, year=2024, tax_brackets=tax_brackets, category=TaxCategory.SINGLE)
taxes2 = tax_liability(income=120_000, year=2024, tax_brackets=tax_brackets, category=TaxCategory.MARRIED_FILLING_JOINTLY)
print(taxes1, TaxCategory.SINGLE)
print(taxes2, TaxCategory.MARRIED_FILLING_JOINTLY)
