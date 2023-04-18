import sqlite3
from models import Entry, Mood


def get_all_entries():
    """gets all the entries"""
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date
        FROM entries e
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            entry = Entry(row['id'], row['concept'], row['entry'], row['mood_id'],
                          row['date'])

            # Create a Location instance from the current row
            # location = Location(
            #     row['location_id'], row['location_name'], row['location_address'])
            # # Create a Customer instance from the current row
            # customer = Customer(
            #     row['customer_id'], row['customer_name'], row['customer_address'], row['customer_email'], row['customer_password'])

        #     self.id = id
        # self.name = name
        # self.address = address
        # self.email = email
        # self.password = password

            # Add the dictionary representation of the location to the animal
            # animal.location = location.__dict__
            # # Add the dictionary representation of the customer to the animal
            # animal.customer = customer.__dict__

            # Add the dictionary representation of the animal to the list
            entries.append(entry.__dict__)
            # entries.append(customer.__dict__)

    return entries
