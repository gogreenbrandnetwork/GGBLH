def lookup_lottery(borough=None, income=None, household_size=None):
    return {
        "status": "success",
        "borough": borough,
        "income": income,
        "household_size": household_size,
        "message": "Lottery lookup placeholder. Connect to NYC Housing Connect API here."
    }