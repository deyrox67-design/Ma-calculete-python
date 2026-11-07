from flask import Flask, request, render_template_string

app = Flask(__name__)

page = """
<h1>Ma première calculatrice</h1>

<form method="POST">
    <input type="number" step="any" name="a"
    placeholder="Premier nombre" required>

    <input type="number" step="any" name="b"
    placeholder="Deuxième nombre" required>

    <button type="submit">Calculer</button>
</form>

{% if resultat is not none %}
<h2>Résultats</h2>
<p>Addition : {{ resultat[0] }}</p>
<p>Soustraction : {{ resultat[1] }}</p>
<p>Multiplication : {{ resultat[2] }}</p>
<p>Division : {{ resultat[3] }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def accueil():
    resultat = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])

        division = a / b if b != 0 else "Impossible"

        resultat = (
            a + b,
            a - b,
            a * b,
            division
        )

    return render_template_string(page, resultat=resultat)
