from flask import Flask, request, jsonify, abort

from service import JobsService

app = Flask("Simple Flask")


@app.route("/")
def hello():
    return "Service is working"


@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 404


@app.route("/jobs", methods=["GET"])
def all_jobs():
    args = request.args
    if len(args) == 0:
        return jsonify(JobsService().get_all_jobs())
    else:
        # check if request parameters are valid
        for arg_key in args:
            if arg_key != 'tags':
                abort(400, description='Invalid usage')
        return jsonify(JobsService().get_filtered_jobs(args.get('tags')))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
