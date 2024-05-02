from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api, Resource
from .models import (
    videos,
    names
)

app = Flask(__name__)
api = Api(app)

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        request.method
        return {}

api.add_resource(Video, '/video/<int:video_id>/')

class WorldGet(Resource):
    def get(self, name):
        return names[name]

    # def get(self, name, test):
    #     # return {'hello': 'world'}
    #     return {
    #         'name': name,
    #         'test': test
    #     }


class WorldPost(Resource):
    def post(self):
        # return {'hello': 'world'}
        return {'post_data': 'hello world'}


api.add_resource(WorldGet, '/hello/<string:name>/')
api.add_resource(WorldPost, '/he/post')
# api.add_resource(HelloWorld, '/hello/<string:name>/<int:test>/')
if __name__ == '__main__':
    app.run(debug=True)
