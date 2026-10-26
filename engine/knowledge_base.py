"""
FlixMatch AI Knowledge Base
Streaming & Reading Recommendation Knowledge Base
Contains official IMDb / Wikipedia posters, metadata, and production rules.
"""

from typing import Dict, List, Any

# ==============================================================================
# 1. CATALOG ITEMS (Movies & Books with Official IMDb/Wikipedia Posters & Metadata)
# ==============================================================================

CATALOG_ITEMS: List[Dict[str, Any]] = [
    # ----------------------------- MOVIES -------------------------------------
    {
        "id": "mov_01",
        "type": "movie",
        "title": "Interstellar",
        "year": 2014,
        "director_or_author": "Christopher Nolan",
        "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Michael Caine"],
        "genres": ["Sci-Fi", "Adventure", "Drama"],
        "moods": ["reflective", "curious", "melancholic", "tense"],
        "cognitive_load": "deeply_philosophical",
        "tempo": "slow_burn",
        "companions": ["solo", "date_night", "friends"],
        "eras": ["contemporary", "modern"],
        "tones": ["intellectual", "epic", "emotional", "scientific"],
        "rating": 8.7,
        "age_rating": "13+",
        "quality": "4K Ultra HD",
        "runtime_or_pages": "2h 49m",
        "synopsis": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft along with a team of researchers to find a new planet for humans.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/xJHokMbljvjADYdit5fK5VQsXEG.jpg",
        "tags": ["space", "time_dilation", "existential", "father_daughter", "physics"],
        "streaming_or_publisher": "Paramount+ / Prime Video",
        "cross_media_rec": "bk_02"  # Project Hail Mary
    },
    {
        "id": "mov_02",
        "type": "movie",
        "title": "Inception",
        "year": 2010,
        "director_or_author": "Christopher Nolan",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page", "Tom Hardy"],
        "genres": ["Sci-Fi", "Action", "Thriller"],
        "moods": ["tense", "curious", "adventurous"],
        "cognitive_load": "mind_bending",
        "tempo": "fast_paced",
        "companions": ["solo", "friends", "date_night"],
        "eras": ["modern", "contemporary"],
        "tones": ["intellectual", "thrilling", "complex"],
        "rating": 8.8,
        "age_rating": "16+",
        "quality": "4K HDR",
        "runtime_or_pages": "2h 28m",
        "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg",
        "tags": ["dreams", "heist", "mind_bending", "psychological", "subconscious"],
        "streaming_or_publisher": "Netflix / Apple TV",
        "cross_media_rec": "bk_08"  # The Silent Patient
    },
    {
        "id": "mov_03",
        "type": "movie",
        "title": "The Grand Budapest Hotel",
        "year": 2014,
        "director_or_author": "Wes Anderson",
        "cast": ["Ralph Fiennes", "Tony Revolori", "Saoirse Ronan", "Willem Dafoe"],
        "genres": ["Comedy", "Adventure", "Drama"],
        "moods": ["joyful", "reflective", "curious"],
        "cognitive_load": "balanced",
        "tempo": "fast_paced",
        "companions": ["date_night", "friends", "family", "solo"],
        "eras": ["contemporary", "vintage_stylized"],
        "tones": ["whimsical", "aesthetic", "witty", "comforting"],
        "rating": 8.1,
        "age_rating": "16+",
        "quality": "HD",
        "runtime_or_pages": "1h 39m",
        "synopsis": "A writer encounters the owner of an aging high-class European hotel, who recounts his years serving as a lobby boy under an exceptional concierge in the hotel's glory years.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/1/1c/The_Grand_Budapest_Hotel.png",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/1/1c/The_Grand_Budapest_Hotel.png",
        "tags": ["symmetry", "quirky", "friendship", "pastel", "art_house"],
        "streaming_or_publisher": "Disney+ / Hulu",
        "cross_media_rec": "bk_07"  # Hitchhiker's Guide
    },
    {
        "id": "mov_04",
        "type": "movie",
        "title": "Spirited Away",
        "year": 2001,
        "director_or_author": "Hayao Miyazaki",
        "cast": ["Rumi Hiiragi", "Miyu Irino", "Mari Natsuki"],
        "genres": ["Animation", "Fantasy", "Adventure"],
        "moods": ["reflective", "joyful", "curious", "exhausted"],
        "cognitive_load": "balanced",
        "tempo": "moderate",
        "companions": ["solo", "family", "date_night"],
        "eras": ["modern", "classic"],
        "tones": ["comforting", "magical", "nostalgic", "wholesome"],
        "rating": 8.6,
        "age_rating": "All Ages",
        "quality": "4K Remastered",
        "runtime_or_pages": "2h 05m",
        "synopsis": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits where humans are changed into beasts.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png",
        "tags": ["anime", "folklore", "coming_of_age", "healing", "visually_stunning"],
        "streaming_or_publisher": "Max / Netflix",
        "cross_media_rec": "bk_05"  # The Midnight Library
    },
    {
        "id": "mov_05",
        "type": "movie",
        "title": "Parasite",
        "year": 2019,
        "director_or_author": "Bong Joon-ho",
        "cast": ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong", "Choi Woo-shik"],
        "genres": ["Thriller", "Drama", "Dark Comedy"],
        "moods": ["tense", "curious", "reflective"],
        "cognitive_load": "mind_bending",
        "tempo": "intense",
        "companions": ["friends", "date_night", "solo"],
        "eras": ["contemporary"],
        "tones": ["dark_gritty", "satirical", "intellectual", "unpredictable"],
        "rating": 8.5,
        "age_rating": "18+",
        "quality": "4K Ultra HD",
        "runtime_or_pages": "2h 12m",
        "synopsis": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/5/53/Parasite_%282019_film%29.png",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/5/53/Parasite_%282019_film%29.png",
        "tags": ["social_class", "twist", "korean_cinema", "masterpiece", "suspense"],
        "streaming_or_publisher": "Max / Prime Video",
        "cross_media_rec": "bk_08"  # The Silent Patient
    },
    {
        "id": "mov_06",
        "type": "movie",
        "title": "Whiplash",
        "year": 2014,
        "director_or_author": "Damien Chazelle",
        "cast": ["Miles Teller", "J.K. Simmons", "Melissa Benoist", "Paul Reiser"],
        "genres": ["Drama", "Music"],
        "moods": ["tense", "adventurous"],
        "cognitive_load": "mind_bending",
        "tempo": "intense",
        "companions": ["solo", "friends"],
        "eras": ["contemporary"],
        "tones": ["adrenaline", "obsessive", "high_stakes", "raw"],
        "rating": 8.5,
        "age_rating": "16+",
        "quality": "HD",
        "runtime_or_pages": "1h 46m",
        "synopsis": "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
        "tags": ["jazz", "ambition", "psychological_pressure", "perfectionism"],
        "streaming_or_publisher": "Sony Pictures / Netflix",
        "cross_media_rec": "bk_03"  # Atomic Habits
    },
    {
        "id": "mov_07",
        "type": "movie",
        "title": "Spider-Man: Into the Spider-Verse",
        "year": 2018,
        "director_or_author": "Bob Persichetti, Peter Ramsey",
        "cast": ["Shameik Moore", "Jake Johnson", "Hailee Steinfeld", "Mahershala Ali"],
        "genres": ["Animation", "Action", "Sci-Fi"],
        "moods": ["joyful", "adventurous", "exhausted"],
        "cognitive_load": "light_easy",
        "tempo": "fast_paced",
        "companions": ["friends", "family", "party", "solo"],
        "eras": ["contemporary"],
        "tones": ["uplifting", "stylish", "humorous", "vibrant"],
        "rating": 8.4,
        "age_rating": "PG",
        "quality": "4K HDR",
        "runtime_or_pages": "1h 57m",
        "synopsis": "Teen Miles Morales becomes the new Spider-Man and joins other Spider-Heroes from parallel dimensions to halt a threat to all reality.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/f/fa/Spider-Man_Into_the_Spider-Verse_poster.png",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/f/fa/Spider-Man_Into_the_Spider-Verse_poster.png",
        "tags": ["multiverse", "comic_art", "hip_hop_soundtrack", "coming_of_age"],
        "streaming_or_publisher": "Disney+ / Apple TV",
        "cross_media_rec": "bk_07"
    },
    {
        "id": "mov_08",
        "type": "movie",
        "title": "Blade Runner 2049",
        "year": 2017,
        "director_or_author": "Denis Villeneuve",
        "cast": ["Ryan Gosling", "Harrison Ford", "Ana de Armas", "Sylvia Hoeks"],
        "genres": ["Sci-Fi", "Mystery", "Drama"],
        "moods": ["reflective", "melancholic", "tense"],
        "cognitive_load": "deeply_philosophical",
        "tempo": "slow_burn",
        "companions": ["solo"],
        "eras": ["contemporary"],
        "tones": ["cyberpunk", "existential", "neo_noir", "atmospheric"],
        "rating": 8.0,
        "age_rating": "16+",
        "quality": "4K Ultra HD",
        "runtime_or_pages": "2h 44m",
        "synopsis": "Young Blade Runner K's discovery of a long-buried secret leads him to track down former Blade Runner Rick Deckard, who's been missing for thirty years.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/9/9b/Blade_Runner_2049_poster.png",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/9/9b/Blade_Runner_2049_poster.png",
        "tags": ["cyberpunk", "identity", "artificial_intelligence", "roger_deakins"],
        "streaming_or_publisher": "Max / Apple TV",
        "cross_media_rec": "bk_04"  # Klara and the Sun
    },
    {
        "id": "mov_09",
        "type": "movie",
        "title": "Paddington 2",
        "year": 2017,
        "director_or_author": "Paul King",
        "cast": ["Hugh Bonneville", "Sally Hawkins", "Hugh Grant", "Brendan Gleeson"],
        "genres": ["Comedy", "Adventure", "Family"],
        "moods": ["joyful", "exhausted", "reflective"],
        "cognitive_load": "light_easy",
        "tempo": "moderate",
        "companions": ["family", "date_night", "solo", "friends"],
        "eras": ["contemporary"],
        "tones": ["wholesome", "comforting", "uplifting", "heartwarming"],
        "rating": 7.8,
        "age_rating": "All Ages",
        "quality": "HD",
        "runtime_or_pages": "1h 43m",
        "synopsis": "Paddington, now settled with the Brown family, picks up odd jobs to buy a pop-up book for Aunt Lucy's birthday, only to be framed when the book is stolen.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/b/b6/Paddington_2_poster.jpg",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/b/b6/Paddington_2_poster.jpg",
        "tags": ["pure_joy", "kindness", "london", "feel_good"],
        "streaming_or_publisher": "Prime Video",
        "cross_media_rec": "bk_05"
    },
    {
        "id": "mov_10",
        "type": "movie",
        "title": "Everything Everywhere All at Once",
        "year": 2022,
        "director_or_author": "Daniel Kwan, Daniel Scheinert",
        "cast": ["Michelle Yeoh", "Stephanie Hsu", "Ke Huy Quan", "Jamie Lee Curtis"],
        "genres": ["Sci-Fi", "Action", "Comedy", "Fantasy"],
        "moods": ["adventurous", "reflective", "joyful", "tense"],
        "cognitive_load": "mind_bending",
        "tempo": "fast_paced",
        "companions": ["friends", "date_night", "solo"],
        "eras": ["contemporary"],
        "tones": ["absurdist", "existential", "emotional", "creative"],
        "rating": 7.8,
        "age_rating": "16+",
        "quality": "4K HDR",
        "runtime_or_pages": "2h 19m",
        "synopsis": "A middle-aged Chinese immigrant is swept into an insane adventure in which she alone can save the existence of multiverse by exploring alternative lives.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/1/1e/Everything_Everywhere_All_at_Once.jpg",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/1/1e/Everything_Everywhere_All_at_Once.jpg",
        "tags": ["multiverse", "absurdism", "family_healing", "nihilism_vs_love", "a24"],
        "streaming_or_publisher": "Paramount+ / Showtime",
        "cross_media_rec": "bk_05"
    },
    {
        "id": "mov_11",
        "type": "movie",
        "title": "The Shawshank Redemption",
        "year": 1994,
        "director_or_author": "Frank Darabont",
        "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"],
        "moods": ["reflective", "melancholic", "joyful"],
        "cognitive_load": "balanced",
        "tempo": "moderate",
        "companions": ["solo", "friends", "family"],
        "eras": ["classic", "modern"],
        "tones": ["uplifting", "hopeful", "triumphant", "profound"],
        "rating": 9.3,
        "age_rating": "16+",
        "quality": "4K Ultra HD",
        "runtime_or_pages": "2h 22m",
        "synopsis": "A banker convicted of murder bonds with a contraband-smuggling fellow inmate over decades, finding solace and eventual redemption through acts of common decency.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
        "tags": ["hope", "prison_break", "friendship", "patience", "all_time_great"],
        "streaming_or_publisher": "Netflix / Apple TV",
        "cross_media_rec": "bk_03"
    },
    {
        "id": "mov_12",
        "type": "movie",
        "title": "Knives Out",
        "year": 2019,
        "director_or_author": "Rian Johnson",
        "cast": ["Daniel Craig", "Chris Evans", "Ana de Armas", "Jamie Lee Curtis"],
        "genres": ["Mystery", "Comedy", "Crime"],
        "moods": ["curious", "joyful", "adventurous"],
        "cognitive_load": "balanced",
        "tempo": "moderate",
        "companions": ["friends", "family", "date_night"],
        "eras": ["contemporary"],
        "tones": ["witty", "satirical", "puzzle", "clever"],
        "rating": 7.9,
        "age_rating": "13+",
        "quality": "4K Ultra HD",
        "runtime_or_pages": "2h 10m",
        "synopsis": "A detective investigates the death of a patriarch of an eccentric, combative family who gathers at his estate for his 85th birthday.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/1/1f/Knives_Out_poster.jpeg",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/1/1f/Knives_Out_poster.jpeg",
        "tags": ["whodunit", "agatha_christie_style", "daniel_craig", "mansion"],
        "streaming_or_publisher": "Netflix / Prime Video",
        "cross_media_rec": "bk_08"
    },
    {
        "id": "mov_13",
        "type": "movie",
        "title": "The Dark Knight",
        "year": 2008,
        "director_or_author": "Christopher Nolan",
        "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
        "genres": ["Action", "Crime", "Drama", "Thriller"],
        "moods": ["tense", "adventurous", "reflective"],
        "cognitive_load": "mind_bending",
        "tempo": "fast_paced",
        "companions": ["friends", "solo", "date_night"],
        "eras": ["modern"],
        "tones": ["dark_gritty", "high_stakes", "epic", "intellectual"],
        "rating": 9.0,
        "age_rating": "16+",
        "quality": "4K Ultra HD",
        "runtime_or_pages": "2h 32m",
        "synopsis": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/1/1c/The_Dark_Knight_%282008_film%29.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg",
        "tags": ["joker", "batman", "chaos", "heroism", "masterpiece"],
        "streaming_or_publisher": "Max / Prime Video",
        "cross_media_rec": "bk_08"
    },
    {
        "id": "mov_14",
        "type": "movie",
        "title": "Dune",
        "year": 2021,
        "director_or_author": "Denis Villeneuve",
        "cast": ["Timothée Chalamet", "Rebecca Ferguson", "Oscar Isaac", "Zendaya"],
        "genres": ["Sci-Fi", "Adventure", "Drama"],
        "moods": ["reflective", "tense", "curious"],
        "cognitive_load": "deeply_philosophical",
        "tempo": "slow_burn",
        "companions": ["solo", "date_night", "friends"],
        "eras": ["contemporary"],
        "tones": ["epic", "intellectual", "mystical", "atmospheric"],
        "rating": 8.0,
        "age_rating": "13+",
        "quality": "4K Dolby Vision",
        "runtime_or_pages": "2h 35m",
        "synopsis": "Paul Atreides arrives on Arrakis after his father accepts the stewardship of the dangerous planet. However, chaos ensues after a betrayal as forces clash over the world's most valuable resource.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/8/8e/Dune_%282021_film%29.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/lzWHmYdfeFiMIY4JaMmtR7GEli3.jpg",
        "tags": ["arrakis", "spice", "sandworms", "destiny", "hans_zimmer"],
        "streaming_or_publisher": "Max / Netflix",
        "cross_media_rec": "bk_01"  # Dune novel
    },
    {
        "id": "mov_15",
        "type": "movie",
        "title": "Oppenheimer",
        "year": 2023,
        "director_or_author": "Christopher Nolan",
        "cast": ["Cillian Murphy", "Emily Blunt", "Matt Damon", "Robert Downey Jr."],
        "genres": ["Biography", "Drama", "History"],
        "moods": ["reflective", "tense", "curious"],
        "cognitive_load": "deeply_philosophical",
        "tempo": "slow_burn",
        "companions": ["solo", "friends"],
        "eras": ["contemporary"],
        "tones": ["intellectual", "obsessive", "epic", "historical"],
        "rating": 8.9,
        "age_rating": "18+",
        "quality": "4K Ultra HD",
        "runtime_or_pages": "3h 00m",
        "synopsis": "The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb during World War II.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/4/4a/Oppenheimer_%28film%29.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
        "tags": ["manhattan_project", "science", "guilt", "politics", "academy_award"],
        "streaming_or_publisher": "Peacock / Prime Video",
        "cross_media_rec": "bk_06"  # Sapiens
    },

    # ----------------------------- BOOKS --------------------------------------
    {
        "id": "bk_01",
        "type": "book",
        "title": "Dune",
        "year": 1965,
        "director_or_author": "Frank Herbert",
        "cast": ["Hugo & Nebula Award Winner", "Epic Sci-Fi Canon"],
        "genres": ["Sci-Fi", "Adventure", "Fantasy"],
        "moods": ["reflective", "tense", "curious"],
        "cognitive_load": "deeply_philosophical",
        "tempo": "slow_burn",
        "companions": ["solo"],
        "eras": ["classic", "timeless"],
        "tones": ["epic", "intellectual", "political", "mystical"],
        "rating": 8.9,
        "age_rating": "13+",
        "quality": "Unabridged Audio & E-Book",
        "runtime_or_pages": "688 pages",
        "synopsis": "Set on the desert planet Arrakis, Dune tells the story of Paul Atreides as his noble family takes stewardship of the galaxy's only source of the valuable spice melange.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/b/be/Dune_by_Frank_Herbert_first_edition_cover.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/lzWHmYdfeFiMIY4JaMmtR7GEli3.jpg",
        "tags": ["ecology", "spice", "prophecy", "sandworms", "world_building"],
        "streaming_or_publisher": "Audible / Ace Books",
        "cross_media_rec": "mov_14"  # Dune movie
    },
    {
        "id": "bk_02",
        "type": "book",
        "title": "Project Hail Mary",
        "year": 2021,
        "director_or_author": "Andy Weir",
        "cast": ["Narrated by Ray Porter", "Goodreads Choice Award Winner"],
        "genres": ["Sci-Fi", "Adventure", "Humor"],
        "moods": ["curious", "joyful", "adventurous", "tense"],
        "cognitive_load": "balanced",
        "tempo": "fast_paced",
        "companions": ["solo"],
        "eras": ["contemporary"],
        "tones": ["optimistic", "scientific", "witty", "heartwarming"],
        "rating": 9.1,
        "age_rating": "13+",
        "quality": "Audible Original",
        "runtime_or_pages": "496 pages",
        "synopsis": "Ryland Grace is the sole survivor on a desperate last-chance mission to save Earth from a stellar catastrophe. With the help of an unexpected alien ally, science might just pull off the impossible.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/a/ad/Project_Hail_Mary%2C_First_Edition_Cover_%282021%29.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/xJHokMbljvjADYdit5fK5VQsXEG.jpg",
        "tags": ["space_survival", "first_contact", "optimism", "rocky", "problem_solving"],
        "streaming_or_publisher": "Audible / Ballantine Books",
        "cross_media_rec": "mov_01"  # Interstellar
    },
    {
        "id": "bk_03",
        "type": "book",
        "title": "Atomic Habits",
        "year": 2018,
        "director_or_author": "James Clear",
        "cast": ["#1 New York Times Bestseller", "Over 15M Copies Sold"],
        "genres": ["Self-Help", "Psychology", "Non-Fiction"],
        "moods": ["reflective", "curious", "exhausted"],
        "cognitive_load": "balanced",
        "tempo": "moderate",
        "companions": ["solo"],
        "eras": ["contemporary"],
        "tones": ["practical", "motivating", "clarifying", "actionable"],
        "rating": 8.8,
        "age_rating": "All Ages",
        "quality": "Audiobook & Hardcover",
        "runtime_or_pages": "320 pages",
        "synopsis": "An easy and proven way to build good habits and break bad ones using behavioral psychology, incremental systems, and identity-driven change.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/2/28/Atomic_Habits_book_cover.jpg",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/2/28/Atomic_Habits_book_cover.jpg",
        "tags": ["productivity", "habits", "psychology", "personal_growth"],
        "streaming_or_publisher": "Penguin Audio / Avery",
        "cross_media_rec": "mov_06"
    },
    {
        "id": "bk_04",
        "type": "book",
        "title": "Klara and the Sun",
        "year": 2021,
        "director_or_author": "Kazuo Ishiguro",
        "cast": ["Nobel Prize in Literature Author"],
        "genres": ["Sci-Fi", "Literary Fiction", "Drama"],
        "moods": ["reflective", "melancholic", "curious"],
        "cognitive_load": "deeply_philosophical",
        "tempo": "slow_burn",
        "companions": ["solo"],
        "eras": ["contemporary"],
        "tones": ["poetic", "heartbreaking", "subtle", "existential"],
        "rating": 8.2,
        "age_rating": "13+",
        "quality": "Unabridged Edition",
        "runtime_or_pages": "303 pages",
        "synopsis": "The story of Klara, an Artificial Friend with outstanding observational qualities, who watches the behavior of customers from the store window and hopes for a family.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/2/26/Klara_and_the_Sun_%28Kazuo_Ishiguro%29.png",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/2/26/Klara_and_the_Sun_%28Kazuo_Ishiguro%29.png",
        "tags": ["artificial_intelligence", "humanity", "love", "nobel_laureate"],
        "streaming_or_publisher": "Faber & Faber / Knopf",
        "cross_media_rec": "mov_08"  # Blade Runner 2049
    },
    {
        "id": "bk_05",
        "type": "book",
        "title": "The Midnight Library",
        "year": 2020,
        "director_or_author": "Matt Haig",
        "cast": ["Narrated by Carey Mulligan"],
        "genres": ["Fantasy", "Fiction", "Philosophical"],
        "moods": ["reflective", "melancholic", "joyful", "exhausted"],
        "cognitive_load": "balanced",
        "tempo": "moderate",
        "companions": ["solo"],
        "eras": ["contemporary"],
        "tones": ["healing", "hopeful", "empathetic", "comforting"],
        "rating": 8.3,
        "age_rating": "16+",
        "quality": "Audio & Print",
        "runtime_or_pages": "304 pages",
        "synopsis": "Between life and death there is a library where Nora Seed can experience all the lives she could have lived had she made different choices.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/8/87/The_Midnight_Library.jpg",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/8/87/The_Midnight_Library.jpg",
        "tags": ["mental_health", "alternate_realities", "second_chances", "comfort_read"],
        "streaming_or_publisher": "Viking / Canongate",
        "cross_media_rec": "mov_10"  # Everything Everywhere
    },
    {
        "id": "bk_06",
        "type": "book",
        "title": "Sapiens: A Brief History of Humankind",
        "year": 2014,
        "director_or_author": "Yuval Noah Harari",
        "cast": ["Global Bestseller in 65+ Languages"],
        "genres": ["History", "Anthropology", "Non-Fiction"],
        "moods": ["curious", "reflective"],
        "cognitive_load": "deeply_philosophical",
        "tempo": "moderate",
        "companions": ["solo"],
        "eras": ["contemporary", "timeless"],
        "tones": ["eye_opening", "panoramic", "intellectual", "challenging"],
        "rating": 9.0,
        "age_rating": "All Ages",
        "quality": "Special Illustrated Edition",
        "runtime_or_pages": "443 pages",
        "synopsis": "Explores how an insignificant ape became the ruler of planet Earth through cognitive, agricultural, and scientific revolutions.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Sapiens-_A_Brief_History_of_Humankind.png",
        "backdrop": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Sapiens-_A_Brief_History_of_Humankind.png",
        "tags": ["evolution", "anthropology", "civilization", "cognitive_revolution"],
        "streaming_or_publisher": "HarperCollins",
        "cross_media_rec": "mov_15"  # Oppenheimer
    },
    {
        "id": "bk_07",
        "type": "book",
        "title": "The Hitchhiker's Guide to the Galaxy",
        "year": 1979,
        "director_or_author": "Douglas Adams",
        "cast": ["Narrated by Stephen Fry"],
        "genres": ["Sci-Fi", "Comedy", "Adventure"],
        "moods": ["joyful", "curious", "exhausted"],
        "cognitive_load": "light_easy",
        "tempo": "fast_paced",
        "companions": ["solo"],
        "eras": ["classic", "timeless"],
        "tones": ["satirical", "absurdist", "hilarious", "whimsical"],
        "rating": 8.6,
        "age_rating": "All Ages",
        "quality": "BBC Full Cast Audio",
        "runtime_or_pages": "224 pages",
        "synopsis": "Seconds before Earth is demolished to make way for a galactic freeway, Arthur Dent is plucked into outer space by his friend Ford Prefect.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/b/bd/H2G2_UK_front_cover.jpg",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/b/bd/H2G2_UK_front_cover.jpg",
        "tags": ["towel", "dont_panic", "42", "space_comedy", "cult_classic"],
        "streaming_or_publisher": "Pan Books",
        "cross_media_rec": "mov_07"
    },
    {
        "id": "bk_08",
        "type": "book",
        "title": "The Silent Patient",
        "year": 2019,
        "director_or_author": "Alex Michaelides",
        "cast": ["#1 NYT Bestseller", "Brad Pitt Plan B Adaptation"],
        "genres": ["Mystery", "Thriller", "Psychological"],
        "moods": ["tense", "curious"],
        "cognitive_load": "mind_bending",
        "tempo": "fast_paced",
        "companions": ["solo"],
        "eras": ["contemporary"],
        "tones": ["dark_gritty", "twisting", "suspenseful", "obsessive"],
        "rating": 8.1,
        "age_rating": "16+",
        "quality": "Macmillan Audio",
        "runtime_or_pages": "336 pages",
        "synopsis": "Alicia Berenson shoots her husband five times and never speaks another word; a criminal psychotherapist is determined to uncover the truth.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/d/df/The_Silent_Patient_early_2019_UK_edition.png",
        "backdrop": "https://upload.wikimedia.org/wikipedia/en/d/df/The_Silent_Patient_early_2019_UK_edition.png",
        "tags": ["twist_ending", "psychotherapy", "murder_mystery", "page_turner"],
        "streaming_or_publisher": "Celadon Books",
        "cross_media_rec": "mov_05"  # Parasite
    }
]

# ==============================================================================
# 2. PRODUCTION RULES (Declarative AI Reasoning Rules)
# ==============================================================================

PRODUCTION_RULES: List[Dict[str, Any]] = [
    {
        "rule_id": "RULE-COG-01",
        "name": "Existential & Speculative Mindset Induction",
        "level": 1,
        "priority": 90,
        "conditions": {
            "mood_in": ["reflective", "curious"],
            "cognitive_load_in": ["deeply_philosophical", "mind_bending"]
        },
        "consequences": {
            "deduce_facts": {
                "inferred_need": "intellectual_transcendence",
                "recommended_focus": "philosophical_speculation"
            },
            "boost_criteria": {
                "tags": ["existential", "identity", "multiverse", "physics", "artificial_intelligence"],
                "cognitive_load": ["deeply_philosophical", "mind_bending"],
                "boost_weight": 35
            }
        },
        "explanation": "Detected a reflective & curious state with high cognitive appetite; prioritizing speculative masterworks that expand worldview and consciousness."
    },
    {
        "rule_id": "RULE-COG-02",
        "name": "Emotional Comfort & Stress Relief Induction",
        "level": 1,
        "priority": 85,
        "conditions": {
            "mood_in": ["exhausted", "melancholic"],
            "cognitive_load_in": ["light_easy", "balanced"]
        },
        "consequences": {
            "deduce_facts": {
                "inferred_need": "cognitive_restoration",
                "recommended_focus": "wholesome_comfort"
            },
            "boost_criteria": {
                "tones": ["wholesome", "comforting", "healing", "uplifting"],
                "tags": ["feel_good", "kindness", "healing", "pure_joy"],
                "boost_weight": 30
            }
        },
        "explanation": "Detected fatigue or low emotional energy; boosting warm, restorative, and uplifting narratives to promote cognitive rejuvenation."
    },
    {
        "rule_id": "RULE-COG-03",
        "name": "High-Stakes Thrill & Adrenaline Synergy",
        "level": 1,
        "priority": 88,
        "conditions": {
            "mood_in": ["tense", "adventurous"],
            "tempo_in": ["fast_paced", "intense"]
        },
        "consequences": {
            "deduce_facts": {
                "inferred_need": "adrenaline_stimulation",
                "recommended_focus": "high_tension_narrative"
            },
            "boost_criteria": {
                "genres": ["Thriller", "Action", "Mystery"],
                "tones": ["adrenaline", "high_stakes", "dark_gritty"],
                "boost_weight": 30
            }
        },
        "explanation": "Adventurous energy paired with brisk pacing; boosting gripping thrillers with intense tension curves."
    },
    {
        "rule_id": "RULE-SOC-01",
        "name": "Social Gathering & Group Crowd-Pleaser Rule",
        "level": 2,
        "priority": 75,
        "conditions": {
            "companion_in": ["friends", "family", "party"]
        },
        "consequences": {
            "deduce_facts": {
                "accessibility": "high_crowd_pleaser"
            },
            "boost_criteria": {
                "companions": ["friends", "family", "party"],
                "genres": ["Comedy", "Animation", "Adventure", "Mystery"],
                "tones": ["uplifting", "vibrant", "whimsical", "witty"],
                "boost_weight": 25
            }
        },
        "explanation": "Group viewing detected; boosting universally engaging, witty, and crowd-pleasing entertainment."
    },
    {
        "rule_id": "RULE-SOC-02",
        "name": "Intimate Solo Immersion Rule",
        "level": 2,
        "priority": 70,
        "conditions": {
            "companion_in": ["solo"]
        },
        "consequences": {
            "deduce_facts": {
                "accessibility": "deep_personal_immersion"
            },
            "boost_criteria": {
                "tempo": ["slow_burn", "moderate"],
                "tones": ["subtle", "poetic", "cyberpunk", "neo_noir", "existential"],
                "boost_weight": 20
            }
        },
        "explanation": "Solo viewing unlocks appetite for patient world-building, poetic cinematography, and intimate atmosphere."
    },
    {
        "rule_id": "RULE-GEN-01",
        "name": "Speculative Sci-Fi & Futuristic Rule",
        "level": 3,
        "priority": 65,
        "conditions": {
            "genre_preference_contains": "Sci-Fi"
        },
        "consequences": {
            "boost_criteria": {
                "genres": ["Sci-Fi"],
                "tags": ["space", "cyberpunk", "world_building", "artificial_intelligence"],
                "boost_weight": 25
            }
        },
        "explanation": "Reinforcing futuristic and sci-fi world-building narratives."
    },
    {
        "rule_id": "RULE-GEN-02",
        "name": "Mystery & Puzzle Twist Rule",
        "level": 3,
        "priority": 65,
        "conditions": {
            "genre_preference_contains": "Mystery"
        },
        "consequences": {
            "boost_criteria": {
                "genres": ["Mystery", "Thriller"],
                "tags": ["twist", "whodunit", "puzzle", "psychological"],
                "boost_weight": 25
            }
        },
        "explanation": "Boosting whodunits, investigative puzzles, and psychological twists."
    },
    {
        "rule_id": "RULE-ERA-01",
        "name": "Timeless Masterpiece Rule",
        "level": 4,
        "priority": 60,
        "conditions": {
            "preferred_era_in": ["classic", "timeless"]
        },
        "consequences": {
            "boost_criteria": {
                "eras": ["classic", "timeless"],
                "min_rating": 8.4,
                "boost_weight": 20
            }
        },
        "explanation": "Favoring universally acclaimed cinematic milestones."
    },
    {
        "rule_id": "RULE-ERA-02",
        "name": "Contemporary Cutting-Edge Visuals Rule",
        "level": 4,
        "priority": 60,
        "conditions": {
            "preferred_era_in": ["contemporary", "modern"]
        },
        "consequences": {
            "boost_criteria": {
                "eras": ["contemporary", "modern"],
                "boost_weight": 18
            }
        },
        "explanation": "Favoring modern high-definition productions with contemporary storytelling rhythm."
    }
]

# Quick presets for immediate streaming vibe selection
PRESETS = [
    {
        "id": "preset_mind_bender",
        "name": "Late Night Mind-Bender",
        "tagline": "Cerebral, existential, and jaw-dropping sci-fi",
        "icon": "🧠",
        "facts": {
            "domain": "both",
            "mood": "reflective",
            "companion": "solo",
            "cognitive_load": "mind_bending",
            "tempo": "slow_burn",
            "preferred_era": "contemporary",
            "genre_preferences": ["Sci-Fi", "Thriller"]
        }
    },
    {
        "id": "preset_cozy_comfort",
        "name": "Cozy & Chill",
        "tagline": "Warm blankets, cocoa, and heartwarming storytelling",
        "icon": "☕",
        "facts": {
            "domain": "both",
            "mood": "exhausted",
            "companion": "solo",
            "cognitive_load": "light_easy",
            "tempo": "moderate",
            "preferred_era": "contemporary",
            "genre_preferences": ["Animation", "Comedy", "Fantasy"]
        }
    },
    {
        "id": "preset_movie_night",
        "name": "Party & Friends Night",
        "tagline": "Fast, funny, high-octane crowd-pleasers",
        "icon": "🍿",
        "facts": {
            "domain": "movie",
            "mood": "joyful",
            "companion": "friends",
            "cognitive_load": "balanced",
            "tempo": "fast_paced",
            "preferred_era": "contemporary",
            "genre_preferences": ["Action", "Comedy", "Mystery"]
        }
    },
    {
        "id": "preset_adrenaline",
        "name": "Adrenaline Rush",
        "tagline": "High-octane intensity and edge-of-your-seat suspense",
        "icon": "⚡",
        "facts": {
            "domain": "both",
            "mood": "tense",
            "companion": "solo",
            "cognitive_load": "mind_bending",
            "tempo": "intense",
            "preferred_era": "contemporary",
            "genre_preferences": ["Thriller", "Action"]
        }
    },
    {
        "id": "preset_deep_thinker",
        "name": "Deep Philosophical",
        "tagline": "Masterpieces that alter your perception of reality",
        "icon": "🌌",
        "facts": {
            "domain": "both",
            "mood": "curious",
            "companion": "solo",
            "cognitive_load": "deeply_philosophical",
            "tempo": "moderate",
            "preferred_era": "timeless",
            "genre_preferences": ["Sci-Fi", "History", "Drama"]
        }
    }
]
