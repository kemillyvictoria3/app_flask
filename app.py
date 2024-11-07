from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])

        # Cálculo do IMC
        imc = peso / (altura ** 2)

        # Definindo a classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 34.9:
            classificacao = "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            classificacao = "Obesidade grau 2"
        else:
            classificacao = "Obesidade grau 3"

        return render_template("index.html", nome=nome, imc=imc, classificacao=classificacao)
    
    return render_template("index.html", nome=None, imc=None, classificacao=None)

if __name__ == "__main__":
    app.run(debug=True)
