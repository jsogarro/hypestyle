"""Migrate Tables

Creates our database tables
"""
from config.db import db

def migrate_tables():
    print('migrate tables')
    # db.create_all()

if __name__ == '__main__':
    migrate_tables()
