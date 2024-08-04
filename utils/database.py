import sqlite3


class Database:
    def __init__(self, db_name='bugs.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bugs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                description TEXT,
                status TEXT,
                priority TEXT,
                rewarded BOOLEAN
            )
        ''')
        self.conn.commit()

    def add_bug(self, user_id, description, status, priority):
        self.cursor.execute('''
            INSERT INTO bugs (user_id, description, status, priority, rewarded)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, description, status, priority, False))
        self.conn.commit()

    def get_bugs(self, user_id):
        self.cursor.execute('SELECT * FROM bugs WHERE user_id = ?', (user_id,))
        return self.cursor.fetchall()

    def update_bug_status(self, bug_id, status):
        self.cursor.execute('UPDATE bugs SET status = ? WHERE id = ?', (status, bug_id))
        self.conn.commit()

    def reward_bug(self, bug_id):
        self.cursor.execute('UPDATE bugs SET rewarded = ? WHERE id = ?', (True, bug_id))
        self.conn.commit()

    def delete_bug(self, bug_id):
        self.cursor.execute('DELETE FROM bugs WHERE id = ?', (bug_id,))
        self.conn.commit()

    def get_all_bugs(self):
        self.cursor.execute('SELECT * FROM bugs')
        return self.cursor.fetchall()

db = Database()
