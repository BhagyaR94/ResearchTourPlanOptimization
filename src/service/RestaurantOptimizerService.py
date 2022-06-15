from src.model.Destination import Destination


class RestaurantOptimizerService:
    def __init__(self):
        self

    restaurants = [
        Destination('Sinhagiri Bakery and Restaurant', 'value', '1', 'low', 'local', 6.8303173, 80.9889498),
        Destination('Gami Gedara', 'value', '1', 'medium', 'local', 6.830180989112515, 80.99775805011357),
        Destination('Q Dine', 'value', '1', 'medium', 'foreign', 6.82715561464838, 80.98775877538107),
        Destination('Chandanie Bakery', 'value', '1', 'low', 'local', 6.8416040007729135, 80.98749268245219),
        Destination('Weeragiri Bakery', 'value', '1', 'low', 'local', 6.831213933811575, 80.99277559889718),
        Destination('Banda Food Family Restaurant', 'value', '1', 'medium', 'foreign', 6.836432389648007,
                    80.99003941313659),
        Destination('Dulsara Restaurant', 'value', '1', 'low', 'local', 6.986079540138897, 81.05989839095038),
        Destination('New Kitchen', 'value', '1', 'low', 'local', 6.985447166016313, 81.05921777215976),
        Destination('Golden Cafe', 'value', '1', 'low', 'local', 6.982805780143674, 81.04513563523938),
        Destination('Dosa Cafe', 'value', '1', 'low', 'foreign', 6.9856443344769135, 81.05883316222598),
        Destination('BB King', 'value', '1', 'low', 'local', 6.984186279514103, 81.05894322174598),
        Destination('MozzarElla By Nero Kitchen', 'value', '1', 'medium', 'foreign', 6.874853028991515,
                    81.04761784078565),
        Destination('Café UFO Ella', 'value', '1', 'medium', 'foreign', 6.874564732534412, 81.04862449475905),
        Destination('Jade Green', 'value', '1', 'medium', 'foreign', 6.873537233041744, 81.0492631217457),
        Destination('Cafe Chill', 'value', '1', 'medium', 'foreign', 6.874357470661339, 81.0489917315414),
        Destination('Raha Ella', 'value', '1', 'medium', 'foreign', 6.873269671027809, 81.0499106677723),
        Destination('Ella Village Restaurant', 'value', '1', 'medium', 'foreign', 6.874610909821841, 81.04814669119497),
        Destination('Global Kitchen', 'value', '1', 'medium', 'foreign', 7.296431124132381, 80.63703432174671),
        Destination('Indian Summer Restaurant', 'value', '1', 'medium', 'foreign', 7.296629827559141,
                    80.63714489660886),
        Destination('Vito Wood Fired Pizza', 'value', '1', 'medium', 'foreign', 7.288043527128633, 80.64298764078657),
        Destination('Theva Cuisine', 'value', '1', 'medium', 'foreign', 7.276244784325804, 80.63627820655456),
        Destination('Theva Cuisine', 'value', '1', 'medium', 'foreign', 7.276244784325804, 80.63627820655456),
        Destination('Honey Pot Restaurant', 'value', '1', 'medium', 'foreign', 7.27661701606932, 80.60734330770191),
        Destination('Themparadu', 'value', '1', 'medium', 'foreign', 6.96654528681269, 80.77269091989707),
        Destination('Grand Thai', 'value', '1', 'medium', 'foreign', 6.968812989044083, 80.76564311195028),
        Destination('The Sackville', 'value', '1', 'medium', 'foreign', 6.982003279069557, 80.75417770640374),
        Destination('Salmiya Italian Restaurant', 'value', '1', 'medium', 'foreign', 6.958310392023373,
                    80.77343835243033),
        Destination('Grand Indian', 'value', '1', 'medium', 'foreign', 6.967952738112743, 80.76626186962137),
        Destination('Kenoli Restaurant', 'value', '1', 'medium', 'foreign', 7.949604808991514, 80.75032586777513),
        Destination('Shenadi Restaurant', 'value', '1', 'medium', 'foreign', 7.951711902437607, 80.75504499845955),
        Destination('Nirwana Restaurant', 'value', '1', 'medium', 'foreign', 7.950153885880235, 80.75061005243295),
        Destination('Pradeep Restaurant', 'value', '1', 'medium', 'foreign', 7.951967007766221, 80.75481177941967),
        Destination('Wijesiri Family Restaurant', 'value', '1', 'medium', 'foreign', 7.952046315845543,
                    80.75482618496623),
        Destination('Sakura Restaurant', 'value', '1', 'medium', 'foreign', 7.901716006780035, 80.66886168921513),
        Destination('Rithu Restaurant', 'value', '1', 'medium', 'foreign', 7.930901666236862, 80.70339016592624),
        Destination('Sandra Restaurant', 'value', '1', 'medium', 'foreign', 7.851427546540246, 80.65542071749915),
        Destination('Athula Restaurant', 'value', '1', 'medium', 'foreign', 7.845797105664468, 80.65506167332137),
        Destination('P&S Restaurant', 'value', '1', 'medium', 'foreign', 7.851691587722094, 80.63738100825495),
        Destination('O Mirissa Cafe And Bistro', 'value', '1', 'medium', 'foreign', 5.94570123364932,
                    80.46057679845508),
        Destination('Flora and Fauna Restaurant Mirissa Beach', 'value', '1', 'medium', 'foreign', 5.945060007036857,
                    80.46154213653487),
        Destination('Margherita Italiano Restaurant', 'value', '1', 'medium', 'foreign', 5.948640174868247,
                    80.45703026961954),
        Destination('Adora Mirissa Beach Restaurant', 'value', '1', 'medium', 'foreign', 5.941767062075079,
                    80.46695918921085),
        Destination('Ambrosia Roti Shop', 'value', '1', 'medium', 'foreign', 5.947502646355471, 80.46110652174409),
        Destination('Mr Fisherman', 'value', '1', 'medium', 'foreign', 6.842267286302822, 81.83253475058125),
        Destination('Bambinis Cafe Shop', 'value', '1', 'medium', 'foreign', 6.847942479543525, 81.83114486962111),
        Destination('The Sketch', 'value', '1', 'medium', 'foreign', 6.842972828799196, 81.8305471984567),
        Destination('Arugam Bay Seafood Restaurant', 'value', '1', 'medium', 'foreign', 6.846328315703019,
                    81.83129821680187),
        Destination('Thanduri Hut Arugam Bay', 'value', '1', 'medium', 'foreign', 6.8454838421500375,
                    81.83050339475898),



    ]
