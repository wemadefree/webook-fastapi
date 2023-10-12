"""iCal module.

Generate iCal files from WeBook events.
"""

from typing import List

from app.arrangement.model.basemodels import Event, Person
from icalendar import Calendar
from icalendar import Event as ICalEvent
from sqlalchemy.orm import Session


def create_calendar(session: Session, events: List[Event]):
    """Create a ICAL calendar from a list of events."""
    cal = Calendar()
    cal.add("prodid", "WeBook")

    for event in events:
        ical_event = ICalEvent()
        for planner in event.arrangement.planners:
            ical_event.add("attendee", planner.social_provider_email)

        ical_event.add("organizer", event.responsible.social_provider_email)
        ical_event.add("summary", event.title)
        ical_event.add("dtstart", event.start)
        ical_event.add("dtend", event.end)
        ical_event.add("uid", event.id)

        room_names = ", ".join(room.name for room in event.rooms)
        location_name = event.arrangement.location.name
        if location_name and event.rooms:
            locations = set([room.location for room in event.rooms])
            if len(locations) == 1:
                location_name = locations.pop().name

        ical_event.add(
            "location",
            ((room_names + " på ") if event.rooms else "") + location_name,
        )

        cal.add_component(ical_event)

    return cal.to_ical()
