from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Inicio</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .header {
                position: fixed;
                top: 0;
                right: 0;
                background-color: #38a169;
                color: white;
                padding: 10px 20px;
                text-align: center;
                border-radius: 0 0 0 10px;
                font-size: 14px;
                z-index: 1000;
            }
            .header a {
                color: white;
                text-decoration: none;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 8px;
                background-color: #2f855a;
                transition: background-color 0.3s ease;
            }
            .header a:hover {
                background-color: #276749;
            }
            .main-content {
                margin-top: 80px;
                min-height: 100vh;
                background: linear-gradient(to bottom, #f0fff4, #d4f1c5);
            }
            .hero {
                position: relative;
                height: 70vh;
                overflow: hidden;
            }
            .hero img {
                position: absolute;
                inset: 0;
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
            .hero-overlay {
                position: absolute;
                inset: 0;
                background: rgba(0, 0, 0, 0.5);
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                color: white;
            }
            .hero-overlay h1 {
                font-size: 6rem;
                font-weight: bold;
            }
            .hero-overlay p {
                font-size: 2rem;
            }
            .hero-overlay span {
                font-size: 4rem;
                margin-top: 1.5rem;
            }
            .section {
                max-width: 1200px;
                margin: auto;
                padding: 16px;
            }
            .section h2 {
                font-size: 24px;
                font-weight: bold;
                color: #2f855a;
                margin-bottom: 16px;
            }
            .section p {
                font-size: 16px;
                color: #2f855a;
                line-height: 1.6;
            }
            .buttons {
                display: flex;
                flex-direction: column;
                gap: 10px;
                margin-top: 20px;
            }
            .button {
                padding: 12px 20px;
                font-size: 18px;
                border: none;
                background-color: #2f855a;
                color: white;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .button:hover {
                background-color: #276749;
            }
            footer {
                background-color: #2f855a;
                color: white;
                text-align: center;
                padding: 16px;
                font-family: 'Trebuchet MS', sans-serif;
            }
        </style>
    </head>
    <body>

    <div class="header">
        <h2>BIENVENIDO</h2>
        <a href="/acciones">Ir a ACCIONES</a>
    </div>

    <div class="main-content">
        <div class="hero">
            <img src="https://images.unsplash.com/photo-1472214103451-9374bd1c798e?auto=format&fit=crop&q=80&w=2000.jpg" alt="Paisaje natural">
            <div class="hero-overlay">
                <div>
                    <h1>Cuidemos Nuestro Planeta</h1>
                    <p>CUIDEMOS DEL MEDIO AMBIENTE</p>
                    <span>🌍</span>
                </div>
            </div>
        </div>
        <div class="section">
            <h2>Acciones para Mejorar el Reciclaje</h2>
            <p>La protección del medio ambiente no solo es una cuestión de responsabilidad hacia la naturaleza, sino también un acto de justicia intergeneracional...</p>
            <p>La educación ambiental es clave para fomentar una cultura de respeto y cuidado hacia el entorno...</p>
            <p>Además, la colaboración entre gobiernos, empresas y ciudadanos es esencial...</p>     
            <div class="buttons">
                <a href="/clasificacion" class="button">🔍 Clasificación Automática de Residuos</a>
                <a href="/reciclaje" class="button">♻️ Reciclaje Inteligente</a>
                <a href="/conciencia" class="button">🌱 Conciencia Ambiental</a>
                <a href="/educacion" class="button">📚 Educación Ambiental</a>
                <a href="/estadisticas" class="button">📊 Estadísticas de Reciclaje</a>
            </div>
        </div>
    </div>

    <footer>
        © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </footer>

    </body>
    </html>
    """)

@app.route("/clasificacion")
def clasificacion():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Clasificación Automática de Residuos</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0fff4;
                margin: 0;
            }
            .header {
                background-color: #38a169;
                color: white;
                padding: 20px;
                text-align: center;
            }
            .content {
                padding: 20px;
                max-width: 900px;
                margin: auto;
            }
            .footer {
                background-color: #2f855a;
                color: white;
                text-align: center;
                padding: 16px;
                font-family: 'Trebuchet MS', sans-serif;
            }
        </style>
    </head>
    <body>

    <div class="header">
        <h1>Clasificación Automática de Residuos</h1>
        <a href="/" class="button">Volver al INICIO</a>
    </div>

    <div class="content">
        <h2>¿Cómo Funciona?</h2>
        <p>La clasificación automática de residuos es un proceso mediante el cual los residuos se separan eficientemente mediante el uso de tecnología avanzada...</p>
    </div>

    <footer class="footer">
        © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </footer>

    </body>
    </html>
    """)

@app.route("/acciones")
def acciones():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Acciones</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0fff4;
                margin: 0;
            }
            .header {
                background-color: #38a169;
                color: white;
                padding: 20px;
                text-align: center;
            }
            .content {
                padding: 20px;
                max-width: 900px;
                margin: auto;
            }
            .footer {
                background-color: #2f855a;
                color: white;
                text-align: center;
                padding: 16px;
                font-family: 'Trebuchet MS', sans-serif;
            }
        </style>
    </head>
    <body>

    <div class="header">
        <h1>ACCIONES</h1>
        <a href="/" class="button">Volver al INICIO</a>
    </div>

    <div class="content">
        <h2>¿Qué podemos hacer por el planeta?</h2>
        <ul>
            <li>Reducir el uso de plásticos de un solo uso.</li>
            <li>Separar los residuos correctamente para facilitar el reciclaje.</li>
            <li>Ahorrar agua y electricidad.</li>
        </ul>
    </div>

    <footer class="footer">
        © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </footer>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
