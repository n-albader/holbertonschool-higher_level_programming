
import os


def generate_invitations(template, attendees):
    """Generate personalized invitation files for attendees."""

    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = [
        "name",
        "event_title",
        "event_date",
        "event_location"
    ]

    for index, attendee in enumerate(attendees, start=1):
        message = template

        for key in placeholders:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            message = message.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        if os.path.exists(filename):
            print(f"{filename} already exists. Skipping.")
            continue

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(message)

        except OSError as error:
            print(f"Error writing {filename}: {error}")
