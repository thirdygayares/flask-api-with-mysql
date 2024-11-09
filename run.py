from waitress import serve

from app import create_app

app = create_app()

if __name__ == '__main':
    # app.run(debug=True, use_reloader=True)
    serve(app, host='0.0.0.0', port=8080)