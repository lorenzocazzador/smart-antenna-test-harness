import re

def parse_and_generate_html():
    try:
        with open("output.log", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("[ERROR] output.log not found.")
        return

    status_lines = re.findall(r"\[(PASS|FAIL)] (.+)", content)

    html = "<html><head><title>Test Report</title></head><body><h2>Test Results</h2><ul>"
    for status, message in status_lines:
        color = "green" if status == "PASS" else "red"
        html += f"<li style='color:{color};'>{status}: {message}</li>"
    html += "</ul></body></html>"

    with open("report.html", "w") as f:
        f.write(html)
    print("[Viewer] report.html generated")

if __name__ == "__main__":
    parse_and_generate_html()
