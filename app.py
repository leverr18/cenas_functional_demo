from flask import Flask, render_template, jsonify

app = Flask(__name__)

locations = [
    {
        "name": "Cenas Kitchen - Tomball",
        "address": "27727 Tomball Parkway, Tomball, TX 77375",
        "lat": 30.078674,
        "lng": -95.629883,
        "order_url": "https://order.toasttab.com/online/aguirres-tex-mex-2-tomball-27727-tomball-parkway"
    },
    {
        "name": "Cenas Kitchen - Houston",
        "address": "15650 Farm To Market rd. 529, Houston TX 77095",
        "lat": 29.879688,
        "lng": -95.644264,
        "order_url": "https://order.toasttab.com/online/aguirres-tex-mex-1-copperfield-6166-hwy-6-north-unit-22"
    },
]

menu_items = [
    {
        "category": "Appetizers",
        "items": [
            {"name": "Taquitos", "description": "Shredded chicken in corn tortillas, topped with lettuce and tomatoes — served with guacamole, sour cream & a cup of queso.", "price": "11.99", "image": "taquito.webp"},
            {"name": "Queso Dip", "price": "7.59", "image": "queso.webp"},
            {"name": "Guacamole Dip", "price": "8.99", "image": "guacamole.webp"},
            {
                "name": "Empanadas",
                "description": "Jumbo empanadas made from scratch",
                "image": "empanadas.webp",
                "options": [
                    {"type": "One", "price": "7.99"},
                    {"type": "Two", "price": "10.49"},
                    {"type": "Three", "price": "12.99"}
                ]
            },
            {
                "name": "Stuffed Jalapeños",
                "description": "Stuffed jalapeños with pork and cheese.",
                "image": "stuffed_jalapenos.webp",
                "options": [
                    {"type": "Four", "price": "7.49"},
                    {"type": "Six", "price": "10.49"},
                ]
            },

            {"name": "Sampler", "description": "Beef nachos, chicken quesadillas, etc.", "price": "14.69", "image": "sampler.webp"},
            {
                "name": "Quesadillas",
                "description": "Choice of filling in warm flour tortillas.",
                "image": "quesadillas.webp",
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
                "image": "nachos.webp",
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
            {"name": "Cenaladas (4)", "description": "Cheese, beef, chicken enchiladas + tamale.", "price": "13.99", "image": "cenalada.webp"},
            {"name": "Veggie Enchiladas (3)", "description": "Grilled veggie enchiladas with sauce.", "price": "12.79", "image": "veggie_enchilada.webp"},
            {"name": "Spinach Enchiladas (3)", "description": "Spinach mix enchiladas.", "price": "12.59", "image": "spinach_enchilada.webp"},
            {"name": "Tamales Dinner (3)", "description": "Pork tamales with chili con carne.", "price": "13.89", "image": "tamale_dinner.webp"},
            {
                "name": "Cheese or Ground Beef Enchiladas (3)",
                "description": "Chili con carne, sour cream & grated cheese.",
                "image": "cheese_beef_enchilada.webp",
                "options": [
                    {"type": "Cheese", "price": 11.79},
                    {"type": "Beef", "price": 12.89}
                ]
            },
            {"name": "Chicken Enchiladas (3)", "description": "Shredded chicken enchiladas with poblano.", "price": "13.89", "image": "chicken_enchilada.webp"},
            {"name": "Pollo Feliz (3)", "description": "Each enchilada has a different sauce.", "price": "14.99", "image": "pollo_felix.webp"},
            {
                "name": "Fajita Enchiladas (3)",
                "description": "Beef or chicken fajita, pick sauce.",
                "image": "fajita_enchilada.webp",
                "options": [
                    {"type": "Chicken Fajita", "price": 14.79},
                    {"type": "Beef Fajita", "price": 16.39}
                ]
            },
            {"name": "Seafood Enchiladas (3)", "description": "Shrimp & crawfish enchiladas.", "price": "15.89", "image": "seafood_enchilada.webp"},
            {"name": "Pork Enchiladas (3)", "description": "Pork & poblano cream.", "price": "12.99", "image": "pork_enchilada.webp"}
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
            {"name": "Mango & Shrimp Salad (8)", "description": "Shrimp with mango, veggies, queso.", "price": "17.49", "image": "shrimp_salad.webp"},
            {
                "name": "Fajita Salad",
                "description": "Lettuce, tomato, avocado, cheese, cucumber.",
                "image": "fajita_salad.webp",
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
                "image": "taco_salad.webp",
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
                "image": "soup_salad.webp",
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
                "image": "tortilla_soup.webp",
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
                "image": "fajitas.webp",
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
                "image": "plato_mazatlan.webp",
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
                "image": "plato_cancun.webp",
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
                "image": "fajita_del_mar.webp",
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
                "image": "el_jefe.webp",
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
            {"name": "Pollo Del Mar", "description": "Shrimp & crawfish over grilled chicken.", "price": "16.79", "image": "pollo_del_mar.webp"},
            {"name": "Chipotle Chicken", "description": "Chicken with mushrooms, spinach, sausage, chipotle cream.", "price": "16.79", "image": "chipotle_chicken.webp"},
            {"name": "Pollo Poblano", "description": "Chicken with vegetables & creamy poblano.", "price": "16.49", "image": "food3.webp"},
            {"name": "Pollo Con Mango", "description": "Chicken with mango pico and queso blanco.", "price": "15.99", "image": "pollo_con_mango.webp"},
            {
                "name": "Fajita Bowl",
                "description": "Fajita meat, beans, rice, queso & cheese.",
                "image": "fajita_bowl.webp",
                "options": [
                    {"type": "Chicken", "price": "13.19"},
                    {"type": "Beef", "price": "15.59"},
                    {"type": "Combo", "price": "14.59"}
                ]
            },
            {"name": "Steak Tampiquena", "description": "Skirt steak with enchilada & salad mix.", "price": "18.99", "image": "steak_tampiquena.webp"},
            {"name": "Chile Rellano", "description": "Stuffed poblano pepper with chicken, cheese, and sauces.", "price": "14.29", "image": "chile_rellano.webp"}
        ]
    },
    {
        "category": "Seafood",
        "items": [
            {"name": "Fish El Rey", "description": "Tilapia with shrimp, crawfish, queso fresco, mango pico.", "price": "16.99", "image": "fish_el_ray.webp"},
            {"name": "Seafood Bowl", "description": "Shrimp & crawfish bowl with rice & cheese.", "price": "13.19", "image": "seafood_bowl.webp"},
            {
                "name": "Chipotle Portobello",
                "description": "Stuffed mushroom with shrimp or spinach.",
                "image": "chipotle_portobello.webp",
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
            {"name": "Chicken Flautas (4)", "description": "Crispy flautas with guac, sour cream, queso blanco.", "price": "13.29", "image": "chicken_flautas.webp"},
            {
                "name": "Tacos Al Carbon (2)",
                "description": "Flour tortillas with fajitas, guac, queso, pico.",
                "image": "tacos_al_carbon.webp",
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
                "image": "texmex_tacos.webp",
                "options": [
                    {"type": "Chicken Fajita", "price": "14.49"},
                    {"type": "Beef Fajita", "price": "16.49"},
                    {"type": "Combo", "price": "15.49"},
                    {"type": "Grilled Veggies", "price": "13.89"}
                ]
            },
            {"name": "Pork Tacos (5)", "description": "Shredded pork tacos with habanero onions.", "price": "12.98", "image": "pork_taco.webp"},
            {
                "name": "Street Tacos (5)",
                "description": "Fajita meat tacos with taco sauce & grilled jalapeño.",
                "image": "street_taco.webp",
                "options": [
                    {"type": "Chicken Fajita", "price": "13.69"},
                    {"type": "Beef Fajita", "price": "15.89"},
                    {"type": "Combo Fajita", "price": "14.89"},
                    {"type": "Add a Taco", "price": "3.50"}
                ]
            },
            {"name": "Fish Tacos (2)", "description": "Tilapia, chipotle, mango, cabbage, queso.", "price": "16.99", "image": "fish_taco.webp"},
            {"name": "Shrimp Tacos (2)", "description": "Shrimp, chipotle, mango, cabbage, queso.", "price": "16.99", "image": "shrimp_taco.webp"},
            {
                "name": "Tostada Dinner (2)",
                "description": "Tostadas with beans, lettuce, cheese, tomato.",
                "image": "tostada_dinner.webp",
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
                "image": "el_texmex.webp",
                "price": "12.99"
            },
            {
                "name": "Plato Guzman",
                "description": "Ground beef enchilada, chicken enchilada, crispy beef taco, crispy chicken taco.",
                "image": "plato_guzman.webp",
                "price": "13.89"
            },
            {
                "name": "Plato Salinas",
                "description": "Chicken enchilada with tomatillo sauce, chicken flauta, chicken fajita nachos, pico, sour cream, guac, queso.",
                "image": "plato_salinas.webp",
                "price": "14.89"
            },
            {
                "name": "Plato Vaquero",
                "description": "Beef fajita taco al carbon, cheese enchilada, ground beef enchilada with gravy, pork tamale, queso, sour cream, guacamole.",
                "image": "plato_vaquero.webp",
                "price": "14.89"
            },
            {
                "name": "Plato Suarez",
                "description": "Cheese enchilada, bean & cheese tostada, crispy ground beef taco, sour cream, guacamole.",
                "image": "plato_saurez.webp",
                "price": "13.39"
            },
            {
                "name": "Combo Special",
                "description": "Beef taco, bean tostada, queso chip, served with pico, guacamole, sour cream (no rice & beans).",
                "image": "combo_special.webp",
                "price": "11.89"
            },
            {
                "name": "Laredo Combo",
                "description": "Chicken quesadillas and beef fajita flour tortilla with queso blanco, pico, sour cream, guacamole.",
                "image": "laredo_combo.webp",
                "price": "14.49"
            },
            {
                "name": "Pollo Capmero",
                "description": "Chicken enchilada with poblano cream, flauta, chicken fajita tortilla, queso, sour cream, guac, pico.",
                "image": "pollo_capmero.webp",
                "price": "13.99"
            },
            {
                "name": "Veggie Los Cabos",
                "description": "Stuffed bell pepper and cheese enchilada with poblano cream, avocado, and pico de gallo.",
                "image": "veggie_los_cabos.webp",
                "price": "13.89"
            },
            {
                "name": "Veggie Suarez",
                "description": "Cheese enchilada with poblano cream, black bean & cheese tostada, veggie taco with sour cream & guacamole.",
                "image": "veggie_saurez.webp",
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
                "image": "burrito_con_queso.webp",
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
                "image": "tiago_burrito.webp",
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
                "image": "chimi_changa.webp",
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
                "image": "mexican_wrap.webp",
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
                "image": "seafood_burrito.webp",
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
                "image": "tejano_burger.webp",
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
                "image": "avocado_burger.webp",
                "options": [
                    {"type": "Half Pound", "price": 15.99},
                    {"type": "One Pound", "price": 20.99}
                ]
            }
        ]
    },
    {
        "category": "Desserts",
        "items": [
            {
                "name": "Sopapillas",
                "description": "",
                "image": "",
            },
            {
                "name": "Churros",
                "description": "",
                "image": ""
            },
            {
                "name": "Tres Leches",
                "description": "",
                "image": ""
            }
        ]
    }
]

drink_items = [
    {
        "category": "Margarita Cantina",
        "items": [
            {"name": "House Margarita SM", "description": "Non-Alcholic also Available", "price": "$6", "image": "house_marg_SM.webp"},
            {"name": "House Margarita LG", "description": "Non-Alcoholic also Available", "price": "$12", "image": "house_marg.webp"},
            {"name": "CenaRita", "description": "House rita with a top shelf kick Don Julio Blanco & Grand Marnier.", "price": "$12"},
            {"name": "Gold Rush Rita SM", "description": "Jose Cuervo Gold, orange liquer.", "price": "$6", "image": "gold_rush_SM.webp"},
            {"name": "Gold Rush Rita LG", "description": "Jose Cuervo Gold, orange liquer.", "price": "$11", "image": "gold_rush_LG.webp"},
            {"name": "Mango Tango SM", "description": "Mango puree, Chamoy, chili salt, served frozen.", "price": "$6", "image": "mango_tango_SM.webp"},
            {"name": "Mango Tango LG", "description": "Mango puree, Chamoy, chili salt, served frozen.", "price": "$10", "image": "mango_tangoLG.webp"},
            {"name": "Beer Rita", "description": "Margarita and an ice-cold beer.", "price": "$10", "image": "beer_rita_.webp"},
            {"name": "La Granada", "description": "Jalapeno infused tequila, fresh lime, pomegranate, chili salt.", "price": "$10", "image": "la_grenada.webp"},
            {"name": "Skinny Summer", "description": "Altos Plata, agave, fresh lime", "price": "$9", "image": "skinny_summer.webp"},
            {"name": "Mezcalita", "description": "Mezcal, Grand Marnier, pineapple, jalapeno", "price": "$12", "image": "mezcalita.webp"},
            {"name": "Guava TikiRita", "description": "Milagro Silver, guava, lime, allspice.", "price": "$12"}
        ]
    },
    {
        "category": "Hand Shaken Cocktails",
        "items": [
            {"name": "Watermelon Ranchwater", "description": "1800 Silver, fresh watermelon, lime, Topo Chico. Non-Alcoholic also Available.", "price": "$11", "image": "watermelon_ranchwater.webp"},
            {"name": "Uno Mas Mule", "description": "House infused jalapeno tequila, fresh lime, ginger beer", "price": "$10"},
            {"name": "Reposado Old Fashioned", "description": "Milagro Reposado, agave, chocolate bitters, Angostura.", "price": "$12"},
            {"name": "Tequila Berry Fizz", "description": "Altos Plata, mixed berry puree, fresh lime, ginger beer.", "price": "$11", "image": "tequila_berry_fizz_pretty.webp"},
            {"name": "Fresh Mint Paloma", "description": "Patron Silver, fresh lime, mint, grapefruit, Topo Chico.", "price": "$11", "image": "mint_drink.webp"},
            {"name": "Cantaritos Michelada", "description": "Homemade michelada mix and an ice-cold beer of your choosing.", "price": "$5", "image": "cantaritos_michelada.webp"},
            {"name": "Sangria", "description": "Red sangria with fresh fruit or swirled into a frozen margarite", "price": "$8", "image": "sangria.webp"},
            {"name": "Mango Mama", "description": "Tito's Vodka, lime, fresh mango, ginger beer.", "price": "$9", "image": "mango_mama.webp"},
            {"name": "Cenas Paradise Daquiris", "description": "Silver Rum, fresh lime, and your choice of flavor.", "price": "$9", "image": "cenas_paradise_daquiris.webp"},
            {"name": "Romancito", "description": "Fresh rosemary, gin, lemon, elderflower liquer.", "price": "$9"},
            {"name": "New Fashioned", "description": "Old forester bourbon, rye whisky, black walnut and peach bitters.", "price": "$11"},
            {"name": "Non Alcoholic Daquiri", "price": "$7"},
            {"name": "Non Alcoholic Mojito", "price": "$5"},
            {"name": "Non Alcoholic Passionfruit Kiss", "price": "$5"},
            {"name": "Non Alcoholic Bloody Mary", "price": "$5"},
            {"name": "Non Alcoholic Michelada W/ Topo", "price": "$5"},
            {"name": "Non Alcoholic Watermelon Ranchwater", "price": "$5"},
            {"name": "Non Alcoholic Margarita", "price": "$7"}
        ]
    },
    {
        "category": "Dessert Drinks",
        "items": [
            {"name": "Carajillo", "description": "Espresso, Licor 43", "price": "$10", "image": "carajillo.webp"},
            {"name": "Classic Espresso Martini", "description": "Kettle One, espresso, cane sugar.", "price": "$10", "image": "espresso_martini_pretty.webp"},
            {"name": "Tequila Alejandro", "description": "Milagro Silver, chocolate liqueur, ice cream, toasted marshmallow.", "price": "$11", "image": "alejandro_tequila.webp"}
        ]
    },
    {
        "category": "Ice Cold Beer",
        "items": [
            {"name": "Miller Lite", "price": "$4.50"},
            {"name": "Budweiser", "price": "$4.50"},
            {"name": "Michelob Ultra", "price": "$4.50"},
            {"name": "Bud Light", "price": "$4.50"},
            {"name": "Coors Light", "price": "$4.50"},
            {"name": "Shinner Block", "price": "$4.50"},
            {"name": "Negra Modelo", "price": "$4.50"},
            {"name": "Model Especial", "price": "$4.50"},
            {"name": "Corona Extra", "price": "$4.50"},
            {"name": "Corona Light", "price": "$4.50"},
            {"name": "Dos XX Larger", "price": "$4.50"},
            {"name": "Tacate", "price": "$4.50"},
            {"name": "Pacifico", "price": "$4.go"}
        ]
    },
    {
        "category": "Flavors",
        "items": [
            {"name": "Mango"},
            {"name": "Strawberry"},
            {"name": "Pina Colada"},
            {"name": "Peach"},
            {"name": "Mixed Berry"},
            {"name": "Watermelon"},
            {"name": "Banana"}
        ]
    },
    {
        "category": "Floaters",
        "items": [
            {"name": "Grand Marneir Floater", "price": "$2"},
            {"name": "Cointreau Floater", "price": "$2"},
            {"name": "Patron Citronage Floater", "price": "$2"},
            {"name": "Don Julio Floater", "price": "$3"},
            {"name": "Patron Silver Floater", "price": "$3"},
            {"name": "1800 Silver Floater", "price": "$3"},
            {"name": "Cuervo Gold Floater", "price": "$3"},
            {"name": "Jalapeno Tequila Floater", "price": "$3"},
            {"name": "Don Julio Reposado Floater", "price": "$3"},
            {"name": "Patron Reposado", "price": "$3"},
            {"name": "Patron Anejo", "price": "$4"},
            {"name": "1800 Reposado", "price": "$3"},
            {"name": "1800 Anejo", "price": "$4"}
        ]
    }
]

weekly_specials = {
    "Monday Madness": [
        "Plato Catrina – $10.99",
        "Two $2 margaritas or bottled beers with entrée (regular pricing after 2)"
    ],
    "Taco Tuesday": [
        "Plato Pancho Villa – $10.99",
        "Pork tacos – $11.50",
        "Street tacos – $12 (chicken), $14 (beef), $13 (combo)",
        "Fish tacos – $15 or $7.50 for one",
        "Shrimp tacos – $15 or $7.50 for one",
        "Tacos al carbon – $13.19 (chicken), $16.39 (beef), $14.39 (combo)"
    ],
    "Enchilada Wednesday": [
        "Plato Sombrero – $10.59",
        "Tamale Dinner – $12.39",
        "Cheese Enchiladas – $9.89",
        "Ground Beef Enchiladas – $11.47",
        "Chicken Enchiladas – $12.89",
        "Beef Fajita Enchiladas – $11.47",
        "Chicken Fajita Enchiladas – $13.89",
        "Veggie Enchiladas – $12.39",
        "Spinach Enchiladas – $12.39",
        "Pork Enchiladas – $11.99"
    ],
    "Fajita Fiesta Thursday": [
        "Seafood Combo – $14.69",
        "Chicken Fajita – $14.49 (one), $28.99 (two)",
        "Beef Fajita – $19.49 (one), $38.99 (two)",
        "Combo Fajita – $17.59 (one), $35.19 (two)",
        "Add 4 Pack: Brochette Shrimp – $9.99",
        "Grilled Shrimp – $8.89",
        "Grilled Sausage – $7.29",
        "Ribs – $9.39"
    ],
    "Fiesta Fridays": [
        "Pollo Del Mar – $16.79",
        "Happy Hour All Day!"
    ],
    "Seafood Saturdays": [
        "Fish El Rey – $15.89",
        "Fish Tacos – $15.99, $7.99 for one",
        "Shrimp Tacos – $15.99, $7.99 for one",
        "Shrimp Portobello – $14.49",
        "Seafood Enchiladas – $15.39",
        "Pollo Del Mar – $15.29",
        "Seafood Bowl – $12.89",
        "Chicken Bowl – $14.99",
        "Beef Bowl – $17.99",
        "Combo Bowl – $16.99",
        "Add sour cream, guac, lettuce – $2.00"
    ],
    "Family Sunday Funday": [
        "Plato Mazatlan – Chicken: $19.81 (one), $39.62 (two)",
        "Beef: $23.92 (one), $47.84 (two)",
        "Combo: $21.98 (one), $43.96 (two)"
    ],
    "All-Day Drink Specials": [
        "Mon–Thu: House Rita – $5, Gold Rush – $6, Bottle Beer – $4",
        "Fri–Sun: House Rita – $6, Gold Rush – $7, Bottle Beer – $4.50"
    ]
}

vegetarian_items = [
    {"name": "Veggie Fajitas", "description": "Sauteed vegetables on a bed of onions, Cenas rice, black beans, and sour cream. Also available for two."},
    {"name": "Veggie Bowl", "description": "A large bowl filled with sauteed vegetables, black beans, Cenas rice, Queso Blanco, & grated cheese. Served with flour tortillas. Make it loaded by adding lettuce, sour cream, and guacamole."},
    {"name": "Veggie Quesadilla", "description": "Sauteed vegetables, served with guacamole, sour cream, and jalapenos."},
    {"name": "Spinach Quesadillas", "description": "Freshly sauteed spinach, guacamole, sour cream, and jalapenos."},
    {"name": "Spinach Portobello", "description": "Sauteed spinach in poblano cream set atop a thick and meaty portobello mushroom. Served with sliced avocado."},
    {"name": "Veggie Enchiladas", "description": "Freshly sauteed vegetables rolled in corn tortillas & smothered in your selection of sauces, sour cream & grated cheese."},
    {"name": "Spinach Enchiladas", "description": "House made spinach mix rolled in corn tortillas & smothered in your selection of sauce, sour cream, & grated cheeses."},
    {"name": "Veggie Tex Mex Tacos (3)", "description": "Soft flour tortillas filled with an assortment of delicious veggies - topped with fresh lettuce, grated cheeses, and roma tomatoes."},
    {"name": "Veggie Los Cabos", "description": ""},
    {"name": "Veggie Saurez", "description": "Cheese enchilada with poblano cream, black bean and cheese tostada, and veggie taco. Served with sour cream, & guacamole."},
    {"name": "Veggie Wrap", "description": "Flour tortilla stuffed with sauteed vegetables, lettuce, Cenas rice, black beans, guacamole, sour cream, and pico de gallo. Served with queso."},
    {"name": "Veggie Bur Con Queso", "description": "Large flour tortilla stuffed with sauteed vegetables, smothered with Queso Blanco, & grated cheese."}
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

@app.route('/weekly_specials_data')
def weekly_specials_data():
    return jsonify(weekly_specials)

@app.route('/menu')
def menu():
    return render_template("menu.html", menu_items=menu_items, weekly_specials=weekly_specials)

@app.route('/menu_data')
def menu_data():
    return jsonify(menu_items)

@app.route('/veggie_menu_data')
def vegetarian_menu_data():
    return jsonify(vegetarian_items)

@app.route('/vegetarian_menu')
def vegetarian_menu():
    return render_template("vegetarian_menu.html", vegetarian_items=vegetarian_items)

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/drinks')
def drinks():
    return render_template("drinkmenu.html", drink_items=drink_items, weekly_specials=weekly_specials)

@app.route('/drink_data')
def drink_data():
    return jsonify(drink_items)

@app.route('/orderlocation')
def orderlocation():
    return render_template("chooselocation.html", locations=locations)

@app.route('/login')
def login():
    return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True)
