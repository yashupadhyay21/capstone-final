from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)  # Change port to 5001 or another unused port
