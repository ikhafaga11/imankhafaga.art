def test_database_connection_projects_table(db_connection):
    db_connection.seed("seeds/database_connection.sql")
    result = db_connection.execute("SELECT * FROM projects")
    assert len(result) == 2

    
def test_database_connection_project_images_table(db_connection):
    db_connection.seed("seeds/database_connection.sql")
    result = db_connection.execute("SELECT * FROM project_images WHERE id = 1")
    assert len(result) == 1

def test_database_connection_sketchs_table(db_connection):
    db_connection.seed("seeds/database_connection.sql")
    result = db_connection.execute("SELECT * FROM sketchs")
    assert len(result) == 1
