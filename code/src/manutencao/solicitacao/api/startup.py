from flask import Flask, request

from manutencao.solicitacao.bootstrap import injector


def create_app():
    app = Flask(__name__)

    # setup with the configuration provided by the user / environment
    """app.config.from_object(os.environ['APP_SETTINGS'])"""

    app.config['SECRETY_KEY'] = 'TESTE'

    injector.injector(app, request)

    return app


if __name__ == '__main__':
    create_app().run(host="0.0.0.0", port=81, debug=True)



