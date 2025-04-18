from flask import Flask, render_template
import os
import datetime

app = Flask(__name__)

LOG_FILE = "output.log"

def parse_log():
    results = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            for line in f:
                line = line.strip()
                status = "neutral"
                if "[PASS]" in line:
                    status = "pass"
                elif "[FAIL]" in line:
                    status = "fail"
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                results.append({"line": line, "status": status, "timestamp": timestamp})
    return results

@app.route('/')
def index():
    log_lines = parse_log()
    return render_template("index.html", logs=log_lines)

if __name__ == "__main__":
    app.run(debug=True)
