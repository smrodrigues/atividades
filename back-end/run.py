from routes import app
#pegando as rotas da aplicação e iniciando o servidor
if __name__ == "__main__":
    app.run(port=5000, debug=True)