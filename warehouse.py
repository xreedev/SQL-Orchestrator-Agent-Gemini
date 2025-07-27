import sqlite3


class DataBase:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

        # Create subjects table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')

        # Create teachers table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject_id INTEGER,
            FOREIGN KEY(subject_id) REFERENCES subjects(id)
        )
        ''')

        # Create marks table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            subject_id INTEGER,
            marks INTEGER,
            FOREIGN KEY(subject_id) REFERENCES subjects(id)
        )
        ''')

        self.connection.commit()

    def insert_sample_data(self):
        # Insert sample subjects
        subjects = [('Maths',), ('English',), ('Science',)]
        self.cursor.executemany('INSERT INTO subjects (name) VALUES (?)', subjects)

        # Fetch subject IDs
        self.cursor.execute('SELECT id, name FROM subjects')
        subject_ids = {name: id for id, name in self.cursor.fetchall()}

        # Insert sample teachers
        teachers = [
            ('Alice Johnson', subject_ids['Maths']),
            ('Bob Smith', subject_ids['English']),
            ('Carol Lee', subject_ids['Science']),
        ]
        self.cursor.executemany('INSERT INTO teachers (name, subject_id) VALUES (?, ?)', teachers)

        # Insert sample marks
        marks = [
            ('John Doe', subject_ids['Maths'], 85),
            ('Jane Doe', subject_ids['English'], 92),
            ('John Doe', subject_ids['Science'], 78),
            ('Jane Doe', subject_ids['Maths'], 88),
            ('Tom Brown', subject_ids['English'], 75),
        ]
        self.cursor.executemany('INSERT INTO marks (student_name, subject_id, marks) VALUES (?, ?, ?)', marks)

        self.connection.commit()

    def get_data(self, query, params=None):
        if params is None:
            params = ()

        self.cursor.execute(query, params)
        return self.cursor.fetchall()


