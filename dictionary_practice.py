makeup_products = {"Products": [
                    {"Primer": {
                               "Shades": 15, 
                               "Styles": 5,
                               "Location": "Face"
                            }
                    },
                    {"Lipstick": {
                               "Shades": 48, 
                               "Styles": 3,
                                "Location": "Lips"
                              }
                    },
                    {"Lip liner": {
                               "Shades": 32, 
                               "Styles": 4,
                                "Location": "Lips"
                               }
                    },
                    {"Blush": {
                            "Shades": 13, 
                            "Styles": 2,
                            "Location": "Face"
                          }
                    },
                    {"Eye Liner": {
                               "Shades": 14, 
                               "Styles": 7,
                               "Location": "Eye"
                               }
                    },
                    {"Travel Makeup Kit": {
                               "Shades": "N/A",
                               "Styles": 3,
                               "Location": "Face, Lips, Eye"
                               }
                    },
                    {"Chapstick": {
                               "Shades": 3,
                               "Styles": 7,
                               "Location": "Lips"
                               }
                    }
                 ] }


total_count_lip_shades = 0
for item in makeup_products["Products"]:
    for product in item:
        
        if("Lips" in item[product]["Location"] and item[product]["Shades"] != "N/A"):
            
            shade_count = item[product]["Shades"]
            # print(shade_count)
            
            total_count_lip_shades += shade_count