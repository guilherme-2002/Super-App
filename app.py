from app import app, db

if __name__ == "__main__":
    # Inicializar o banco de dados
    with app.app_context():
        db.create_all()

    # Executar a aplicação
    app.run(host="0.0.0.0", debug=True, port=8080)