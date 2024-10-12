from werkzeug.security import check_password_hash
from .models import Profile
from . import auth

# Função de validação de autenticação
def validate_authentication(username, password):
    user = Profile.query.filter(Profile.username == username).first()
    if user and user.password == password:
        return True
    return False

# Verificação de senha utilizando o HTTPBasicAuth
@auth.verify_password
def verify_password(username, password):
    user = Profile.query.filter(Profile.username == username).first()
    if user and check_password_hash(user.password, password):
        return username
    return None

