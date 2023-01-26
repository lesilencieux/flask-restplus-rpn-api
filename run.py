from rpn_api import create_app
import logging

app = create_app()

if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    app.run(host='0.0.0.0',debug=True)