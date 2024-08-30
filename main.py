from web import create_app

app = create_app()

# only runs web server if this file is run
if __name__ == '__main__':
    app.run(debug=True)