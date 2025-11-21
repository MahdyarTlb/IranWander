from iranwander import db, create_app 
from iranwander.models import City, Place 


CITIES_TO_ADD = [
    {
        "name": "Tehran", 
        "image_file": "tehran.jpg", 
        "description": "The capital of Iran, its largest city, and the political and economic center of the country."
    },
    {
        "name": "Isfahan", 
        "image_file": "isfahan.jpg",
        "description": "Half of the World (Nisf-e Jahan), famous for its stunning Islamic architecture, historic bridges, and Naqsh-e Jahan Square."
    },
    {
        "name": "Shiraz", 
        "image_file": "shiraz.jpg",
        "description": "The city of poetry, literature, beautiful Persian gardens (like Eram), and the tombs of Hafez and Saadi."
    },
    {
        "name": "Mashhad", 
        "image_file": "mashhad.jpg",
        "description": "Iran's religious and pilgrimage center, home to the shrine of Imam Reza."
    },
    {
        "name": "Karaj", 
        "image_file": "karaj.jpg",
        "description": "The fourth most populous city in Iran and the capital of Alborz province."
    }
]

PLACES_TO_ADD = [
    {
        "name": "Milad Tower",
        "city_name": "Tehran",
        "header_image": "miladheader.jpg",
        "location": "Tehran, Sheikh Fazlollah Nouri Expressway",
        "hours": "9:00 AM - 9:00 PM",
        "price": "300,000 Rials",
        "overview": "It serves as a symbol of modern Tehran and features a range of attractions, including an open-air observation deck with a 360-degree view of the city, the Sky Dome, a revolving restaurant, museums, exhibition spaces, and entertainment facilities." +
        "Today, Milad Tower is considered one of Tehran’s most iconic tourist destinations, attracting visitors for its panoramic cityscape views, architectural design, and cultural events.",
        "gallery_images": "milad1.jpg,milad2.jpg,milad3.jpg,milad4.jpg" 
    },
    {
        "name": "Golestan Palace",
        "city_name": "Tehran",
        "header_image": "golestanheader.jpg",
        "location": "Tehran, Panzdah-e Khordad Street",
        "hours": "9:00 AM - 5:00 PM",
        "price": "500,000 Rials",
        "overview": "        architecture. The complex blends traditional Persian craft with European influences, creating a unique royal residence filled with richly decorated halls, mirrored chambers, royal gardens, and museums." + 
        "As a UNESCO World Heritage Site, Golestan Palace showcases centuries of Persian art, royal ceremonies, and cultural evolution. Today it stands as one of Tehran’s most celebrated landmarks, admired for its intricate tilework, dazzling mirror mosaics, and beautifully landscaped courtyards.",
        "gallery_images": "golestan1.jpg,golestan2.jpg,golestan3.jpg,golestan4.jpg" 
    },
    {
        "name": "Naqsh-e Jahan Square",
        "city_name": "Isfahan",
        "header_image": "naqshejahanheader.jpg",
        "location": "Isfahan, center of the city",
        "hours": "Open 24 hours (Bazaars have specific hours)",
        "price": "Free access to the square",
        "overview": "Naqsh-e Jahan Square, also known as Imam Square, is a UNESCO World Heritage Site and one of the largest historical squares in the world. Built during the Safavid era," + 
        "it is surrounded by remarkable landmarks such as the Shah Mosque, Sheikh Lotfollah Mosque, Ali Qapu Palace, and the Grand Bazaar. Today, it stands as the cultural and architectural heart of Isfahan, attracting visitors with its stunning Persian design and vibrant atmosphere.",
        "gallery_images": "naqshe1.jpg,naqshe3.jpg,naqshe2.jpg,naqshe4.jpg" 
    },
    {
        "name": "Si-o-se-pol Bridge",
        "city_name": "Isfahan",
        "header_image": "siosepolheader.jpg",
        "location": "Isfahan, Allahverdi Khan Bridge",
        "hours": "Open 24 hours",
        "price": "Free",
        "overview": "Si-o-se-pol, also known as the Bridge of 33 Arches, is one of the most iconic structures of the Safavid era. Built in the early 17th century, it spans the Zayandeh River and is admired for its elegant arches," + 
        "symmetrical Persian architecture, and historical significance. Today, it stands as one of Isfahan’s most famous landmarks and a popular gathering place for locals and tourists.",
        "gallery_images": "siosepol1.jpg,siosepol2.jpg,siosepol3.jpg,siosepol4.jpg" 
    },
    {
        "name": "Hafez Mausoleum",
        "city_name": "Shiraz",
        "header_image": "hafezheader.jpg",
        "location": "Shiraz, Hafezieh",
        "hours": "8:30 AM - 8:30 PM",
        "price": "200,000 Rials",
        "overview": "The Tomb of Hafez, dedicated to the celebrated Persian poet, is one of Shiraz’s most beloved cultural landmarks. Surrounded by beautiful gardens," + 
        "the site features a striking pavilion and marble tombstone adorned with verses from Hafez’s poetry. Today, it is a place of reflection, literature, and tradition, drawing visitors who come to honor the poet’s legacy and enjoy the peaceful atmosphere.",
        "gallery_images": "hafez1.jpg,hafez2.jpg,hafez3.jpg,hafez4.jpg" 
    },
    {
        "name": "Persepolis",
        "city_name": "Shiraz",
        "header_image": "persepolisheader.jpg",
        "location": "70 km northeast of Shiraz",
        "hours": "8:00 AM - 5:30 PM",
        "price": "400,000 Rials",
        "overview": "Persepolis was the ceremonial capital of the Achaemenid Empire, built around 518 BC."+
        "It features monumental staircases, grand halls, and stone carvings depicting"+ 
        "the diverse peoples of the empire. Today, it stands as one of Iran’s most iconic"+
        "archaeological sites and a UNESCO World Heritage site.",
        "gallery_images": "persepolis1.jpg,persepolis2.jpg,persepolis3.jpg,persepolis4.jpg" 
    },
    {
        "name": "Chamran Park",
        "city_name": "Karaj",
        "header_image": "chamranheader.jpg",
        "location": "Karaj, Shahriyar Blvd",
        "hours": "Open 24 hours",
        "price": "Free",
        "overview": "Chamran Park is one of Karaj’s largest and most popular urban parks, known for its long riverside walkway, extensive green spaces, and recreational facilities." +  
        "It’s a major hangout spot for families and young people, offering cycling paths, playgrounds, picnic areas, and seasonal events. Its central location and natural scenery make it one of the city’s key outdoor attractions.",
        "gallery_images": "chamran1.jpg,chamran2.jpg,chamran3.jpg,chamran4.jpg" 
    },
    {
        "name": "Little Iran Park",
        "city_name": "Karaj",
        "header_image": "littleiranheader.jpg",
        "location": "Karaj, Mehrshahr",
        "hours": "9:00 AM - 6:00 PM",
        "price": "Free",
        "overview": "Little Iran Park (Iran Koochak Park) spans about 7 hectares and is recognized as Iran’s first “cultural garden” by the national UNESCO commission." + 
        "The park is designed to showcase the cultural and architectural diversity of Iran, featuring scaled-down reproductions (about half-size) of traditional dwellings and landmarks from different Iranian provinces." + 
        "Visitors can explore replicas of tribal tents (like Bakhtiari and Turkmen), historic houses, windmills, bazaars, and other structures representing regions such as Yazd, Qazvin, Khorasan, and others." + 
        "The park is a symbolic space celebrating the ethnic and architectural richness of Iran.",
        "gallery_images": "littleiran1.jpg,littleiran2.jpg,littleiran3.jpg,littleiran4.jpg" 
    },
    {
        "name": "Imam Reza Shrine",
        "city_name": "Mashhad",
        "header_image": "emamheader.jpg",
        "location": "Mashhad center",
        "hours": "Open 24 hours",
        "price": "Free",
        "overview": "The largest mosque in the world and the burial place of the eighth Imam of Shia Islam.",
        "gallery_images": "emam1.jpg,emam2.jpg,emam3.jpg,emam4.jpg" 
    },
    {
        "name": "Ferdosi Mausoleum",
        "city_name": "Mashhad",
        "header_image": "ferdosiheader.jpg",
        "location": "20 km north of Mashhad",
        "hours": "9:00 AM - 5:00 PM",
        "price": "200,000 Rials",
        "overview": "The Imam Reza Holy Shrine is one of the most significant religious and cultural complexes in the Islamic world. It features the mausoleum of Imam Reza, vast courtyards," +  
        "stunning Islamic architecture, museums, libraries, and religious centers. Millions of visitors and pilgrims travel to Mashhad each year to experience its spiritual atmosphere and admire its intricate tilework, domes, and historical structures",
        "gallery_images": "ferdosi1.jpg,ferdosi2.jpg,ferdosi3.jpg,ferdosi4.jpg" 
    }
]


def seed_db():
    """Function to refresh both City and Place data."""
    
    app = create_app()
    with app.app_context():
        print("Starting Data Re-Seeding process...")
        
        db.session.query(City).delete()
        db.session.query(Place).delete() 
        print("🗑️ Existing data deleted (Cities and Places).")
        
        city_objects = {}
        for city_data in CITIES_TO_ADD:
            city = City(name=city_data["name"], image=city_data["image_file"], description=city_data["description"])
            db.session.add(city)
            city_objects[city.name] = city 
            print(f"City {city.name} added.")
        
        for place_data in PLACES_TO_ADD:
            city_obj = city_objects.get(place_data["city_name"])
            
            place = Place(
                name=place_data["name"],
                image=place_data["header_image"], 
                description=place_data["overview"], 
                location=place_data["location"],   
                hours=place_data["hours"],         
                price=place_data["price"],        
                gallery_images=place_data["gallery_images"],
                city_id=city_obj.id if city_obj else None
            )

            
            db.session.add(place)
            print(f"Place {place.name} added.")
        
        db.session.commit()
        print("Data successfully refreshed in both City and Place tables.")

if __name__ == '__main__':
    seed_db()