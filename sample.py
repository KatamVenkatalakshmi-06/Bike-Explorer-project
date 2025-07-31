
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

bikes = {
    "budget_friendly": {
        "gear": [
            {"name": "Hero Xtreme 160R", "price": "₹1,11,611", "launch": "2020", "special": "Lightweight, good city performance", "mileage": "55 kmpl", "image": "https://imgd.aeplcdn.com/1056x594/n/cw/ec/127127/xtreme-right-side-view-2.jpeg?isig=0&q=80&wm=3", "website": "https://www.heromotocorp.com/en-in/motorcycles/performance/xtreme-160r.html", "colors": ["Pearl Silver White", "Sports Red", "Vibrant Blue", "Matte Black"]},
            {"name": "Bajaj Pulsar 150", "price": "₹1,13,734", "launch": "2019", "special": "Popular, reliable, value for money", "mileage": "50 kmpl", "image": "https://imgd.aeplcdn.com/1280x720/n/cw/ec/185667/pulsar-150-right-side-view-9.jpeg?isig=0", "website": "https://www.bajajauto.com/bikes/pulsar/pulsar-150", "colors": ["Sapphire Blue", "Pearl White", "Sparkle Black", "Volcanic Red"]},
            {"name": "TVS Apache RTR 160", "price": "₹98,264", "launch": "2021", "special": "Sporty design, good handling", "mileage": "48 kmpl", "image": "https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/tvs-apache-160-rm-drum-black-edition1732629216165.jpg?q=80", "website": "https://www.tvsmotor.com/tvs-apache/premium/apache-rtr-160-4v", "colors": ["Gloss Black", "Pearl White", "Matte Blue", "T Grey"]},
            {"name": "Honda Unicorn", "price": "₹1,55,000", "launch": "2018", "special": "Smooth engine, good mileage", "mileage": "60 kmpl", "image": "https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/--disc-20251735194316753.jpg?q=80", "website": "https://www.honda2wheelersindia.com/motorcycle/unicorn", "colors": ["Imperial Red Metallic", "Pearl Igneous Black", "Matte Axis Grey Metallic"]},
            {"name": "Yamaha FZ-S", "price": "₹1,59,387", "launch": "2022", "special": "Street style, fuel injection", "mileage": "50 kmpl", "image": "https://shop.yamaha-motor-india.com/cdn/shop/files/Green_b90fac0e-e6c9-4733-a708-f377c417c7ca.webp?v=1715159733", "website": "https://www.bikewale.com/yamaha-bikes/fz-s/", "colors": ["Matte Red", "Matte Black", "Dark Matte Blue", "Matte Grey"]}
        ],
        "non_gear": [
            {"name": "Honda Activa 6G", "price": "₹1,04,028", "launch": "2020", "special": "Most popular scooter, smooth engine", "mileage": "50 kmpl", "image": "https://imgd.aeplcdn.com/1280x720/n/cw/ec/44686/activa-6g-right-side-view-3.png?isig=0", "website": "https://www.bikewale.com/honda-bikes/activa-6g/", "colors": ["Decent Blue", "Pearl Siren Blue", "Black", "Pearl Precious White", "Matte Axis Grey", "Rebel Red Metallic"]},
            {"name": "TVS Jupiter", "price": "₹77,291", "launch": "2019", "special": "Comfortable ride, good features", "mileage": "50 kmpl","image":"https://www.tvsmotor.com/tvs-jupiter/-/media/Feature/BrandPriceCity/JupiterBikeImg.webp","website": "https://www.tvsmotor.com/tvs-jupiter/jupiter-disc-smartxonnect", "colors": ["Titanium Grey", "Pristine White", "Midnight Black", "Walnut Brown", "Metallic Red", "Indiblue", "Royal Wine", "Starlight Blue"]},
            {"name": "Suzuki Access 125", "price": "₹85,057", "launch": "2021", "special": "Powerful 125cc engine, lightweight", "mileage": "52 kmpl", "image": "https://imgd.aeplcdn.com/1200x900/n/cw/ec/188491/access-125-2025-right-side-view-11.jpeg?isig=0", "website": "https://www.suzukimotorcycle.co.in/product-details/all-new-access-125-bluetooth-enabled", "colors": ["Pearl Suzuki Deep Blue", "Metallic Matte Platinum Silver", "Metallic Dark Greenish Blue", "Pearl Mirage White", "Metallic Matte Black", "Metallic Sonic Silver", "Metallic Matte Bordeaux Red"]},
            {"name": "Hero Pleasure+", "price": "₹75,263", "launch": "2020", "special": "Lightweight, easy to handle", "mileage": "55 kmpl", "image": "https://media.zigcdn.com/media/model/2023/Jul/hero-pleasure-plus-right-side-view_360x240.jpg", "website": "https://www.heromotocorp.com/en-in/scooters/pleasure-plus-xtec.html", "colors": ["Jazzy Yellow", "Polestar Blue", "Sporty Red", "Pearl Silver White", "Midnight Black", "Matte Vernier Grey", "Matte Black"]},
            {"name": "Yamaha Ray ZR 125", "price": "₹93,065", "launch": "2022", "special": "Sporty scooter, good pickup", "mileage": "52 kmpl", "image": "https://imgd.aeplcdn.com/664x374/n/bw/models/colors/yamaha-select-model-matte-reddrum-1679658645174.png?q=80", "website": "https://www.yamaha-motor-india.com/yamaha-ray-zr125fihybrid.html", "colors": ["Matt Red", "Cyan Blue", "Metallic Black", "Racing Blue", "Dark Matte Blue", "Sparkle Green"]}
        ]
    },
    "naked_bikes": [
        {"name": "KTM Duke 200", "price": "₹2,06,312", "launch": "2020", "special": "Aggressive styling, performance", "mileage": "35 kmpl","image": "https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/ktm-duke-200-standard1732631072395.jpg?q=80", "website":"https://www.ktmindia.com/ktm-bikes/naked-bike/ktm-200-duke", "colors": ["Electronic Orange", "Dark Silver Metallic"]},
        {"name": "Yamaha MT-15", "price": "₹2,27,000", "launch": "2019", "special": "Lightweight, VVA engine", "mileage": "45 kmpl", "image": "https://imgd.aeplcdn.com/664x374/n/bw/models/colors/yamaha-select-model-metallic-black-2023-1680847548270.png?q=80", "website": "https://shop.yamaha-motor-india.com/products/buy-mt-15-ver2?srsltid=AfmBOoojePP7lZCBQIknLS7N8i-n77dEa5GPPtUug4vWKo-cU8U4sVj8", "colors": ["Metallic Black", "Ice Fluo-Vermillion", "Racing Blue", "Cyan Storm"]},
        {"name": "Bajaj Pulsar NS200", "price": "₹1,81,000", "launch": "2018", "special": "Triple spark engine, muscular looks", "mileage": "38 kmpl", "image": "https://imgd.aeplcdn.com/664x374/n/bw/models/colors/bajaj-select-model-pewter-grey-1709101653302.png?q=80", "website": "https://www.bajajauto.com/bikes/pulsar/pulsar-ns200", "colors": ["Pewter Grey", "Burnt Red", "Metallic Pearl White", "Satin Blue"]},
        {"name": "Honda Hornet 2.0", "price": "₹1,58,000", "launch": "2020", "special": "Refined engine, good handling", "mileage": "42 kmpl", "image": "https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/--standard-obd-2b1740150415645.jpg?q=80", "website":"https://www.honda2wheelersindia.com/motorcycle/hornet-2-0", "colors": ["Pearl Igneous Black", "Matte Axis Grey Metallic", "Matte Marvel Blue Metallic", "Matte Sangria Red Metallic"]},
        {"name": "Suzuki Gixxer", "price": "₹1,35,000", "launch": "2021", "special": "Sporty looks, good handling", "mileage": "45 kmpl", "image": "https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/suzuki-gixxer-ride-connect-obd-2b1740545220923.jpg?q=80", "website": "https://www.suzukimotorcycle.co.in/product-details/gixxer-sf", "colors": ["Metallic Triton Blue", "Glass Sparkle Black", "Metallic Sonic Silver"]},
        {"name": "TVS Apache RTR 200 4V", "price": "₹2,96,000", "launch": "2022", "special": "Race tuned, slipper clutch", "mileage": "40 kmpl","image": "https://imgd.aeplcdn.com/664x374/n/bw/models/colors/undefined-matte-blue-1604475089223.jpg?q=80", "website": "https://www.tvsmotor.com/tvs-apache/premium/apache-rtr-200-4v", "colors": ["Gloss Black", "Matte Blue", "Pearl White", "Matte Red"]}
    ],
    "cruiser_bikes": [
        {"name": "Suzuki Intruder 150", "price": "₹1,28,000", "launch": "2020", "special": "Modern cruiser, comfortable seat", "mileage": "47 kmpl", "image": "https://imgd.aeplcdn.com/1280x720/bw/models/suzuki-intruder-150-standard--bs-vi20200320182536.jpg", "website": "https://ramlalautomobiles.com/product/intruder-150-fi-abs/", "colors": ["Metallic Matte Titanium Silver", "Metallic Matte Black"]},
        {"name": "Royal Enfield Classic 350", "price": "₹2,50,909", "launch": "2021", "special": "Iconic design, thumping engine", "mileage": "35 kmpl","image": "https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/--redditch1738919737719.jpg?q=80", "website":"https://www.bikewale.com/royalenfield-bikes/classic-350/", "colors": ["Redditch Grey", "Halcyon Black", "Signals Marsh Grey", "Dark Stealth Black", "Chrome Bronze"]},
        {"name": "Bajaj Avenger Cruise 220", "price": "₹1,47,000", "launch": "2019", "special": "Low seat, comfortable cruiser", "mileage": "40 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/bw/models/colors/bajaj-select-model-auburn-black-1669289946200.png?q=80","website": "https://www.bajajauto.com/bikes/avenger/avenger-cruise-220", "colors": ["Auburn Black", "Moon White"]},
        {"name": "Jawa 42", "price": "₹2,42,000", "launch": "2020", "special": "Retro-modern looks, strong engine", "mileage": "37 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/jawa-42-1-channel-spoke-vega-white1723556329819.jpg?q=80","website":"https://www.jawamotorcycles.com/motorcycles/42", "colors": ["Halley’s Teal", "Starlight Blue", "Lumos Lime", "Comet Red", "Cosmic Carbon"]},
        {"name": "Honda H'ness CB350", "price": "₹2,64,000", "launch": "2021", "special": "Refined engine, modern features", "mileage": "35 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/--dlx-obd-2b1743781036971.jpg?q=80","website":"https://www.honda2wheelersindia.com/motorcycle/cb350-hness", "colors": ["Matte Marshal Green Metallic", "Matte Steel Black Metallic", "Pearl Nightstar Black", "Precious Red Metallic"]},
        {"name": "Royal Enfield Meteor 350", "price": "₹2,63,000", "launch": "2022", "special": "Touring comfort, modern features", "mileage": "41 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/51245/meteor-350-right-side-view-10.png?isig=0&q=80","website":"https://www.royalenfield.com/in/en/motorcycles/meteor/", "colors": ["Fireball Red", "Stellar Blue", "Supernova Brown", "Fireball Yellow", "Stellar Black"]},
        {"name": "Benelli Imperiale 400", "price": "₹2,35,000", "launch": "2021", "special": "Retro style, torquey engine", "mileage": "33 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/48694/imperiale-400-right-side-view.png?isig=0&q=80","website":"https://www.benelli.com/int-en/products/imperiale-400", "colors": ["Red", "Black", "Silver"]}
    ],
    "sports_bikes": [
        {"name": "Honda CBR150R", "price": "₹1,70,000", "launch": "2022", "special": "Lightweight sports bike, smooth engine", "mileage": "40 kmpl", "image": "https://imgd.aeplcdn.com/0x0/bikewaleimg/ec/530/img/l/Honda-CBR150-R-Side-1474.jpg", "website": "https://boonsiewhonda.com.my/product/honda-cbr150r/", "colors": ["Victory Black Red", "Honda Racing Red"]},
        {"name": "Yamaha R15 V4", "price": "₹1,89,000", "launch": "2021", "special": "Track focused, VVA engine", "mileage": "40 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/bw/models/colors/yamaha-select-model-metallic-red-1704802630538.png?q=80","website":"https://www.yamaha-motor-india.com/yamaha-r15v4.html", "colors": ["Metallic Red", "Racing Blue", "Dark Knight", "Intensity White"]},
        {"name": "KTM RC 200", "price": "₹2,54,000", "launch": "2020", "special": "Sharp styling, performance", "mileage": "35 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/bw/models/colors/ktm-select-model-gp-editiond-1670826275682.png?q=80","website":"https://www.ktmindia.com/ktm-bikes/supersport/ktm-rc-200", "colors": ["GP Edition", "Electronic Orange", "Dark Galvano"]},
        {"name": "TVS Apache RR 310", "price": "₹3,40,000", "launch": "2021", "special": "BMW engine, premium features", "mileage": "33 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/--red-without-quickshifter-obd-2b1744894903832.jpg?q=80","website":"https://www.tvsmotor.com/tvs-apache/super-premium/rr-310", "colors": ["Racing Red", "Titanium Black"]},
        {"name": "Bajaj Pulsar RS200", "price": "₹1,70,000", "launch": "2019", "special": "Affordable sports bike", "mileage": "35 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/46hj39b_1807569.jpg?q=80","website":"https://www.bajajauto.com/bikes/pulsar/pulsar-rs200", "colors": ["Pewter Grey", "Burnt Red", "White"]},
        {"name": "Suzuki Gixxer SF", "price": "₹1,35,000", "launch": "2022", "special": "Sporty faired bike, good mileage", "mileage": "45 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/--ride-connect-obd-2b1742989550749.jpg?q=80","website":"https://www.suzukimotorcycle.co.in/product-details/gixxer-sf", "colors": ["Metallic Triton Blue", "Glass Sparkle Black", "Metallic Sonic Silver"]},
        {"name": "Honda CBR 250R", "price": "₹679,900", "launch": "2018", "special": "Smooth engine, comfortable ride", "mileage": "30 kmpl","image":"https://imgd.aeplcdn.com/664x374/bw/models/honda-cbr-250r.jpg?20190103151915&q=80","website":"https://honda.com.np/motorcycle/cbr-250r/", "colors": ["Sports Red", "Pearl Amazing White", "Matte Axis Grey Metallic", "Matte Marvel Blue Metallic"]}
    ],
    "adventure_bikes": [
        {"name": "Kawasaki Versys-X 300", "price": "₹4,69,000", "launch": "2023", "special": "Lightweight adventure, long travel suspension", "mileage": "28 kmpl", "image": "https://www.kawasaki-india.com/content/dam/products/pim/studio/Resource_304580_23KLE300C_44SGN1DRF1CG_A.jpg", "website": "https://www.kawasaki-india.com/bikes/versys-x-300", "colors": ["Candy Lime Green", "Metallic Graphite Grey"]},
        {"name": "Royal Enfield Himalayan", "price": "₹ 3,55,890", "launch": "2021", "special": "Long travel suspension, off-road ready", "mileage": "30 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/110431/himalayan-450-left-front-three-quarter-2.jpeg?isig=0&q=80","website":"https://www.royalenfield.com/in/en/motorcycles/new-himalayan/", "colors": ["Slate Poppy Blue", "Slate Himalayan Salt", "Slate Himalayan Black", "Kaza Brown", "Kamet White"]},
        {"name": "Hero XPulse 200", "price": "₹1,51,500", "launch": "2020", "special": "Lightweight, best for trails", "mileage": "40 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/bw/models/colors/hero-select-model-sports-red-1707139187405.png?q=80","website":"https://www.heromotocorp.com/en-in/motorcycles/performance/xpulse-200-4v.html", "colors": ["Sports Red", "Matte Nexus Blue", "Polestar Blue", "Matte Black"]},
        {"name": "BMW G 310 GS", "price": "₹3,20,000", "launch": "2021", "special": "Premium adventure, BMW badge", "mileage": "28 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/126519/g-410-gs-right-side-view-3.png?isig=0&q=80","website":"https://www.bmwmotorcycles.com/en/models/adventure/g310gs.html", "colors": ["Racing Red", "Polar White", "Cosmic Black"]},
        {"name": "KTM Adventure 250", "price": "₹2,60,850", "launch": "2022", "special": "Off-road ABS, WP suspension", "mileage": "32 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/ktm-250-adventure-2025-standard1738766794300.jpg?q=80","website":"https://www.ktmindia.com/ktm-bikes/travel/2025-ktm-250-adventure", "colors": ["Electronic Orange", "Factory Racing Blue"]},
        {"name": "Suzuki V-Strom SX", "price": "₹2,39,000", "launch": "2022", "special": "Comfortable ADV, 250cc engine", "mileage": "36 kmpl","image":"https://imgd.aeplcdn.com/664x374/n/cw/ec/1/versions/--standard-20251736424652530.jpg?q=80","website":"https://www.suzukimotorcycle.co.in/product-details/v-strom-sx", "colors": ["Champion Yellow No. 2", "Pearl Blaze Orange", "Glass Sparkle Black"]}
    ]
}

# Home page: select category
@app.route('/', methods=['GET', 'POST'])
def index():
    categories = [
        ("budget_friendly", "Budget Friendly Bikes"),
        ("naked_bikes", "Naked Bikes"),
        ("cruiser_bikes", "Cruiser Bikes"),
        ("sports_bikes", "Sports Bikes"),
        ("adventure_bikes", "Adventure Bikes")
    ]
    if request.method == 'POST':
        selected_category = request.form.get('category')
        return render_template('bikes_list.html', category=selected_category, bikes=bikes[selected_category])
    return render_template('index.html', categories=categories)

# Show bikes in selected category and let user pick a bike
@app.route('/bikes', methods=['POST'])
def show_bikes():
    def parse_price(price_str):
        # Remove currency and commas, return int
        return int(price_str.replace('₹', '').replace(',', '').strip())

    category = request.form.get('category')
    selected_bike_name = request.form.get('bike_name')
    bike_list = []
    if isinstance(bikes[category], dict):
        gear_bikes = bikes[category].get('gear', [])
        non_gear_bikes = bikes[category].get('non_gear', [])
        bike_list = gear_bikes + non_gear_bikes
    else:
        bike_list = bikes[category]

    selected_bike = None
    emi_plan = None
    if selected_bike_name:
        for bike in bike_list:
            if bike['name'] == selected_bike_name:
                selected_bike = bike
                # Calculate EMI plan
                price = parse_price(bike['price'])
                emi_plan = {
                    '12': round(price / 12, 2),
                    '24': round(price / 24, 2),
                    '36': round(price / 36, 2)
                }
                break
    return render_template('bikes_list.html', category=category, bikes=bikes[category], bike_list=bike_list, selected_bike=selected_bike, emi_plan=emi_plan)

if __name__ == '__main__':
    app.run(debug=True)
