from models.models import Event


def return_events_with_draws():
    events = Event.query.all()
    draws_set = []
    for event in events:
        if event.draw_set:
            draws_set.append(event.event_id)
    return draws_set
