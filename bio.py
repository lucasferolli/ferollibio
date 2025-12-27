from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    # Seus links personalizados
    meus_links = [
        {"nome": "Instagram", "url": "https://www.instagram.com/lucas.ferolli", "icone":"fa-brands fa-instagram"},
        {"nome": "Tiktok", "url": "https://www.tiktok.com/@lucas.ferolli","icone":"fa-brands fa-tiktok"},
        {"nome": "Grupo Whatsapp", "url": "https://chat.whatsapp.com/GpZ52PMFqDKBHMf3ymFHKa?mode=ems_copy_t","icone":"fa-brands fa-whatsapp"},
        {"nome": "Grupo Telegram", "url": "https://t.me/+hHhQ2TJcM2wxOGRh","icone":"fa-brands fa-telegram"},
        {"nome": "Ferramenta Extrair contatos", "url": "https://kiwify.app/MxBFcKN?afid=XcyiCW6I","icone":"fa-solid fa-user-ninja"}
    ]
    return render_template('index.html', links=meus_links)

if __name__ == '__main__':
    app.run(debug=True)