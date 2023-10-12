from iebank_api import app


def add(a, b):
    return a + b

if __name__ == '__main__':
    app.run(debug=True)