from flask import Flask, render_template, session
import random


app = Flask(__name__,template_folder="templates")
app.debug = True
app.secret_key='ajksdnk'
@app.route('/')
def hod_kostkou():
    hod = random.randint(1,6)
    hodpc = random.randint(1,6)

    if not 'hod' in session:
        session['hod'] = 0
        session['hodpc'] = 0

 
    if (hod > hodpc):
        vyhra="Vyhral jsi!"
        session['hod'] = session['hod'] + 1

    elif (hod < hodpc):
        vyhra="Prohral jsi"
        session['hodpc'] = session['hodpc'] + 1

    else:
        vyhra="remiza!"

    HracVyhra = session['hod'] 
    PcVyhra = session['hodpc'] 


    return render_template('index.html', hod=hod,hodpc=hodpc , vyhra=vyhra, HracVyhra = HracVyhra, PcVyhra = PcVyhra)

if __name__ == '__main__':
    app.run()