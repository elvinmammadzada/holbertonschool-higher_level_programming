#!/usr/bin/python3
"""Basic template creating"""

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

template_text = """
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
"""


def generate_invitations(template, attendees):
    """Generate invitations"""
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a dictionary")
        return
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    for i, attende in enumerate(attendees, start=1):
        name = attende.get("name", "N/A")
        event_title = attende.get("event_title", "N/A")
        event_date = attende.get("event_date", "N/A")
        event_location = attende.get("event_location", "N/A")

        filled = template.replace("{name}", name)\
                        .replace("{event_title}", event_title)\
                        .replace("{event_date}", event_date)\
                        .replace("{event_location}", event_location)
        filename = f"output_{i}.txt"
        with open(filename, "w") as f:
            f.write(filled)

        print(f"Generated: {filename}")
