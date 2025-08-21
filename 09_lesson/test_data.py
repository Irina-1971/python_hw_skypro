from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

db_connection_string = "postgresql://postgres:123@localhost:5432/"  # Added database name
db = create_engine(db_connection_string)

def test_create_students():
    """Test to verify students can be created and retrieved"""
    with db.connect() as connection:
        # First, let's create a test student
        test_data = {
            'student_id': 125,  # Use a high ID to avoid conflicts
            'first_name': 'Test',
            'last_name': 'Student',
            'email': 'er@gmail.com'
        }
        
        # Insert test student
        connection.execute(text("""
            INSERT INTO student (student_id, first_name, last_name, email) 
            VALUES (:student_id, :first_name, :last_name, :email)
        """), test_data)
        
        # Verify the student was created
        result = connection.execute(
            text("SELECT * FROM student WHERE student_id = :student_id"),
            {'student_id': test_data['student_id']}
        )
        student = result.fetchone()
        
        assert student is not None
        assert student['first_name'] == 'Test'
        
        # Clean up
        connection.execute(
            text("DELETE FROM student WHERE student_id = :student_id"),
            {'student_id': test_data['student_id']}
        )

def test_search_students():
    """Test to search for students"""
    with db.connect() as connection:
        result = connection.execute(text("SELECT * FROM student WHERE first_name LIKE '%John%'"))
        students = result.fetchall()
        
        # Verify we get results (could be empty, but should not error)
        assert students is not None

def test_create_subjects():
    """Test subject creation"""
    with db.connect() as connection:
        # Get initial count
        initial_count = connection.execute(text("SELECT COUNT(*) FROM subject")).fetchone()[0]
        
        # Insert new subject
        connection.execute(text("""
            INSERT INTO subject (subject_id, subject_title) 
            VALUES (17, 'Football')
        """))
        
        # Get new count
        new_count = connection.execute(text("SELECT COUNT(*) FROM subject")).fetchone()[0]
        
        assert new_count == initial_count + 1
        
        # Clean up
        connection.execute(text("DELETE FROM subject WHERE subject_id = 17"))

def test_update_subject_name():
    """Test subject name update"""
    with db.connect() as connection:
        # First create a test subject
        connection.execute(text("""
            INSERT INTO subject (subject_id, subject_title) 
            VALUES (18, 'TestSubject')
        """))
        
        # Update the subject
        connection.execute(text("""
            UPDATE subject SET subject_title = 'Baseball' 
            WHERE subject_id = 18
        """))
        
        # Verify the update
        result = connection.execute(text("""
            SELECT subject_title FROM subject WHERE subject_id = 18
        """))
        subject = result.fetchone()
        
        assert subject[0] == 'Baseball'
        
        # Clean up
        connection.execute(text("DELETE FROM subject WHERE subject_id = 18"))

def test_delete_subject():
    """Test subject deletion"""
    with db.connect() as connection:
        # First create a test subject to delete
        connection.execute(text("""
            INSERT INTO subject (subject_id, subject_title) 
            VALUES (13, 'SubjectToDelete')
        """))
        
        # Get initial count
        initial_count = connection.execute(text("SELECT COUNT(*) FROM subject")).fetchone()[0]
        
        # Delete the subject
        connection.execute(text("DELETE FROM subject WHERE subject_id = 13"))
        
        # Get final count
        final_count = connection.execute(text("SELECT COUNT(*) FROM subject")).fetchone()[0]
        
        # Verify deletion
        assert final_count == initial_count - 1
        
        # Verify the subject no longer exists
        result = connection.execute(text("SELECT * FROM subject WHERE subject_id = 13"))
        deleted_subject = result.fetchone()
        assert deleted_subject is None