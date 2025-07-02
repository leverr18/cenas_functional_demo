from flask import Flask, render_template, jsonify

app = Flask(__name__)

locations = [
    {
        "name": "Cenas Kitchen - Tomball",
        "address": "27727 Tomball Parkway, Tomball, TX 77375",
        "lat": 30.078674,
        "lng": -95.629883
    },
    {
        "name": "Cenas Kitchen - Houston",
        "address": "15650 Farm To Market rd. 529, Houston TX 77095",
        "lat": 29.879688,
        "lng": -95.644264
    },
]

menu_items = [
    {
        "category": "Appetizers",
        "items": [
            {"name": "Taquitos", "description": "Shredded chicken in corn tortillas, topped with lettuce and tomatoes — served with guacamole, sour cream & a cup of queso.", "price": "11.99", "image": "taquito.jpg"},
            {"name": "Queso Dip", "price": "7.59", "image": "queso.jpg"},
            {"name": "Guacamole Dip", "price": "8.99", "image": "guacamole.jpg"},
            {
                "name": "Empanadas",
                "description": "Jumbo empanadas made from scratch",
                "image": "empanadas.jpg",
                "options": [
                    {"type": "One", "price": "7.99"},
                    {"type": "Two", "price": "10.49"},
                    {"type": "Three", "price": "12.99"}
                ]
            },
            {
                "name": "Stuffed Jalapeños",
                "description": "Stuffed jalapeños with pork and cheese.",
                "image": "stuffed_jalapenos.jpg",
                "options": [
                    {"type": "Four", "price": "7.49"},
                    {"type": "Six", "price": "10.49"},
                ]
            },

            {"name": "Sampler", "description": "Beef nachos, chicken quesadillas, etc.", "price": "14.69", "image": "sampler.jpg"},
            {
                "name": "Quesadillas",
                "description": "Choice of filling in warm flour tortillas.",
                "image": "quesadillas.jpg",
                "options": [
                    {"type": "Cheese", "price": 11.89},
                    {"type": "Chicken Fajita", "price": 12.99},
                    {"type": "Beef Fajita", "price": 15.59},
                    {"type": "Combo Fajita", "price": 14.99},
                    {"type": "Shrimp", "price": 12.89},
                    {"type": "BBQ Pork", "price": 12.19},
                    {"type": "Spinach", "price": 13.39},
                    {"type": "Sautéed Veggies", "price": 13.99}
                ]
            },
            {
                "name": "Classic Nachos",
                "description": "Tortilla chips topped with queso, meat, jalapeños, etc.",
                "image": "nachos.jpg",
                "options": [
                    {"type": "Bean & Cheese", "price": 11.99},
                    {"type": "Ground Beef", "price": 12.89},
                    {"type": "Shredded Chicken", "price": 13.89},
                    {"type": "Chicken Breast", "price": 13.99},
                    {"type": "Beef Fajita", "price": 15.39},
                    {"type": "Sautéed Vegetables", "price": 13.99}
                ]
            }
        ]
    },
    {
        "category": "Enchiladas",
        "items": [
            {"name": "Cenaladas (4)", "description": "Cheese, beef, chicken enchiladas + tamale.", "price": "13.99", "image": "cenalada.jpg"},
            {"name": "Veggie Enchiladas (3)", "description": "Grilled veggie enchiladas with sauce.", "price": "12.79", "image": "veggie_enchilada.jpg"},
            {"name": "Spinach Enchiladas (3)", "description": "Spinach mix enchiladas.", "price": "12.59", "image": "spinach_enchilada.jpg"},
            {"name": "Tamales Dinner (3)", "description": "Pork tamales with chili con carne.", "price": "13.89", "image": "tamale_dinner.jpg"},
            {
                "name": "Cheese or Ground Beef Enchiladas (3)",
                "description": "Chili con carne, sour cream & grated cheese.",
                "image": "cheese_beef_enchilada.jpg",
                "options": [
                    {"type": "Cheese", "price": 11.79},
                    {"type": "Beef", "price": 12.89}
                ]
            },
            {"name": "Chicken Enchiladas (3)", "description": "Shredded chicken enchiladas with poblano.", "price": "13.89", "image": "chicken_enchilada.jpg"},
            {"name": "Pollo Feliz (3)", "description": "Each enchilada has a different sauce.", "price": "14.99", "image": "pollo_felix.jpg"},
            {
                "name": "Fajita Enchiladas (3)",
                "description": "Beef or chicken fajita, pick sauce.",
                "image": "fajita_enchilada.jpg",
                "options": [
                    {"type": "Chicken Fajita", "price": 14.79},
                    {"type": "Beef Fajita", "price": 16.39}
                ]
            },
            {"name": "Seafood Enchiladas (3)", "description": "Shrimp & crawfish enchiladas.", "price": "15.89", "image": "seafood_enchilada.jpg"},
            {"name": "Pork Enchiladas (3)", "description": "Pork & poblano cream.", "price": "12.99", "image": "pork_enchilada.jpg"}
        ]
    },
    {
        "category": "House Made Sauces",
        "items": [
            {"name": "Chili Con Carne", "description": "Chili gravy with beef & spices."},
            {"name": "Tomatillo Sauce", "description": "Tomatillos, avocado, spices."},
            {"name": "Poblano Sauce", "description": "Roasted poblano with sour cream."},
            {"name": "Street Taco Sauce (spicy)", "description": "Spicy sauce with bold flavor."},
            {"name": "Chipotle Cream", "description": "Chipotle + tomatillo + jalapeño."},
            {"name": "Ranchero Sauce", "description": "Tomatoes, onion, celery blend."}
        ]
    },
    {
        "category": "Soups & Salads",
        "items": [
            {"name": "Mango & Shrimp Salad (8)", "description": "Shrimp with mango, veggies, queso.", "price": "17.49", "image": "shrimp_salad"},
            {
                "name": "Fajita Salad",
                "description": "Lettuce, tomato, avocado, cheese, cucumber.",
                "image": "fajita_salad.jpg",
                "options": [
                    {"type": "Chicken Breast", "price": 13.39},
                    {"type": "Beef Fajita", "price": 16.99},
                    {"type": "Combo", "price": 14.99},
                    {"type": "Grilled Shrimp", "price": 15.89},
                    {"type": "Grilled Veggies", "price": 13.89}
                ]
            },
            {
                "name": "Taco Salad",
                "description": "Lettuce, chicken/beef, cheese, guac, sour cream.",
                "image": "taco_salad.jpg",
                "price": "13.49",
                "options": [
                    {"type": "Chicken Breast", "price": 13.99},
                    {"type": "Beef Fajita", "price": 16.89},
                    {"type": "Combo Fajita", "price": 14.89},
                    {"type": "Grilled Veggies", "price": 13.89}
                ]
            },
            {
                "name": "Soup & Salad",
                "description": "Mini salad & tortilla soup combo.",
                "image": "soup_salad.jpg",
                "options": [
                    {"type": "Chicken Breast", "price": 16.99},
                    {"type": "Beef Fajita", "price": 19.39},
                    {"type": "Combo", "price": 17.99},
                    {"type": "Grilled Veggies", "price": 17.29}
                ]
            },
            {
                "name": "Tortilla Soup",
                "description": "Shredded chicken, vegetables, rice, tortilla strips.",
                "image": "tortilla_soup.jpg",
                "options": [
                    {"type": "Cup", "price": 7.89},
                    {"type": "Bowl", "price": 9.49}
                ]
            }
        ]
    },


    {
        "category": "Cenas Signature Grill",
        "items": [
            {
                "name": "Fajitas",
                "description": "Served with guacamole, sour cream, pico de gallo, flour tortillas, Cenas rice & choice of beans.",
                "image": "fajitas.jpg",
                "options": [
                    {
                        "type": "Chicken",
                        "variants": [
                            {"type": "One", "price": 16.49},
                            {"type": "Two", "price": 32.99}
                        ]
                    },
                    {
                        "type": "Beef",
                        "variants": [
                            {"type": "One", "price": 22.49},
                            {"type": "Two", "price": 44.99}
                        ]
                    },
                    {
                        "type": "Combo",
                        "variants": [
                            {"type": "One", "price": 19.59},
                            {"type": "Two", "price": 39.19}
                        ]
                    },
                    {
                        "type": "Veggie Fajitas",
                        "variants": [
                            {"type": "One", "price": 15.81},
                            {"type": "Two", "price": 31.62}
                        ]
                    }
                ]
            },
            {
                "name": "Plato Mazatlan",
                "description": "Fajitas, bacon-wrapped shrimp, ribs, and sausage.",
                "image": "plato_mazatlan.jpg",
                "options": [
                    {
                        "type": "Chicken",
                        "variants": [
                            {"type": "One", "price": 21.19},
                            {"type": "Two", "price": 42.29}
                        ]
                    },
                    {
                        "type": "Beef",
                        "variants": [
                            {"type": "One", "price": 26.29},
                            {"type": "Two", "price": 52.59}
                        ]
                    },
                    {
                        "type": "Combo",
                        "variants": [
                            {"type": "One", "price": 23.59},
                            {"type": "Two", "price": 47.19}
                        ]
                    }
                ]
            },
            {
                "name": "Plato Cancun",
                "description": "Fajitas and jumbo bacon-wrapped shrimp.",
                "image": "plato_cancun.jpg",
                "options": [
                    {
                        "type": "Chicken",
                        "variants": [
                            {"type": "One", "price": 20.99},
                            {"type": "Two", "price": 41.99}
                        ]
                    },
                    {
                        "type": "Beef",
                        "variants": [
                            {"type": "One", "price": 25.29},
                            {"type": "Two", "price": 50.39}
                        ]
                    },
                    {
                        "type": "Combo",
                        "variants": [
                            {"type": "One", "price": 23.39},
                            {"type": "Two", "price": 46.69}
                        ]
                    }
                ]
            },
            {
                "name": "Fajitas Del Mar",
                "description": "Fajitas with seafood sauce and jumbo shrimp.",
                "image": "fajita_del_mar.jpg",
                "options": [
                    {
                        "type": "Chicken",
                        "variant": [
                            {"type": "One", "price": 18.99},
                            {"type": "Two", "price": 37.99}
                        ]
                    },
                    {
                        "type": "Beef",
                        "variants": [
                            {"type": "One", "price": 22.59},
                            {"type": "Two", "price": 45.19}
                        ]
                    },
                    {
                        "type": "Combo",
                        "variants": [
                            {"type": "One", "price": 20.99},
                            {"type": "Two", "price": 41.99}
                        ]
                    }
                ]
            },
            {"name": "Shrimp Brochette (8)", "description": "Bacon-wrapped shrimp with peppers and cheese.", "price": "24.99", "image": "shrimp_brochette.jpg"},
            {"name": "Shrimp Fajitas (8)", "description": "Grilled jumbo shrimp with sautéed veggies.", "price": "21.99", "image": "shrimp_fajita.jpg"},
            {
                "name": "El Jefe's Ribs",
                "description": "BBQ baby back ribs, coleslaw, and fries.",
                "image": "el_jefe.jpg",
                "options": [
                    {"type": "Half Rack", "price": "19.99"},
                    {"type": "Full Rack", "price": "32.99"}
                ]
            }
        ]
    },
    {
        "category": "Fan Favorites",
        "items": [
            {"name": "Pollo Del Mar", "description": "Shrimp & crawfish over grilled chicken.", "price": "16.79", "image": "pollo_del_mar.jpg"},
            {"name": "Chipotle Chicken", "description": "Chicken with mushrooms, spinach, sausage, chipotle cream.", "price": "16.79", "image": "chipotle_chicken.jpg"},
            {"name": "Pollo Poblano", "description": "Chicken with vegetables & creamy poblano.", "price": "16.49", "image": "pollo_poblano.jpg"},
            {"name": "Pollo Con Mango", "description": "Chicken with mango pico and queso blanco.", "price": "15.99", "image": "pollo_con_mango.jpg"},
            {
                "name": "Fajita Bowl",
                "description": "Fajita meat, beans, rice, queso & cheese.",
                "image": "fajita_bowl.jpg",
                "options": [
                    {"type": "Chicken", "price": "13.19"},
                    {"type": "Beef", "price": "15.59"},
                    {"type": "Combo", "price": "14.59"}
                ]
            },
            {"name": "Steak Tampiquena", "description": "Skirt steak with enchilada & salad mix.", "price": "18.99", "image": "steak_tampiquena.jpg"},
            {"name": "Chile Rellano", "description": "Stuffed poblano pepper with chicken, cheese, and sauces.", "price": "14.29", "image": "chile_rellano.jpg"}
        ]
    },
    {
        "category": "Seafood",
        "items": [
            {"name": "Fish El Rey", "description": "Tilapia with shrimp, crawfish, queso fresco, mango pico.", "price": "16.99", "image": "fish_el_ray.jpg"},
            {"name": "Seafood Bowl", "description": "Shrimp & crawfish bowl with rice & cheese.", "price": "13.19", "image": "seafood_bowl.jpg"},
            {
                "name": "Chipotle Portobello",
                "description": "Stuffed mushroom with shrimp or spinach.",
                "image": "chipotle_portobello.jpg",
                "options": [
                    {"type": "Spinach", "price": "13.93"},
                    {"type": "Shrimp", "price": "15.29"},
                    {"type": "Shrimp & Spinach", "price": "16.89"}
                ]
            }
        ]
    },
    {
        "category": "Tacos, Tostadas & More",
        "items": [
            {"name": "Chicken Flautas (4)", "description": "Crispy flautas with guac, sour cream, queso blanco.", "price": "13.29", "image": "chicken_flautas.jpg"},
            {
                "name": "Tacos Al Carbon (2)",
                "description": "Flour tortillas with fajitas, guac, queso, pico.",
                "image": "tacos_al_carbon.jpg",
                "options": [
                    {"type": "Chicken Fajita", "price": "14.69"},
                    {"type": "Beef Fajita", "price": "16.99"},
                    {"type": "Combo", "price": "15.99"},
                    {"type": "Grilled Veggies", "price": "13.89"}
                ]
            },
            {
                "name": "Tex-Mex Tacos (3) (Crispy or Soft)",
                "description": "Tacos with lettuce, tomato, cheese.",
                "image": "texmex_tacos.jpg",
                "options": [
                    {"type": "Chicken Fajita", "price": "14.49"},
                    {"type": "Beef Fajita", "price": "16.49"},
                    {"type": "Combo", "price": "15.49"},
                    {"type": "Grilled Veggies", "price": "13.89"}
                ]
            },
            {"name": "Pork Tacos (5)", "description": "Shredded pork tacos with habanero onions.", "price": "12.98", "image": "pork_taco.jpg"},
            {
                "name": "Street Tacos (5)",
                "description": "Fajita meat tacos with taco sauce & grilled jalapeño.",
                "image": "street_taco.jpg",
                "options": [
                    {"type": "Chicken Fajita", "price": "13.69"},
                    {"type": "Beef Fajita", "price": "15.89"},
                    {"type": "Combo Fajita", "price": "14.89"},
                    {"type": "Add a Taco", "price": "3.50"}
                ]
            },
            {"name": "Fish Tacos (2)", "description": "Tilapia, chipotle, mango, cabbage, queso.", "price": "16.99", "image": "fish_taco.jpg"},
            {"name": "Shrimp Tacos (2)", "description": "Shrimp, chipotle, mango, cabbage, queso.", "price": "16.99", "image": "shrimp_taco.jpg"},
            {
                "name": "Tostada Dinner (2)",
                "description": "Tostadas with beans, lettuce, cheese, tomato.",
                "image": "tostada_dinner.jpg",
                "price": "11.89",
                "options": [
                    {"type": "Ground Beef or Shredded Chicken", "price": "12.89"},
                    {"type": "Chicken Fajita", "price": "13.99"},
                    {"type": "Beef Fajita", "price": "14.99"},
                    {"type": "Combo Fajita", "price": "14.49"},
                    {"type": "Grilled Veggies", "price": "13.89"}
                ]
            }
        ]
    },

    {
        "category": "Combination",
        "items": [
            {
                "name": "El Tex-Mex",
                "description": "Crispy beef taco, queso chip, bean tostada, two cheese enchiladas with savory gravy.",
                "image": "el_texmex.jpg",
                "price": "12.99"
            },
            {
                "name": "Plato Guzman",
                "description": "Ground beef enchilada, chicken enchilada, crispy beef taco, crispy chicken taco.",
                "image": "plato_guzman.jpg",
                "price": "13.89"
            },
            {
                "name": "Plato Salinas",
                "description": "Chicken enchilada with tomatillo sauce, chicken flauta, chicken fajita nachos, pico, sour cream, guac, queso.",
                "image": "plato_salinas.jpg",
                "price": "14.89"
            },
            {
                "name": "Plato Vaquero",
                "description": "Beef fajita taco al carbon, cheese enchilada, ground beef enchilada with gravy, pork tamale, queso, sour cream, guacamole.",
                "image": "plato_vaquero.jpg",
                "price": "14.89"
            },
            {
                "name": "Plato Suarez",
                "description": "Cheese enchilada, bean & cheese tostada, crispy ground beef taco, sour cream, guacamole.",
                "image": "plato_saurez.jpg",
                "price": "13.39"
            },
            {
                "name": "Combo Special",
                "description": "Beef taco, bean tostada, queso chip, served with pico, guacamole, sour cream (no rice & beans).",
                "image": "combo_special.jpg",
                "price": "11.89"
            },
            {
                "name": "Laredo Combo",
                "description": "Chicken quesadillas and beef fajita flour tortilla with queso blanco, pico, sour cream, guacamole.",
                "image": "laredo_combo.jpg",
                "price": "14.49"
            },
            {
                "name": "Pollo Capmero",
                "description": "Chicken enchilada with poblano cream, flauta, chicken fajita tortilla, queso, sour cream, guac, pico.",
                "image": "pollo_capmero.jpg",
                "price": "13.99"
            },
            {
                "name": "Veggie Los Cabos",
                "description": "Stuffed bell pepper and cheese enchilada with poblano cream, avocado, and pico de gallo.",
                "image": "veggie_los_cabos.jpg",
                "price": "13.89"
            },
            {
                "name": "Veggie Suarez",
                "description": "Cheese enchilada with poblano cream, black bean & cheese tostada, veggie taco with sour cream & guacamole.",
                "image": "veggie_saurez.jpg",
                "price": "13.49"
            }
        ]
    },
    {
        "category": "Burritos",
        "items": [
            {
                "name": "Burrito Con Queso",
                "description": "Tortilla with beef, chicken, or pork, queso blanco, grated cheese.",
                "image": "burrito_con_queso.jpg",
                "price": "13.99",
                "options": [
                    {"type": "Chicken Fajita", "price": "add 3"},
                    {"type": "Beef Fajita", "price": "add 4"},
                    {"type": "Grilled Veggies", "price": "13.89"},
                    {"type": "Sour Cream, Guacamole & Lettuce Inside", "price": "1.49"}
                ]
            },
            {
                "name": "Tiago Burrito",
                "description": "Stuffed with meat, beans, queso blanco, chili gravy, cheese.",
                "image": "tiago_burrito.jpg",
                "price": "13.89",
                "options": [
                    {"type": "Chicken Fajita", "price": "add 3"},
                    {"type": "Beef Fajita", "price": "add 4"},
                    {"type": "Grilled Veggies", "price": "13.89"},
                    {"type": "Sour Cream, Guacamole & Lettuce Inside", "price": "1.49"}
                ]
            },
            {
                "name": "Chimi & Changa",
                "description": "Fried burrito with cheese, lettuce, tomato, queso fresco, sour cream, guac, queso blanco.",
                "image": "chimi_changa.jpg",
                "price": "14.99",
                "options": [
                    {"type": "Chicken Fajita", "price": "add 3"},
                    {"type": "Beef Fajita", "price": "add 4"},
                    {"type": "Grilled Veggies", "price": "13.89"}
                ]
            },
            {
                "name": "Mexican Wrap",
                "description": "Tortilla with meat, lettuce, rice, beans, guac, sour cream, pico, served with queso & taco sauce.",
                "image": "mexican_wrap.jpg",
                "price": "14.99",
                "options": [
                    {"type": "Chicken Fajita", "price": "add 3"},
                    {"type": "Beef Fajita", "price": "add 4"},
                    {"type": "Grilled Veggies", "price": "13.89"}
                ]
            },
            {
                "name": "Seafood Burrito",
                "description": "Stuffed with shrimp & crawfish, topped with white wine seafood sauce.",
                "image": "seafood_burrito.jpg",
                "price": "14.89",
                "options": [
                    {"type": "Sour Cream, Guacamole & Lettuce Inside", "price": "1.49"}
                ]
            }
        ]
    },
    {
        "category": "Burgers",
        "items": [
            {
                "name": "Tejano Burger",
                "description": "Sirloin burger on sourdough bun with fries & chipotle mayo.",
                "image": "tejano_burger.jpg",
                "options": [
                    {
                        "type": "Regular - Lettuce, grilled onions",
                        "variants": [
                            {"type": "Half Pound", "price": 13.99},
                            {"type": "One Pound", "price": 18.99}
                        ]
                    },
                    {
                        "type": "Cheeseburger - Monterey cheese, lettuce, grilled onions",
                        "variants": [
                            {"type": "Half Pound", "price": 14.99},
                            {"type": "One Pound", "price": 19.49}
                        ]
                    },
                    {
                        "type": "Bacon Cheeseburger - Bacon, Monterey cheese, lettuce, tomatoes, grilled onions",
                        "variants": [
                            {"type": "Half Pound", "price": 15.99},
                            {"type": "One Pound", "price": 19.99}
                        ]
                    }
                ]
            },
            {
                "name": "Avocado Burger",
                "description": "Avocado, Monterey cheese, lettuce, tomatoes, grilled onions.",
                "image": "avocado_burger.jpg",
                "options": [
                    {"type": "Half Pound", "price": 15.99},
                    {"type": "One Pound", "price": 20.99}
                ]
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('home.html')

@app.route("/about-us")
def about_us():
    return render_template("about.html", locations=locations)

@app.route('/locations')
def get_locations():
    return jsonify(locations)

@app.route('/career')
def career():
    return render_template("career.html")

@app.route('/catering')
def catering():
    return render_template("catering.html")

@app.route('/community')
def community():
    return render_template("community.html")

@app.route('/donations')
def donations():
    return render_template("communitydonations.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/menu')
def menu():
    return render_template("menu.html", menu_items=menu_items)

@app.route('/menu_data')
def menu_data():
    return jsonify(menu_items)

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/drinks')
def drinks():
    return render_template("drinkmenu.html")

@app.route('/orderlocation')
def orderlocation():
    return render_template("chooselocation.html")



if __name__ == '__main__':
    app.run(debug=True)
