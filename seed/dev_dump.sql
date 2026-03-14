--
-- PostgreSQL database dump
--

\restrict 2eRr1leChoJE5sh9gRCHriB4ckCi6FMWbnjuokfaGWogsE7zHQnyY918pafDX7O

-- Dumped from database version 15.15 (Debian 15.15-1.pgdg13+1)
-- Dumped by pg_dump version 15.15 (Debian 15.15-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: project_contents; Type: TABLE; Schema: public; Owner: iman
--

CREATE TABLE public.project_contents (
    id integer NOT NULL,
    caption character varying(255) NOT NULL,
    image_url character varying(255) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    project_id integer
);


ALTER TABLE public.project_contents OWNER TO iman;

--
-- Name: project_contents_id_seq; Type: SEQUENCE; Schema: public; Owner: iman
--

CREATE SEQUENCE public.project_contents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_contents_id_seq OWNER TO iman;

--
-- Name: project_contents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: iman
--

ALTER SEQUENCE public.project_contents_id_seq OWNED BY public.project_contents.id;


--
-- Name: projects; Type: TABLE; Schema: public; Owner: iman
--

CREATE TABLE public.projects (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    cover_image_url character varying(255) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.projects OWNER TO iman;

--
-- Name: projects_id_seq; Type: SEQUENCE; Schema: public; Owner: iman
--

CREATE SEQUENCE public.projects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.projects_id_seq OWNER TO iman;

--
-- Name: projects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: iman
--

ALTER SEQUENCE public.projects_id_seq OWNED BY public.projects.id;


--
-- Name: sketches; Type: TABLE; Schema: public; Owner: iman
--

CREATE TABLE public.sketches (
    id integer NOT NULL,
    image_url character varying(255) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.sketches OWNER TO iman;

--
-- Name: sketches_id_seq; Type: SEQUENCE; Schema: public; Owner: iman
--

CREATE SEQUENCE public.sketches_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sketches_id_seq OWNER TO iman;

--
-- Name: sketches_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: iman
--

ALTER SEQUENCE public.sketches_id_seq OWNED BY public.sketches.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: iman
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(255),
    password character varying(255),
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO iman;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: iman
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO iman;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: iman
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: project_contents id; Type: DEFAULT; Schema: public; Owner: iman
--

ALTER TABLE ONLY public.project_contents ALTER COLUMN id SET DEFAULT nextval('public.project_contents_id_seq'::regclass);


--
-- Name: projects id; Type: DEFAULT; Schema: public; Owner: iman
--

ALTER TABLE ONLY public.projects ALTER COLUMN id SET DEFAULT nextval('public.projects_id_seq'::regclass);


--
-- Name: sketches id; Type: DEFAULT; Schema: public; Owner: iman
--

ALTER TABLE ONLY public.sketches ALTER COLUMN id SET DEFAULT nextval('public.sketches_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: iman
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: project_contents; Type: TABLE DATA; Schema: public; Owner: iman
--

COPY public.project_contents (id, caption, image_url, created_at, project_id) FROM stdin;
4		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440058/Castle_COLOURED_dnyhb9.jpg	2026-03-13 22:17:21.53818+00	4
5		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440054/Final_castle_background_ighstf.jpg	2026-03-13 22:17:37.314052+00	4
8		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440058/Final_Kitchen_Background_nytjws.jpg	2026-03-13 22:18:28.144369+00	4
10		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440055/Throne_banquet_room_Final_Background_o9bh3b.jpg	2026-03-13 22:19:16.861915+00	4
12		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440522/Animation_background_mfqjie.jpg	2026-03-13 22:24:47.959446+00	5
18		https://res.cloudinary.com/dgszgdizv/image/upload/v1773441587/Project-Storyboard_Updated_f9st3a.png	2026-03-13 22:40:05.348511+00	5
19		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440478/shot_1_beat_board_03_dlnhtj.png	2026-03-13 22:41:58.137663+00	6
23		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440173/Angelica_shapes_experiment_silhuette_qy4jq6.jpg	2026-03-13 22:45:06.429873+00	6
24		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440173/Benicio_Shape_experimentsilhuette_tzxlqg.jpg	2026-03-13 22:45:16.013789+00	6
25		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440478/Lucia_character_colour_concepts_n7pimi.jpg	2026-03-13 22:46:11.588381+00	6
26		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440479/Angelica_colour_schemes_02_bpk3vd.jpg	2026-03-13 22:46:23.994097+00	6
27		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440516/BediounRig_y5psrv.png	2026-03-13 22:57:05.21185+00	7
28		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440484/Expression_and_body_pose_sheet_e1jzzo.png	2026-03-13 22:57:30.293135+00	7
29		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440480/Illustration3_mwd6yh.png	2026-03-13 22:57:45.529122+00	7
30		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440481/Illustration2_hwfybk.png	2026-03-13 22:58:17.25893+00	7
31		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440641/EXT_SCROLLV3-REDUCED_vq3dp0.png	2026-03-13 22:59:30.693365+00	8
32		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440594/BG_EXT_WIN_LADV04_rpjmru.png	2026-03-13 22:59:44.171158+00	8
34		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440480/LAY_EXT_WIN_LADV2_i3iiup.png	2026-03-13 23:00:22.846652+00	8
35		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440414/5PT-LAYV5_jtezzd.png	2026-03-13 23:00:34.402705+00	8
36		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440410/BG_EXT_FISHMARKET03_rqhb67.png	2026-03-13 23:01:09.395075+00	8
37		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440481/Floor_shot.psdEXTENDED_segjaz.png	2026-03-13 23:01:36.696997+00	8
47		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440475/BG_INT_DSK_A_e2nrvs.png	2026-03-13 23:10:07.165171+00	9
49		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440475/BG_INT_OFF_A_h9wg2n.png	2026-03-13 23:10:40.914554+00	9
50		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440404/BG_INT_OFF_B_nn9hts.png	2026-03-13 23:10:52.776492+00	9
53		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440511/LAY_INT_OFF_A_V2_itb2lh.png	2026-03-13 23:11:38.983597+00	9
54		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440475/LAY_INT_OFF_B_V2_2_bzfhpq.png	2026-03-13 23:12:23.087732+00	9
55		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440511/LAY_INT_OFF_A_V2_itb2lh.png	2026-03-13 23:12:38.120197+00	9
56		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440403/LAY_EXT_STR_B_s66t6u.png	2026-03-13 23:12:57.527688+00	9
57		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440954/OctupusNoBG_00044_fxgp8z.png	2026-03-13 23:16:53.801379+00	10
58		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440849/OctupusShotV19_jgjlby.png	2026-03-13 23:17:15.955278+00	10
60		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440462/Octupus_Scene_khb8sc.jpg	2026-03-13 23:18:58.924604+00	10
61		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440536/AboveShotv7_puhwzv.png	2026-03-13 23:19:26.77984+00	10
62		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440400/CloseupVendingMachinev4_wkt7t3.png	2026-03-13 23:19:37.719552+00	10
63		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440399/DoorShotV6_tfeaud.png	2026-03-13 23:19:49.652648+00	10
64		https://res.cloudinary.com/dgszgdizv/image/upload/v1773444222/ImanKhafaga_23100419_CR6001_CoffeeShopEXT_PhotoShop_bzf4zf.png	2026-03-13 23:24:09.52495+00	11
65		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440971/Tutorial_EP02_Value_Tones_m1rbkm.png	2026-03-13 23:24:20.314182+00	11
67		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440504/INT_BG_CLOCK_0270_xqwxpo.png	2026-03-13 23:24:57.485856+00	11
69		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440551/INT_LAY_CLOCK_0270_Value-FG_mb5fna.png	2026-03-13 23:25:23.685618+00	11
71		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440611/INT_BG_PORTAFILTERPULL_0220_f1ttmk.png	2026-03-13 23:26:09.596315+00	11
72		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440546/INT_LAY_PORTAFILTERPULL_0220_Values_yc87fo.png	2026-03-13 23:26:29.137709+00	11
73		https://res.cloudinary.com/dgszgdizv/image/upload/v1773440557/EXT_LAY_SEATS_0190_iu7lay.png	2026-03-13 23:26:52.749413+00	11
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: iman
--

COPY public.projects (id, title, cover_image_url, created_at) FROM stdin;
4	The Kings Chef	https://res.cloudinary.com/dgszgdizv/image/upload/v1773440058/Castle_COLOURED_dnyhb9.jpg	2026-03-13 22:16:50.294824+00
5	Walkies	https://res.cloudinary.com/dgszgdizv/image/upload/v1773441101/Screenshot_2026-03-13_223044_dv0yrr.png	2026-03-13 22:24:21.890055+00
6	Lucia	https://res.cloudinary.com/dgszgdizv/image/upload/v1773440478/shot_1_beat_board_03_dlnhtj.png	2026-03-13 22:41:49.800109+00
7	Bedioun_Rig	https://res.cloudinary.com/dgszgdizv/image/upload/v1773442595/Screenshot_2026-03-13_225421_mwmpsr.png	2026-03-13 22:56:46.355076+00
8	Fishy Business	https://res.cloudinary.com/dgszgdizv/image/upload/v1773443080/Screenshot_2026-03-13_230400_ft4g5z.png	2026-03-13 22:59:06.586401+00
9	Ate	https://res.cloudinary.com/dgszgdizv/image/upload/v1773440475/LAY_INT_OFF_B_V2_2_bzfhpq.png	2026-03-13 23:06:04.607886+00
10	Washed Under	https://res.cloudinary.com/dgszgdizv/image/upload/v1773440954/OctupusNoBG_00044_fxgp8z.png	2026-03-13 23:16:45.615832+00
11	Symphony Of The Morning Rush	https://res.cloudinary.com/dgszgdizv/image/upload/v1773444222/ImanKhafaga_23100419_CR6001_CoffeeShopEXT_PhotoShop_bzf4zf.png	2026-03-13 23:23:54.463746+00
\.


--
-- Data for Name: sketches; Type: TABLE DATA; Schema: public; Owner: iman
--

COPY public.sketches (id, image_url, created_at) FROM stdin;
1	https://res.cloudinary.com/dgszgdizv/image/upload/v1773444543/Illustration4_1_cvla2y.png	2026-03-14 00:17:47.563879+00
2	https://res.cloudinary.com/dgszgdizv/image/upload/v1773446115/IMG_1540_oo9xto.jpg	2026-03-14 00:17:57.963389+00
6	https://res.cloudinary.com/dgszgdizv/image/upload/v1773446479/IMG_1549_drdwqg.jpg	2026-03-14 00:18:45.929777+00
7	https://res.cloudinary.com/dgszgdizv/image/upload/v1773446636/Character_Turnaround_animation_qec1st.gif	2026-03-14 00:19:02.52276+00
8	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447395/jhvjhvj_tiextt.jpg	2026-03-14 00:19:16.755707+00
9	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447404/WhatsApp_Image_2026-03-14_at_00.08.30_sspqo3.jpg	2026-03-14 00:19:31.86394+00
10	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447408/WhatsApp_Image_2026-03-13_at_23.51.35_wgprtn.jpg	2026-03-14 00:19:41.892436+00
11	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447413/WhatsApp_Image_2026-03-14_at_00.12.57_2_p0rtco.jpg	2026-03-14 00:19:50.618266+00
12	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447418/ugyfv_besdh2.jpg	2026-03-14 00:20:03.291655+00
14	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447422/WhatsApp_Image_2026-03-14_at_00.12.57_1_hyobzl.jpg	2026-03-14 00:20:22.445111+00
15	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447427/fvjl_votuub.jpg	2026-03-14 00:20:38.514942+00
16	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447438/gh_pfzrkk.jpg	2026-03-14 00:20:50.562947+00
17	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447442/ghcjgcdj_uyblsi.jpg	2026-03-14 00:21:03.238937+00
18	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447447/gvkgvk_bkutwx.jpg	2026-03-14 00:21:18.395156+00
20	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447457/hjglhg_gsyos2.jpg	2026-03-14 00:21:37.880792+00
31	https://res.cloudinary.com/dgszgdizv/image/upload/v1773447527/IMG_1540_tpzkj8.jpg	2026-03-14 20:03:09.333912+00
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: iman
--

COPY public.users (id, username, password, created_at) FROM stdin;
1	imankaty	Iman1996!	2026-02-11 19:14:12.945607+00
\.


--
-- Name: project_contents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: iman
--

SELECT pg_catalog.setval('public.project_contents_id_seq', 73, true);


--
-- Name: projects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: iman
--

SELECT pg_catalog.setval('public.projects_id_seq', 11, true);


--
-- Name: sketches_id_seq; Type: SEQUENCE SET; Schema: public; Owner: iman
--

SELECT pg_catalog.setval('public.sketches_id_seq', 31, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: iman
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: project_contents project_contents_pkey; Type: CONSTRAINT; Schema: public; Owner: iman
--

ALTER TABLE ONLY public.project_contents
    ADD CONSTRAINT project_contents_pkey PRIMARY KEY (id);


--
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: iman
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);


--
-- Name: sketches sketches_pkey; Type: CONSTRAINT; Schema: public; Owner: iman
--

ALTER TABLE ONLY public.sketches
    ADD CONSTRAINT sketches_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: iman
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: project_contents fk_project_id; Type: FK CONSTRAINT; Schema: public; Owner: iman
--

ALTER TABLE ONLY public.project_contents
    ADD CONSTRAINT fk_project_id FOREIGN KEY (project_id) REFERENCES public.projects(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

\unrestrict 2eRr1leChoJE5sh9gRCHriB4ckCi6FMWbnjuokfaGWogsE7zHQnyY918pafDX7O

