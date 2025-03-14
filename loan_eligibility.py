def loan_eligibility(age, annual_income, credit_score):
    if age < 0 or age > 125:
        raise ValueError("Invalid age")
    if annual_income < 0:
        raise ValueError("Invalid income")
    if credit_score < 0:
        raise ValueError("Invalid credit score")

    if age < 18 or age > 65:
        return False

    if annual_income < 30000:
        return False
    
    if credit_score < 60:
        return False
    
    return True
