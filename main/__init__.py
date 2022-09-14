import logging

import azure.functions as func
from flask import Flask, request, redirect

app = Flask(__name__)

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the WSGI handler.
    """
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)

@app.route("/")
def index():
    logging.info('Python HTTP trigger function processed a request.')
    
    referer = request.headers.get("Referer", "")
    logging.info(f"got a referer: {referer}")

    if referer.startswith("https://github.com"):
        url_part = referer.split("https://github.com/")[-1]
        vscode_redirect = f"https://vscode.dev/github/{url_part}"
    else:
        vscode_redirect = "https://vscode.dev/"

    return redirect(vscode_redirect, code=302)
    #return func.HttpResponse(vscode_redirect, status_code=302)


