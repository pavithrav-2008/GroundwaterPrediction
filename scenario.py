def simulate_scenario(
    scenario,
    rainfall,
    temperature,
    humidity,
    soil,
    previous,
    water,
    recharge
):
    """
    Modify environmental parameters based on
    the selected scenario.
    """

    if scenario == "Heavy Rainfall":
        rainfall += 100
        recharge += 30

    elif scenario == "Drought":
        rainfall = max(0, rainfall - 100)
        recharge = max(0, recharge - 30)
        temperature += 3

    elif scenario == "High Water Consumption":
        water += 200

    elif scenario == "Improved Recharge":
        recharge += 40

    return (
        rainfall,
        temperature,
        humidity,
        soil,
        previous,
        water,
        recharge
    )