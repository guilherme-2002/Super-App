from flask import jsonify
from . import app, auth, log
from .models import Profile

@app.route('/')
@auth.login_required
def index():
    user = auth.current_user()

    user_db = Profile.query.filter(Profile.username == user)

    user_list = False
    try:
        user_list = user_db.all()[0]
    except IndexError:
        pass

    if user_list:
        message_info = f"Usuário {user}, acessou o index."
        response = {"success": message_info}
        log.info(message_info)

        return jsonify(response)
    return jsonify({"error": "Usuário não encontrado."}), 404

