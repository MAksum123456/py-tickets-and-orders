from django.contrib.auth import get_user_model

from db.models import Order, Ticket, MovieSession
from datetime import datetime


def create_order(
        tickets: list[dict],
        username: str, date:
        datetime = None) -> Order:
    User = get_user_model()
    user, _ = User.objects.get_or_create(username=username)

    order = Order.objects.create(user=user)
    if date:
        order.created_at = date
        order.save()
    for ticket in tickets:
        Ticket.objects.create(
            row=ticket['row'],
            seat=ticket['seat'],
            movie_session=MovieSession.objects.get(id=ticket['movie_session']),
            order=order
        )
    return order
