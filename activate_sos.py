


# sos.py (Flask code)
from flask import Flask
from main import eas_sound  # Import your sound generation logic
from waitress import serve
from paste.translogger import TransLogger
import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)





app = Flask(__name__)

@app.route('/activate_sos', methods=['POST'])
def activate_sos():
    try:
        app.logger.info("SOS activated!")
        eas_sound()
        return "SOS activated!"
    except Exception as e:
        app.logger.error(f"Error activating SOS: {str(e)}")
        return "Error activating SOS"



if __name__ == '__main__':
    serve(TransLogger(app, setup_console_handler=False), host='127.0.0.1', port=9999)

