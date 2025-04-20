from app.database import db
from app.app import create_app

# Create app instance
app = create_app()

# Drop and recreate the database schema
with app.app_context():
    db.drop_all()  # Drop all tables
    db.create_all()  # Create all tables again

print("Database reset successfully.")
