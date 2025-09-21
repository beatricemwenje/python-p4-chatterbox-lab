#!/usr/bin/env python3
from app import app
from models import db, Message

with app.app_context():
    # Clear out existing messages
    Message.query.delete()

    # Add new messages
    m1 = Message(body="Hello World!", username="alice")
    m2 = Message(body="Flask is awesome!", username="bob")
    m3 = Message(body="Seeding works!", username="charlie")

    db.session.add_all([m1, m2, m3])
    db.session.commit()

    print("Database seeded!")
