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
            e.date,
            m.label mood
        FROM entries e
        JOIN moods m
            ON m.id = e.mood_id
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            entry = Entry(
                row['id'],
                row['concept'],
                row['entry'],
                row['mood_id'],
                row['date']
            )
            mood = Mood(
                row['mood_id'],
                row['mood']
            )

            entry.mood = mood.__dict__

            entries.append(entry.__dict__)

    return entries


def get_single_entry(id):
    """gets a single entry"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date,
            m.label mood
        FROM entries e
        JOIN moods m
            ON m.id = e.mood_id
        WHERE e.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(
            data['id'],
            data['concept'],
            data['entry'],
            data['mood_id'],
            data['date']
        )

        mood = Mood(
            data['mood_id'],
            data['mood']
        )

        entry.mood = mood.__dict__

        return entry.__dict__


def get_entries_by_search(search_param):
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
        WHERE e.entry LIKE ? OR e.concept LIKE ?
        """, ('%' + search_param + '%', '%' + search_param + '%'))

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            entry = Entry(
                row['id'],
                row['concept'],
                row['entry'],
                row['mood_id'],
                row['date']
            )

            entries.append(entry.__dict__)

    return entries


def create_entry(new_entry):
    """Creates a new entry"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO entries
            ( concept, entry, mood_id, date )
        VALUES
            ( ?, ?, ?, ? );
        """, (
            new_entry['concept'],
            new_entry['entry'],
            new_entry['mood_id'],
            new_entry['date'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id

    return new_entry


def update_entry(id, new_entry):
    """Updates Entry with Replacement"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE entries
            SET
                concept = ?,
                entry = ?,
                mood_id = ?,
                date = ?
        WHERE id = ?
        """, (
            new_entry['concept'],
            new_entry['entry'],
            new_entry['mood_id'],
            new_entry['date'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def delete_entry(id):
    """Deletes single entry"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))
