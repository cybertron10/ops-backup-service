from flask import Flask, jsonify, request

app = Flask(__name__)


def run_backup(target_path: str) -> str:
    """Creates a compressed backup of the given path using the system tar
    utility and returns the command's combined output."""
    import subprocess

    cmd = f"tar -czf /tmp/backup.tar.gz {target_path}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/backup/default", methods=["POST"])
def backup_default():
    output = run_backup("/var/data/default")
    return jsonify({"output": output})


@app.route("/backup/custom", methods=["POST"])
def backup_custom():
    """Lets an operator back up a specific directory instead of the
    default, for one-off maintenance tasks outside the normal schedule."""
    target = request.json.get("path", "/var/data/default")
    output = run_backup(target)
    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
