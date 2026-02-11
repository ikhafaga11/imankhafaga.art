INSERT INTO
    projects (title, cover_image_url)
VALUES
    (
        'Picasso',
        'https://res.cloudinary.com/dm7q2jmog/image/upload/v1770139856/e5b4d3f4-694b-4238-8128-ada81d5bb86a.png'
    ),
    (
        'Leonardo da Vinci',
        'https://res.cloudinary.com/dm7q2jmog/image/upload/v1770139844/bffcf5a8-52da-42be-881b-e5e57d0ba577.png'
    );

INSERT INTO
    project_contents (caption, image_url, project_id)
VALUES
    (
        'Girl Before A Mirror',
        'https://res.cloudinary.com/dm7q2jmog/image/upload/v1770139424/GirlBeforeAMirror_jsmgrx.jpg',
        1
    ),
    (
        'Mona Lisa',
        'https://res.cloudinary.com/dm7q2jmog/image/upload/v1770139362/Mona-Lisa-oil-wood-panel-Leonardo-da_azpakd.webp',
        2
    );

INSERT INTO
    sketches (image_url)
VALUES
    (
        'https://res.cloudinary.com/dm7q2jmog/image/upload/v1770140043/c8b24259-fdee-45ca-ad87-a68bc19893bb.png'
    );

INSERT INTO 
users (username, password)
VALUES 
(
    'ikhafaga1',
    'Password123!'
)