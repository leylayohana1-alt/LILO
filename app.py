# app.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dulceeden123"

productos = {

    "pasteles":[

        {
            "nombre":"Pastel de Chocolate",
            "precio":60,
            "imagen":"https://www.cocinadelirante.com/800x600/filters:format(webp):quality(75)/sites/default/files/images/2023/08/receta-de-pastel-de-chocolate-facil.jpg"
        },

        {
            "nombre":"Pastel de Fresa",
            "precio":50,
            "imagen":"https://www.elle-et-vire.com/uploads/cache/930w/uploads/recip/recipe/3779/6377ad3abb209_bra004354-iconic-strawberry-ca.jpg"
        },

        {
            "nombre":"Pastel de Cumpleaños",
            "precio":50,
            "imagen":"https://yanubapasteleria.com/wp-content/uploads/2022/01/Nuevo-proyecto-23.jpg"
        },

        {
            "nombre":"Pastel de Cumpleaños",
            "precio":100,
            "imagen":"https://wiltonenespanol.com/wp-content/uploads/2020/11/Sprinkle-on-the-Fun-Birthday-Cake.jpg"
        },

        {
            "nombre":"Pastel de Cumpleaños",
            "precio":300,
            "imagen":"https://www.marialunarillos.com/blog/wp-content/uploads/2023/01/receta-tarta-infantil-cumpleanos-animalitos-0.jpg"
        },

        {
            "nombre":"Pastel de Boda",
            "precio":700,
            "imagen":"https://images.unsplash.com/photo-1623428454614-abaf00244e52?q=80&w=387&auto=format&fit=crop"
        },

        {
            "nombre":"Pastel de Boda",
            "precio":500,
            "imagen":"https://plus.unsplash.com/premium_photo-1675720060105-ba50ca9e21a7?q=80&w=871&auto=format&fit=crop"
        },

        {
            "nombre":"Pastel de Boda",
            "precio":700,
            "imagen":"https://images.unsplash.com/photo-1519654793190-2e8a4806f1f2?q=80&w=387&auto=format&fit=crop"
        }

    ],

    "bebidas":[

        {
            "nombre":"Café Latte",
            "precio":10,
            "imagen":"https://www.cuisinart.com/dw/image/v2/ABAF_PRD/on/demandware.static/-/Sites-us-cuisinart-sfra-Library/default/dw42dcae51/images/recipe-Images/cafe-latte1-recipe_resized.jpg"
        },

        {
            "nombre":"Capuccino",
            "precio":12,
            "imagen":"https://www.cabucoffee.com/newimages/Guia-Cappuccino.jpg"
        }
    ],
    "panes_dulces":[
    
            {
                "nombre":"trufas",
                "precio":10,
                "imagen":"https://dulcesperu.com/wp-content/uploads/2025/12/trufas-navidad-1.jpg"
            },
    
            {
                "nombre":"muffins",
                "precio":12,
                "imagen":"https://cdn.vegkit.com/wp-content/uploads/sites/2/2024/02/18160130/berry_muffins_1.jpg"
            },

            {
              "nombre":"pan de masa madre",
                 "precio":12,
                "imagen":"https://veggiefestchicago.org/wp-content/uploads/2025/01/AdobeStock_968234066.jpg"
            }
        ]

}
@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/registro", methods=["GET", "POST"])
def registro():

    mensaje = ""

    if request.method == "POST":

        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]

        with open("registros.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{correo},{telefono}\n")

        mensaje = "Registro guardado correctamente"

    return render_template(
        "registro.html",
        mensaje=mensaje
    )


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/carrito")
def carrito():

    carrito = session.get("carrito", [])

    total = sum(
        float(producto["precio"])
        for producto in carrito
    )

    return render_template(
        "carrito.html",
        carrito=carrito,
        total=total
    )


@app.route("/vaciar")
def vaciar():

    session["carrito"] = []

    return redirect(url_for("carrito"))

@app.route("/pasteles")
def pasteles():
    return render_template(
        "pasteles.html",
        productos=productos["pasteles"]
    )


@app.route("/bebidas")
def bebidas():
    return render_template(
        "bebidas.html",
        productos=productos["bebidas"]
    )


@app.route("/panes_dulces")
def panes_dulces():
    return render_template(
        "panes_dulces.html",
        productos=productos["panes y dulces"]
    )


@app.route("/agregar")
def agregar():

    nombre = request.args.get("nombre")
    precio = float(request.args.get("precio"))

    carrito = session.get("carrito", [])

    carrito.append({
        "nombre": nombre,
        "precio": precio
    })

    session["carrito"] = carrito

    return redirect(url_for("carrito"))

if __name__ == "__main__":
    app.run(debug=True)