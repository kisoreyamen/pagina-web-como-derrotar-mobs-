# Importar
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La primera página
@app.route('/')
def index():
    return render_template('index.html')
# Segunda página
@app.route("/nomuertos")
def nomuertos():
    return render_template(
                            'lights.html',
                           )

# La tercera página
@app.route('/mayoria')
def mayoria():
    return render_template(
                            'electronics.html',                                                     
                           )

# La tercera página
@app.route('/acuaticos')
def acuaticos():
    return render_template(
                            'acuaticos.html',                                                     
                           )

# aldeano zombi
@app.route('/aldeanozombi')
def aldeanozombi():
    return render_template(
                            'aldeanozombi.html',                                                     
                           )

# esqueleto
@app.route('/esqueleto')
def esqueleto():
    return render_template(
                            'esqueleto.html',                                                     
                           )

# ghast
@app.route('/ghast')
def ghast():
    return render_template(
                            'ghast.html',                                                     
                           )

# pez globo
@app.route('/pezglobo')
def pezglobo():
    return render_template(
                            'pezglobo.html',                                                     
                           )

# creeper
@app.route('/creeper')
def creeper():
    return render_template(
                            'creeper.html',                                                     
                           )

# delfin
@app.route('/delfin')
def delfin():
    return render_template(
                            'delfin.html',                                                     
                           )

# guardian
@app.route('/guardian')
def guardian():
    return render_template(
                            'guardian.html',                                                     
                           )

# guardian anciano
@app.route('/guardiananciano')
def guardiananciano():
    return render_template(
                            'guardiananciano.html',                                                     
                           )

# creaking
@app.route('/creaking')
def creaking():
    return render_template(
                            'creaking.html',                                                     
                           )

# zombie
@app.route('/zombie')
def zombie():
    return render_template(
                            'zombie.html',                                                     
                           )

# araña
@app.route('/arana')
def arana():
    return render_template(
                            'arana.html',                                                     
                           )

# slime
@app.route('/slime')
def slime():
    return render_template(
                            'slime.html',                                                     
                           )

# bruja
@app.route('/bruja')
def bruja():
    return render_template(
                            'bruja.html',                                                     
                           )

# enderman
@app.route('/enderman')
def enderman():
    return render_template(
                            'enderman.html',                                                     
                           )

# blaze
@app.route('/blaze')
def blaze():
    return render_template(
                            'blaze.html',                                                     
                           )

# ender dragon
@app.route('/enderdragon')
def enderdragon():
    return render_template(
                            'enderdragon.html',                                                     
                           )

# ahogado
@app.route('/ahogado')
def ahogado():
    return render_template(
                            'ahogado.html',                                                     
                           )

# husk
@app.route('/husk')
def husk():
    return render_template(
                            'husk.html',                                                     
                           )

# breeze
@app.route('/breeze')
def breeze():
    return render_template(
                            'breeze.html',                                                     
                           )

# evocador
@app.route('/evocador')
def evocador():
    return render_template(
                            'evocador.html',                                                     
                           )

# vex
@app.route('/vex')
def vex():
    return render_template(
                            'vex.html',                                                     
                           )

# shulker
@app.route('/shulker')
def shulker():
    return render_template(
                            'shulker.html',                                                     
                           )

# esqueleto wither
@app.route('/esqueletowither')
def esqueletowither():
    return render_template(
                            'esqueletowither.html',                                                     
                           )

# zoglin
@app.route('/zoglin')
def zoglin():
    return render_template(
                            'zoglin.html',                                                     
                           )

# piglin zombificado
@app.route('/piglinzombificado')
def piglinzombificado():
    return render_template(
                            'piglinzombificado.html',                                                     
                           )

# wither
@app.route('/wither')
def wither():
    return render_template(
                            'wither.html',                                                     
                           )

# errante
@app.route('/errante')
def errante():
    return render_template(
                            'errante.html',                                                     
                           )

# phantom
@app.route('/phantom')
def phantom():
    return render_template(
                            'phantom.html',                                                     
                           )

# bogged
@app.route('/bogged')
def bogged():
    return render_template(
                            'bogged.html',                                                     
                           )

# abeja
@app.route('/abeja')
def abeja():
    return render_template(
                            'abeja.html',                                                     
                           )

# arana de cueva
@app.route('/aranadecueva')
def aranadecueva():
    return render_template(
                            'aranadecueva.html',                                                     
                           )

# zorro
@app.route('/zorro')
def zorro():
    return render_template(
                            'zorro.html',                                                     
                           )

# cabra
@app.route('/cabra')
def cabra():
    return render_template(
                            'cabra.html',                                                     
                           )

# iron golem
@app.route('/irongolem')
def irongolem():
    return render_template(
                            'irongolem.html',                                                     
                           )

# cubo de magma
@app.route('/cubodemagma')
def cubodemagma():
    return render_template(
                            'cubodemagma.html',                                                     
                           )

# devastador
@app.route('/devastador')
def devastador():
    return render_template(
                            'devastador.html',                                                     
                           )

# vindicador
@app.route('/vindicador')
def vindicador():
    return render_template(
                            'vindicador.html',                                                     
                           )

# warden
@app.route('/warden')
def warden():
    return render_template(
                            'warden.html',                                                     
                           )

# panda
@app.route('/panda')
def panda():
    return render_template(
                            'panda.html',                                                     
                           )

# llama
@app.route('/llama')
def llama():
    return render_template(
                            'llama.html',                                                     
                           )

# llama comerciante errante
@app.route('/llamacomerciante')
def llamacomerciante():
    return render_template(
                            'llamacomerciante.html',                                                     
                           )

# lobo
@app.route('/lobo')
def lobo():
    return render_template(
                            'lobo.html',                                                     
                           )

# oso polar
@app.route('/osopolar')
def osopolar():
    return render_template(
                            'osopolar.html',                                                     
                           )

# piglin
@app.route('/piglin')
def piglin():
    return render_template(
                            'piglin.html',                                                     
                           )

# silverfish
@app.route('/silverfish')
def silverfish():
    return render_template(
                            'silverfish.html',                                                     
                           )

# saqueador
@app.route('/saqueador')
def saqueador():
    return render_template(
                            'saqueador.html',                                                     
                           )

# piglin bruto
@app.route('/piglinbruto')
def piglinbruto():
    return render_template(
                            'piglinbruto.html',                                                     
                           )

# hoglin
@app.route('/hoglin')
def hoglin():
    return render_template(
                            'hoglin.html',                                                     
                           )

# endermite
@app.route('/endermite')
def endermite():
    return render_template(
                            'endermite.html',                                                     
                           )



# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# El formulario
@app.route('/form')
def form():
    return render_template('form.html')

#Resultados del formulario
@app.route('/submit', methods=['POST'])
def submit_form():
    # Declarar variables para la recogida de datos
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    # Puedes guardar tus datos o enviarlos por correo electrónico
    return render_template('form_result.html', 
                           # Coloque aquí las variables
                           name=name, email = email,
                           address = address, date = date
                           )

app.run(debug=True)
