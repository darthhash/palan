from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home(): 
    gallery_images = [
        {"filename": "1.jpg", "alt": "Утро на берегу Суры", "caption": "Прекрасное утро"},
        {"filename": "2.jpg", "alt": "Дождь в Палане", "caption": "Дождливый день"},
        {"filename": "3.jpg", "alt": "Вид на поля", "caption": "Русские просторы"},
        {"filename": "4.jpg", "alt": "Домик в кемпинге", "caption": "Уютное убежище"},
        {"filename": "7.jpg", "alt": "Рыбалка на Суре", "caption": "Улов на рассвете"}
    ]
    return render_template("index.html", images=gallery_images)

if __name__ == "__main__":
    app.run()
