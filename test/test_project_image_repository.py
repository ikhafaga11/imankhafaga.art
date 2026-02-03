from lib.project_image_repository import ProjectImageRepository

def test_get_all_project_images(db_connection):
    db_connection.seed('seeds/database_connection.sql')
    repo = ProjectImageRepository(db_connection)
    results = repo.get_all_project_images(1)
    
    assert len(results) == 1