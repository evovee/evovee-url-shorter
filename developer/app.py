import re
import hashlib
from utils import Database
from flask import Flask, request, render_template
import json


app = Flask(__name__)
db = Database()

@app.route("/<short_url>")
def redirect_url(short_url):
    """
    TODO: Il flusso generale sarebbe il seguente:
        L'utente inserisce l'URL originale in una form sul tuo sito web.

        Quando l'utente clicca sul bottone di accorciamento, viene inviata una richiesta al tuo server, che esegue il
        codice di accorciamento dell'URL.

        Il server restituisce l'URL accorciato all'utente, che lo copia e lo incolla in un'altra scheda del browser.

        Quando l'utente visita l'URL accorciato, la richiesta viene inviata al tuo server.

        Il tuo server verifica l'URL accorciato nella base dati delle associazioni URL accorciati/URL originali.

        Se l'URL accorciato è presente nella base dati, il server restituisce un comando di reindirizzamento all'URL originale.

        Il browser dell'utente riceve il comando di reindirizzamento e rendirizza l'utente all'URL originale.
    """

# @app.route('/')
# def docs():
#     return json.loads(open("./API/api.json", "r").read())

@app.route('/')
def docs():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/api/url/create', methods=["POST"])
def create():
    """
    In sintesi, la funzione accorcia un URL originale, memorizza l'associazione tra URL accorciato e URL
    originale e restituisce l'URL accorciato come risultato.
    :return: dict{url:url}
    """
    url = request.json["url"]
    if re.match(
            "^(http://www.|https://www.|http://|https://)?[a-z0-9]+([-.]{1}[a-z0-9]+)*.[a-z]{2,5}(:[0-9]{1,5})?(/.*)?$",
            url):
        """

        Questa condizione utilizza un'espressione regolare per effettuare la verifica. L'espressione regolare è 
        costruita con l'obiettivo di verificare se l'URL soddisfa un particolare formato.

        L'espressione regolare verifica se l'URL inizia con http://www., https://www., http:// o https:// (questi sono 
        tutti opzionali), seguiti da una serie di caratteri alfanumerici, un punto o un trattino, seguiti da un altro 
        insieme di caratteri alfanumerici, un punto seguito da due a cinque caratteri alfabetici, una stringa opzionale 
        che rappresenta una porta (seguita da : e da un numero compreso tra 1 e 5 cifre), seguita da un'altra stringa 
        opzionale che rappresenta il percorso (seguita da / e una stringa qualsiasi).
        
        """
        h = hashlib.sha1(url.encode())
        shortened_url = h.hexdigest()[:8]
        return {"shouft.it/" + shortened_url: db.addUrl(request.get_json()["url"])}
        """
        REMINDER:
            Il metodo request.get_json è una funzione presente in Flask che permette di recuperare i dati inviati nel 
            corpo di una richiesta HTTP POST codificati in formato JSON. Questo metodo cerca di decodificare il contenuto
            della richiesta e restituisce un dizionario Python con i dati codificati. Nel codice in questione, 
            request.get_json()["url"] restituisce il valore associato alla chiave "url" all'interno del dizionario 
            decodificato dalla richiesta HTTP.
        """

    else:
        return "Non è un URL valido."



@app.route('/api/url/get')
def get_url():
    args = request.args.get("refer")

    return {"url": db.getUrl(args)}


if __name__ == "__main__":
    app.run()

