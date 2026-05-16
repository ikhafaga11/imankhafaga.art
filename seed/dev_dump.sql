-- 1. Setup Environment
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;

-- 2. Create Tables
CREATE TABLE IF NOT EXISTS public.projects (
    id SERIAL PRIMARY KEY,
    title character varying(255) NOT NULL,
    cover_image_url character varying(255) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.project_contents (
    id SERIAL PRIMARY KEY,
    caption character varying(255) NOT NULL,
    image_url character varying(255) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    project_id integer REFERENCES public.projects(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS public.sketches (
    id SERIAL PRIMARY KEY,
    image_url character varying(255) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    username character varying(255),
    password character varying(255),
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

-- 3. Insert Data: Projects
INSERT INTO public.projects (id, title, cover_image_url, created_at) VALUES
(4, 'The Kings Chef', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773440058/Castle_COLOURED_dnyhb9.jpg', '2026-03-13 22:16:50'),
(5, 'Walkies', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773441101/Screenshot_2026-03-13_223044_dv0yrr.png', '2026-03-13 22:24:21'),
(6, 'Lucia', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773440478/shot_1_beat_board_03_dlnhtj.png', '2026-03-13 22:41:49'),
(7, 'Bedioun_Rig', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773442595/Screenshot_2026-03-13_225421_mwmpsr.png', '2026-03-13 22:56:46'),
(8, 'Fishy Business', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773443080/Screenshot_2026-03-13_230400_ft4g5z.png', '2026-03-13 22:59:06'),
(9, 'Ate', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773440475/LAY_INT_OFF_B_V2_2_bzfhpq.png', '2026-03-13 23:06:04'),
(10, 'Washed Under', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773440954/OctupusNoBG_00044_fxgp8z.png', '2026-03-13 23:16:45'),
(11, 'Symphony Of The Morning Rush', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773444222/ImanKhafaga_23100419_CR6001_CoffeeShopEXT_PhotoShop_bzf4zf.png', '2026-03-13 23:23:54')
ON CONFLICT (id) DO NOTHING;

-- 4. Insert Data: Project Contents
INSERT INTO public.project_contents (id, caption, image_url, created_at, project_id) VALUES
(4, 'Castle Coloured', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773440058/Castle_COLOURED_dnyhb9.jpg', '2026-03-13 22:17:21', 4),
(5, 'Final Castle BG', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773440054/Final_castle_background_ighstf.jpg', '2026-03-13 22:17:37', 4),
(12, 'Animation BG', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773440522/Animation_background_mfqjie.jpg', '2026-03-13 22:24:47', 5),
(64, 'Coffee Shop EXT', 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773444222/ImanKhafaga_23100419_CR6001_CoffeeShopEXT_PhotoShop_bzf4zf.png', '2026-03-13 23:24:09', 11)
ON CONFLICT (id) DO NOTHING;

-- 5. Insert Data: Sketches
INSERT INTO public.sketches (id, image_url, created_at) VALUES
(1, 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773444543/Illustration4_1_cvla2y.png', '2026-03-14 00:17:47'),
(31, 'https://res.cloudinary.com/dgszgdizv/image/upload/v1773447527/IMG_1540_tpzkj8.jpg', '2026-03-14 20:03:09')
ON CONFLICT (id) DO NOTHING;

-- 6. Insert Data: Users
INSERT INTO public.users (id, username, password, created_at) VALUES
(1, 'imankaty', 'Iman1996!', '2026-02-11 19:14:12')
ON CONFLICT (id) DO NOTHING;

-- 7. Sync ID Sequences (Crucial for Postgres SERIAL types)
SELECT setval('projects_id_seq', (SELECT MAX(id) FROM projects));
SELECT setval('project_contents_id_seq', (SELECT MAX(id) FROM project_contents));
SELECT setval('sketches_id_seq', (SELECT MAX(id) FROM sketches));
SELECT setval('users_id_seq', (SELECT MAX(id) FROM users));