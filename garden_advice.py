# This program provides gardening advice based on two pieces of information:
# the current season and the type of plant the user is growing. The script
# collects user input, determines the appropriate advice, and prints it out.


def get_user_input():
    """
    Ask the user for the season and plant type.

    This function handles all user interaction related to input.
    It normalizes the input by stripping extra spaces and converting
    everything to lowercase to make comparisons consistent.
    """
    # Prompt the user to enter the season and clean the input
    season = input("Enter the season (summer/winter): ").strip().lower()

    # Prompt the user to enter the plant type and clean the input
    plant_type = input("Enter the plant type (flower/vegetable): ").strip().lower()

    # Return both values so they can be used by other functions
    return season, plant_type


def get_season_advice(season):
    """
    Return gardening advice based on the season provided.

    This function checks the season and returns a specific message.
    If the season is not recognized, it returns a default message.
    """
    # Provide advice for summer conditions
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"

    # Provide advice for winter conditions
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"

    # Fallback advice if the season is not one of the expected values
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """
    Return gardening advice based on the plant type provided.

    This function checks the plant type and returns a specific message.
    If the plant type is not recognized, it returns a default message.
    """
    # Advice specific to flowering plants
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."

    # Advice specific to vegetable plants
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"

    # Fallback advice if the plant type is not one of the expected values
    else:
        return "No advice for this type of plant."


def main():
    """
    Main function that coordinates the program flow.

    It gathers user input, generates advice based on that input,
    and prints the final combined message for the user.
    """
    # Collect the season and plant type from the user
    season, plant_type = get_user_input()

    # Start with an empty advice string and build it step-by-step
    advice = ""
    advice += get_season_advice(season)   # Add season-specific advice
    advice += get_plant_advice(plant_type)  # Add plant-type-specific advice

    # Display the final advice to the user
    print(advice)


# This ensures the main function only runs when the script is executed directly,
# not when it is imported as a module in another program.
if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
