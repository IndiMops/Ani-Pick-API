import json
import random
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self):
        return {
            "method": "GET",
            "info": {
                "name": "Ani Pick",
                "version": "1.0.1",
                "description": "A variety of anime images on different occasions",
                "license": {
                    "type": "MIT",
                    "url": "https://github.com/IndiMops/Ani-Pick.py/blob/master/LICENSE"
                },
                "homepage": "https://ani-pick.xyz",
                "repository": "https://github.com/IndiMops/Ani-Pick.py",
                "documentation": "https://docs.ani-pick.xyz",
                "author": {
                    "name": "Indi Mops",
                    "profile": "https://github.com/IndiMops"
                }
            },
            "v1": {
                "sfw": {
                    "images": {
                        "tag": {
                            0: "kiss",
                            1: "slap",
                            2: "ask",
                            3: "bite",
                            4: "eat",
                            5: "cuddle",
                            6: "glare",
                            7: "highfive",
                            8: "hug",
                            9: "lick",
                            10: "pat",
                            11: "poke",
                            12: "punch",
                            13: "cry",
                            14: "hungry",
                            15: "angry",
                            16: "boring",
                            17: "tired",
                            18: "scary",
                            19: "thinking",
                            20: "smarty",
                            21: "smile",
                            22: "uniform",
                            23: "maid",
                            24: "waifu",
                            25: "oppai",
                            26: "selfies",
                            27: "poker-face"
                        }
                    },
                    "wallpers": {
                        "tag": {
                            0: "Desktop",
                            1: "Mobile",
                            2: "Collection",
                            3: "Multi-monitor",
                            4: "Animated"
                        }
                    }
                },
                "nsfw": {
                    "images": {
                        "tag": {
                            0: "ass",
                            1: "hentai",
                            2: "milf",
                            3: "oral",
                            4: "paizuri",
                            5: "ecchi",
                            6: "ero"
                        }
                    },
                    "wallpers": {
                        "tag": {
                            0: "Desktop",
                            1: "Mobile",
                            2: "Collection",
                            3: "Multi-monitor",
                            4: "Animated"
                        }
                    }
                }
            }
        }

class Main_v1(Resource):
    def get(self):
        return {
            "method": "GET",
            "info": {
                "name": "Ani Pick",
                "version": "1.0.1",
                "description": "A variety of anime images on different occasions",
                "license": {
                    "type": "MIT",
                    "url": "https://github.com/IndiMops/Ani-Pick.py/blob/master/LICENSE"
                },
                "homepage": "https://ani-pick.xyz",
                "repository": "https://github.com/IndiMops/Ani-Pick.py",
                "documentation": "https://docs.ani-pick.xyz",
                "author": {
                    "name": "Indi Mops",
                    "profile": "https://github.com/IndiMops"
                }
            },
            "v1": {
                "sfw": {
                    "images": {
                        "tag": {
                            0: "kiss",
                            1: "slap",
                            2: "ask",
                            3: "bite",
                            4: "eat",
                            5: "cuddle",
                            6: "glare",
                            7: "highfive",
                            8: "hug",
                            9: "lick",
                            10: "pat",
                            11: "poke",
                            12: "punch",
                            13: "cry",
                            14: "hungry",
                            15: "angry",
                            16: "boring",
                            17: "tired",
                            18: "scary",
                            19: "thinking",
                            20: "smarty",
                            21: "smile",
                            22: "uniform",
                            23: "maid",
                            24: "waifu",
                            25: "oppai",
                            26: "selfies",
                            27: "poker-face"
                        }
                    },
                    "wallpers": {
                        "tag": {
                            0: "Desktop",
                            1: "Mobile",
                            2: "Collection",
                            3: "Multi-monitor",
                            4: "Animated"
                        }
                    }
                },
                "nsfw": {
                    "images": {
                        "tag": {
                            0: "ass",
                            1: "hentai",
                            2: "milf",
                            3: "oral",
                            4: "paizuri",
                            5: "ecchi",
                            6: "ero"
                        }
                    },
                    "wallpers": {
                        "tag": {
                            0: "Desktop",
                            1: "Mobile",
                            2: "Collection",
                            3: "Multi-monitor",
                            4: "Animated"
                        }
                    }
                }
            }
        }

class SfwImageKiss(Resource):
    def get(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
        all_img = len(data['sfw']['images']['kiss']) - 1
        return data['sfw']['images']['kiss'][f'{random.randint(0, all_img)}']

class SfwImageSlap(Resource):
    def get(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
        all_img = len(data['sfw']['images']['slap']) - 1
        return data['sfw']['images']['slap'][f'{random.randint(0, all_img)}']

api.add_resource(Main, "/api")
api.add_resource(Main_v1, "/api/v1")
api.add_resource(SfwImageKiss, "/api/v1/sfw/kiss")
api.add_resource(SfwImageSlap, "/api/v1/sfw/slap")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
