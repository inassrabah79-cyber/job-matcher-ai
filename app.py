from flask import Flask, request, jsonify
from matcher import JobMatcher

app = Flask(__name__)


@app.route("/job_match", methods=["POST"])
def job_match():

    data = request.get_json()
    cv_text = data.get("cv_text")

    if not cv_text:
        return jsonify({
            "success": False,
            "message": "Missing CV text"
        }), 400

    matcher = JobMatcher(cv_text)
    matcher.encode_cv()

    result = matcher.match()

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)