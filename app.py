from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template using render_template_string for simplicity
HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f5f5f5; text-align: center; padding-top: 50px; }
        input, button { padding: 10px; font-size: 16px; margin: 5px; }
        table { margin: 20px auto; border-collapse: collapse; background: white; }
        td, th { border: 1px solid #ccc; padding: 10px 20px; }
        th { background: #4CAF50; color: white; }
    </style>
</head>
<body>
    <h1>Multiplication Table Generator</h1>
    <form method="POST">
        <input type="number" name="number" placeholder="Enter a number" required>
        <button type="submit">Show Table</button>
    </form>

    {% if table %}
    <h2>Table of {{ number }}</h2>
    <table>
        <tr><th>Expression</th><th>Result</th></tr>
        {% for expr, result in table %}
            <tr><td>{{ expr }}</td><td>{{ result }}</td></tr>
        {% endfor %}
    </table>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    table = None
    number = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table = [(f"{number} x {i}", number * i) for i in range(1, 11)]
        except ValueError:
            table = None
    return render_template_string(HTML_PAGE, table=table, number=number)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
