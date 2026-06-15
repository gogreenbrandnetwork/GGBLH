def eligibility_check(ami, income, household_size):
    eligible = income <= ami
    return {
        "eligible": eligible,
        "ami_limit": ami,
        "income": income,
        "household_size": household_size
    }