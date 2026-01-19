def get_user_input():
    """Ask the user for the season and plant type."""
    season = input("Enter the season (summer/winter): ").strip().lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").strip().lower()
    return season, plant_type


def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Generate gardening advice based on user input."""
    season, plant_type = get_user_input()
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)
    print(advice)


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
