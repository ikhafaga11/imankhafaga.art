from lib.project_content_repository import ProjectContentRepository


def test_get_all_project_images(db_connection):
    db_connection.seed("db/seed.sql")
    repo = ProjectContentRepository(db_connection)
    results = repo.get_project_contents(1)

    assert len(results) == 1
