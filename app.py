from flask import Flask, render_template_string
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Gerar o gráfico
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='x', ylabel='y', title='Gráfico simples')
    ax.grid()

    # Salvar o gráfico em um objeto BytesIO
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    img_str = base64.b64encode(img.getvalue()).decode('utf-8')

    # Renderizar a página HTML com o gráfico
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gráfico Matplotlib</title>
    </head>
    <body>
        <h1>Gráfico gerado com Matplotlib</h1>
        <img src="data:image/png;base64,{{ img_str }}" />
    </body>
    </html>
    '''
    return render_template_string(html, img_str=img_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
