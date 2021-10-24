import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

sports = []
sports_list = [
    "https://images.complex.com/complex/images/c_fill,dpr_auto,f_auto,q_90,w_1400/fl_lossy,pg_1/isy0qmbfazbupgmsgpnr/basektball-net",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQviJ2Un-svkkNv6TRg1N1UqEna3fe4UZotQ&usqp=CAU",
    "https://lakelandmom.com/wp-content/uploads/2021/01/Baseball-Teams-Lakeland-Florida.jpg",
    "https://www.ocf.berkeley.edu/~ugradsa/static/usa_website/images/blog/rp/spring_2019/winning-the-mlb-world-series/title_pic.png",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRavmpdYS_63GP6HwSwsA6xv5O8bXbBkSv-8w&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyV_BFKggZtifXZVhXVbML8erVNuqQowElcA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGgwuKPJUZ3kFD4kMgaNfkOl44cWVHoP2Feg&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREwDYc49_qZLLvzVJ0H_xWz2M-KtAMS1jgTQ&usqp=CAU"
]

def find_next_id():
    return max(sports["id"] for sport in sports) + 1


def _init_sports():
    id = 1
    for sport in sports_list:
        sports.append({"id": id, "sport": sport, "haha": 0, "boohoo": 0})
        id += 1

@api_bp.route('/sport')
def get_sport():
    if len(sports) == 0:
        _init_sports()
    return jsonify(random.choice(sports))

@api_bp.route('/sports')
def get_sports():
    if len(sports) == 0:
        _init_sports()
    return jsonify(sports)


if __name__ == "__main__":
    print(random.choice(sports_list))