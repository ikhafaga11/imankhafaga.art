DROP TABLE IF EXISTS projects CASCADE;
DROP TABLE IF EXISTS project_contents CASCADE;
DROP TABLE IF EXISTS sketches CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE
    projects (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        cover_image_url VARCHAR(255) NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE
    project_contents (
        id SERIAL PRIMARY KEY,
        caption VARCHAR(255) NOT NULL,
        image_url VARCHAR(255) NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        project_id INTEGER,
        constraint fk_project_id foreign key (project_id) REFERENCES projects (id) ON DELETE CASCADE
    );

CREATE TABLE
    sketches (
        id SERIAL PRIMARY KEY,
        image_url VARCHAR(255) NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE
    users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255),
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );