from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<h2>Calculator</h2>
<form method="get">
  A: <input type="number" name="a"><br><br>
  B: <input type="number" name="b"><br><br>
  <button name="op" value="add">Add</button>
  <button name="op" value="sub">Sub</button>
  <button name="op" value="mul">Mul</button>
  <button name="op" value="div">Div</button>
</form>

{% if result is not none %}
<h3>Result: {{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET"])
def calculator():
    result = None
    if "a" in request.args and "b" in request.args:
        a = int(request.args["a"])
        b = int(request.args["b"])
        op = request.args["op"]

        if op == "add": result = a + b
        if op == "sub": result = a - b
        if op == "mul": result = a * b
        if op == "div": result = a / b

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
