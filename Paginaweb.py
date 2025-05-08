from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>EcoWeb</title>
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
                text-decoration: underline;
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
            .buttons {x;
                flex-directi
                display: fleon: column;
                gap: 10px;
                margin-top: 20px;
            }
            .button {
                padding: 10px 15px;
                font-size: 16px;
                border: none;
                background-color: #38a169;
                color: white;
                border-radius: 6px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #2f855a;
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
   <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medio Ambiente</title>
    <style>
        body {
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 1rem 2rem;
                background: linear-gradient(90deg, #4CAF50, #2E7D32);
                color: white;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                position: sticky;
                top: 0;
                z-index: 1000;
            }
            .navbar-logo {
                font-size: 1.8rem;
                font-weight: bold;
                letter-spacing: 1px;
            }
            .navbar-links a {
                color: white;
                text-decoration: none;
                margin-left: 1.5rem;
                font-size: 1rem;
                padding: 0.5rem 1rem;
                border-radius: 5px;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }
            .navbar-links a:hover {
                background-color: #388E3C;
                transform: scale(1.05);
            }
            .header a {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                padding: 0.5rem 1rem;
                border-radius: 5px;
                font-size: 1rem;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }
            .header a:hover {
                background-color: #388E3C;
                transform: scale(1.05);
            }
        </style>
</head>
<body>
    <header class="navbar">
        <div class="navbar-logo">🌿 BIENVENIDO</div>
        <nav class="navbar-links">
            <a href="/">Inicio</a>
            <a href="/acciones">Acciones</a>
            <a href="/3r">3R</a>
            <a href="/quiz">Quiz Ambiental</a>
        </nav>
    </header>
</body>
</html>

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
    <h2>🌿 Juntos por un Futuro Verde</h2>
    <p>
        El planeta Tierra es nuestro hogar y protegerlo es una tarea que comienza con pequeños gestos. Cada acción que tomamos tiene un impacto directo en la salud de nuestro entorno.
    </p>
    <p>
        🌱 Separar los residuos, ♻️ reutilizar materiales, 🚶‍♀️ caminar o usar bicicleta en lugar de vehículos motorizados y 🌞 aprovechar la energía solar son maneras sencillas pero poderosas de marcar la diferencia.
    </p>
    <p>
        La conciencia ecológica crece cuando compartimos el mensaje. Educar a nuestras comunidades, apoyar iniciativas verdes y exigir políticas sostenibles son pasos claves hacia un futuro limpio y justo.
    </p>
    <p>
        🌿 Juntos, podemos construir un mundo donde el progreso y la naturaleza vayan de la mano. ¡Haz tu parte hoy!
    </p>
</div>

<style>
.section {
    max-width: 850px;
    margin: 2rem auto;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    color: #2e7d32;
}

.section h2 {
    font-size: 2.2rem;
    margin-bottom: 1.5rem;
    color: #1b5e20;
    font-weight: bold;
}

.section p {
    font-size: 1.15rem;
    margin-bottom: 1.2rem;
    color: #333;
    line-height: 1.6;
}
</style>

                                  
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secciones Ambientales</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f8f5;
            padding: 2rem;
        }

        .buttons {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            max-width: 600px;
            margin: auto;
        }

        .button {
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            padding: 1rem 1.5rem;
            border-radius: 10px;
            text-align: center;
            font-size: 1.1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease, transform 0.3s ease;
        }

        .button:hover {
            background-color: #388E3C;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="buttons">
        <a href="/clasificacion" class="button">🔍 Clasificación Automática de Residuos</a>
        <a href="/reciclaje" class="button">♻️ Reciclaje Inteligente</a>
        <a href="/conciencia" class="button">🌱 Conciencia Ambiental</a>
        <a href="/educacion" class="button">📚 Educación Ambiental</a>
        <a href="/estadisticas" class="button">📊 Estadísticas de Reciclaje</a>
    </div>
</body>
</html>

                           
       

</body>
</html>




<!-- Repite el mismo bloque para cada una de las demás páginas: Reciclaje, Conciencia, Educación, etc. -->


                                  
                                  
 <!-- Imágenes lado a lado -->
<div style="display: flex; justify-content: center; gap: 20px; margin-top: 30px; flex-wrap: wrap;">
    <img src="https://gtaambiental.com/wp-content/uploads/paises-mejor-gestion-residuos-estrategias-gta-ambiental-blog-feat-img-54.jpg" 
         alt="Medio ambiente" 
         style="width: 45%; height: auto; border-radius: 10px;">
         
    <img src="https://www.ecocontenedores.cl/wp-content/uploads/2017/11/recicla_web.jpg" 
         alt="Reciclaje" 
         style="width: 45%; height: auto; border-radius: 10px;">
</div>


<div class="contenido">
    <h2>🌍 Cuidemos Nuestro Planeta</h2>
    <p>
        La protección del medio ambiente es una responsabilidad de todos. Cada acción cuenta: reciclar, reducir el consumo y educar sobre sostenibilidad ayudan a preservar los recursos naturales para futuras generaciones.
    </p>
    <div class="video-container">
        <iframe 
            src="https://www.youtube.com/embed/Gpc1s9qSeVM" 
            title="Cómo Cuidar el Medio Ambiente" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
    </div>
</div>

<style>
    .footer {
        text-align: center;
        padding: 1rem;
        background-color: #2E7D32;
        color: white;
        font-size: 0.9rem;
    }

    .contenido {
        max-width: 700px;
        margin: 3rem auto;
        text-align: center;
        color: #2E7D32;
    }

    .contenido h2 {
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }

    .contenido p {
        font-size: 1.1rem;
        margin-bottom: 2rem;
        color: #333;
    }

    .video-container {
        position: relative;
        padding-bottom: 56.25%;
        height: 0;
        overflow: hidden;
        max-width: 100%;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    .video-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
</style>

  <footer class="footer">
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
            .header a {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                padding: 0.7rem 1.5rem;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: bold;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
            }
            .header a:hover {
                background-color: #388E3C;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
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
        <a href="/">Volver al INICIO</a>
    </div>

    <div class="content">
        <h2>¿Cómo Funciona?</h2>
        <p>La clasificación automática de residuos es un proceso mediante el cual los residuos se separan eficientemente mediante el uso de tecnología avanzada. Sensores y algoritmos de inteligencia artificial permiten identificar y clasificar materiales como plásticos, metales, vidrio y papel, facilitando su reciclaje y reduciendo la contaminación. Este tambien cuenta con varios beneficios como lo puede ser una mayor eficiencia, reducción de errores, menor coste y mayor sostenibilidad.</p>
        <img src="https://media.istockphoto.com/id/1191750758/es/foto/basura-de-clasificaci%C3%B3n-rob%C3%B3tica-de-brazos-clasificaci%C3%B3n-autom%C3%A1tica-de-basura-renderizado-3d.jpg?s=170667a&w=0&k=20&c=dYs9O6rez0ZEbYUKpnpKm1YKrPBtacWL86qw3sOj4wI=" alt="Clasificación de residuos" style="width: 100%; height: auto; border-radius: 10px;">
    </div>

    <footer class="footer">
        © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </footer>

    </body>
    </html>
    """)

@app.route("/reciclaje")
def reciclaje():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reciclaje Inteligente</title>
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
            .header a {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                padding: 0.7rem 1.5rem;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: bold;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
            }
            .header a:hover {
                background-color: #388E3C;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
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
        <h1>Reciclaje Inteligente</h1>
        <a href="/">Volver al INICIO</a>
    </div>

    <div class="content">
        <h2>¿Qué es el Reciclaje Inteligente?</h2>
        <p>El reciclaje inteligente implica el uso de tecnologías avanzadas para mejorar la eficiencia del proceso de reciclaje. Esto incluye sensores, sistemas automatizados y análisis de datos para mejorar la separación de materiales reciclables, reduciendo los costos y aumentando la efectividad del proceso.</p>
        <img src="https://contelogic.com/wp-content/uploads/2024/07/contenedores-innovadores.jpg" alt="Reciclaje Inteligente" style="width: 100%; height: auto; border-radius: 10px;">
    </div>

    <footer class="footer">
        © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </footer>

    </body>
    </html>
    """)

@app.route("/conciencia")
def conciencia():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Conciencia Ambiental</title>
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
            .header a {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                padding: 0.7rem 1.5rem;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: bold;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
            }
            .header a:hover {
                background-color: #388E3C;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
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
        <h1>Conciencia Ambiental</h1>
        <a href="/">Volver al INICIO</a>
    </div>

    <div class="content">
        <h2>¿Por qué es importante la conciencia ambiental?</h2>
        <p>La conciencia ambiental es fundamental para promover prácticas sostenibles y reducir el impacto negativo que nuestras acciones tienen en el planeta. Se trata de educar a las personas sobre la importancia de conservar los recursos naturales y proteger los ecosistemas que hacen posible la vida en la Tierra.</p>
        <img src="https://peruvienblog.wordpress.com/wp-content/uploads/2016/05/dia_del_medio_ambiente-ok.jpg" alt="Conciencia ambiental" style="width: 100%; height: auto; border-radius: 10px;">
    </div>

    <footer class="footer">
        © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </footer>

    </body>
    </html>
    """)

@app.route("/educacion")
def educacion():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Educación Ambiental</title>
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
            .header a {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                padding: 0.7rem 1.5rem;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: bold;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
            }
            .header a:hover {
                background-color: #388E3C;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
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
        <h1>Educación Ambiental</h1>
        <a href="/">Volver al INICIO</a>
    </div>

    <div class="content">
        <h2>La importancia de la educación ambiental</h2>
        <p>La educación ambiental es esencial para sensibilizar a las personas sobre el impacto de sus acciones en el medio ambiente. Además, fomenta el desarrollo de hábitos sostenibles y promueve un cambio de actitud hacia el respeto y conservación de la naturaleza.</p>
        <img src="https://educacion.mma.gob.cl/wp-content/uploads/2019/06/arbol-600x334.jpg" alt="Educación Ambiental" style="width: 100%; height: auto; border-radius: 10px;">
    </div>

    <footer class="footer">
        © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </footer>

    </body>
    </html>
    """)

@app.route("/estadisticas")
def estadisticas():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Estadísticas de Reciclaje</title>
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
            .header a {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                padding: 0.7rem 1.5rem;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: bold;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
            }
            .header a:hover {
                background-color: #388E3C;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
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
        <h1>Estadísticas de Reciclaje</h1>
        <a href="/"">Volver al INICIO</a>
    </div>

    <div class="content">
        <h2>Datos importantes sobre reciclaje</h2>
        <p>El reciclaje es crucial para reducir la cantidad de residuos en los vertederos y disminuir el impacto ambiental. A nivel mundial, cada vez más países implementan políticas de reciclaje que contribuyen a la reducción de la huella ecológica.</p>
        <img src="https://www.rts.com/wp-content/uploads/2020/10/facts-recycling-scaled.jpg" alt="Estadísticas de Reciclaje" style="width: 100%; height: auto; border-radius: 10px;">
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
            .header a {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                padding: 0.7rem 1.5rem;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: bold;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
            }
            .header a:hover {
                background-color: #388E3C;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
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
        <a href="/">Volver al INICIO</a>
    </div>

    <div class="content">
        <h2>¿Qué podemos hacer por el planeta?</h2>
        <ul style="font-size: 18px; color: #2f855a; line-height: 1.8;">
            <li>Reducir el uso de plásticos de un solo uso.</li>
            <li>Separar los residuos correctamente para facilitar el reciclaje.</li>
            <li>Ahorrar agua y electricidad.</li>
            <li>Utilizar transporte sostenible (caminar, bici, transporte público).</li>
            <li>Plantar árboles y cuidar los espacios verdes.</li>
            <li>Comprar productos locales y ecológicos.</li>
            <li>Evitar el desperdicio de alimentos.</li>
            <li>Promover la educación ambiental.</li>
            <li>Reutilizar objetos antes de desecharlos.</li>
            <li>Participar en limpiezas comunitarias.</li>
        </ul>
                                  
   <!-- Imágenes lado a lado -->
<div style="display: flex; justify-content: center; gap: 20px; margin-top: 30px; flex-wrap: wrap;">
    <img src="https://factorenergetico.mx/wp-content/uploads/2024/06/medio-ambiente.jpeg" 
         alt="Medio ambiente" 
         style="width: 45%; height: auto; border-radius: 10px;">
         
    <img src="https://cdn0.ecologiaverde.com/es/posts/9/8/7/como_cuidar_el_medio_ambiente_3789_orig.jpg" 
         alt="Reciclaje" 
         style="width: 45%; height: auto; border-radius: 10px;">
</div>

 <div class="contenido">
    <h2>🌿 ¿Qué podemos hacer por nuestro planeta?</h2>
    <p>
        Cada pequeña acción cuenta: reciclar, ahorrar energía, reducir el uso de plásticos y educar a otros sobre la importancia de cuidar nuestro entorno. ¡Juntos podemos marcar la diferencia!
    </p>
    <div class="video-container">
        <iframe 
            src="https://www.youtube.com/embed/BTLyw18HjXk" 
            title="10 acciones para salvar al planeta" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
    </div>
</div>

<style>
    .footer {
        text-align: center;
        padding: 1rem;
        background-color: #2E7D32;
        color: white;
        font-size: 0.9rem;
    }

    .contenido {
        max-width: 700px;
        margin: 3rem auto;
        text-align: center;
        color: #2E7D32;
    }

    .contenido h2 {
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }

    .contenido p {
        font-size: 1.1rem;
        margin-bottom: 2rem;
        color: #333;
    }

    .video-container {
        position: relative;
        padding-bottom: 56.25%;
        height: 0;
        overflow: hidden;
        max-width: 100%;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    .video-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
</style>
                                  
     <footer class="footer">
        © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </footer>
    </body>
    </html>
    """)

@app.route("/3r")
def tres_R():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>3R: Reducir, Reutilizar, Reciclar</title>
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
            .header a {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                padding: 0.7rem 1.5rem;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: bold;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
            }
            .header a:hover {
                background-color: #388E3C;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
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
        <h1>3R: Reducir, Reutilizar, Reciclar</h1>
        <a href="/">Volver al INICIO</a>
    </div>
    <div class="content">
        <h2>Como EcoWeb, promovemos las 3R</h2>
        <p>En EcoWeb, creemos que cada acción cuenta. Al adoptar las 3R en nuestra vida diaria, contribuimos a la conservación del medio ambiente y fomentamos un futuro más sostenible.</p>
        <h2>¿Qué son las 3R?</h2>
        <p>Las 3R son principios fundamentales para la gestión de residuos y la sostenibilidad ambiental. Reducir implica disminuir la cantidad de residuos que generamos; reutilizar significa dar un nuevo uso a los objetos en lugar de desecharlos; y reciclar consiste en procesar materiales usados para convertirlos en nuevos productos.</p>
        
        <h2>Beneficios de las 3R</h2>
        <ul>
            <li>Reducen la cantidad de residuos en vertederos.</li>
            <li>Disminuyen la contaminación ambiental.</li>
            <li>Conservan recursos naturales.</li>
            <li>Fomentan la economía circular.</li>
            <li>Generan conciencia sobre el consumo responsable.</li>
        </ul>
        <p>Implementar las 3R en nuestra vida diaria ayuda a conservar recursos naturales, reducir la contaminación y fomentar una economía circular.</p>
        <img src="https://renovables.blog/wp-content/uploads/2023/06/las-3r-del-reciclaje-reduce-reutiliza-y-recicla-para-cuidar-el-planeta.jpg" alt="Conciencia ambiental" style="width: 100%; height: auto; border-radius: 10px;">
    </div>
    <footer class="footer">
        © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </footer>
    </body>
    </html>
                                  """)

@app.route("/quiz")
def quiz():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Quiz Ambiental</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #9ef88d;
            }
            
            .quiz-container {
                max-width: 600px;
                margin: 2rem auto;
                padding: 1rem;
                background: white;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .quiz-container h1 {
                text-align: center;
                color: #2e7d32;
            }
            .question {
                margin-bottom: 1rem;
                font-size: 1.2rem;
                color: #333;
            }
            .options {
                list-style: none;
                padding: 0;
            }
            .options li {
                margin-bottom: 0.5rem;
            }
            .options button {
                width: 100%;
                padding: 0.5rem;
                font-size: 1rem;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .options button:hover {
                background-color: #388E3C;
            }
            .result {
                text-align: center;
                margin-top: 1rem;
                font-size: 1.2rem;
                color: #2e7d32;
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
        <div class="quiz-container">
    <h1>Quiz Ambiental</h1>    
    <div id="quiz">
        <!-- Aquí saldrán las preguntas dinámicamente -->
    </div>
    <div id="result" class="result"></div>
                                  
       <div style="text-align: center; margin-top: 20px;">
        <a href="/" class="back-button">⬅️ Volver al INICIO</a>
    </div>
                                  
    <style>
    .back-button {
        display: inline-block;
        background-color: #4CAF50;
        color: white;
        text-decoration: none;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
    }

    .back-button:hover {
        background-color: #388E3C;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
    }
</style>
                                  
</div>
        <script>
            const questions = [
                {
                    question: "¿Cuál de las siguientes acciones ayuda a reducir la contaminación?",
                    options: ["Reciclar materiales", "Usar plásticos de un solo uso", "Dejar las luces encendidas", "Tirar basura en la calle"],
                    correct: 0
                },
                {
                    question: "¿Qué significa la primera R en las 3R?",
                    options: ["Reutilizar", "Reciclar", "Reducir", "Reparar"],
                    correct: 2
                },
                {
                    question: "¿Qué recurso natural es renovable?",
                    options: ["Petróleo", "Agua", "Carbón", "Gas natural"],
                    correct: 1
                },
                {
                    question: "¿Qué es el cambio climático?",
                    options: ["Un cambio temporal en el clima", "Un cambio a largo plazo en los patrones climáticos", "Un fenómeno natural sin intervención humana", "Un mito"],
                    correct: 1
                },
                {
                    question: "¿Qué gas contribuye más al efecto invernadero?",
                    options: ["Oxígeno", "Dióxido de carbono", "Nitrógeno", "Helio"],
                    correct: 1
                },
                {
                    question: "¿Qué es la biodiversidad?",
                    options: ["La variedad de especies en un ecosistema", "La cantidad de oxígeno en el aire", "El número de árboles en un bosque", "La cantidad de agua en un río"],
                    correct: 0
                },
                {
                    question: "¿Qué es la energía renovable?",
                    options: ["Energía que se agota rápidamente", "Energía que proviene de recursos naturales inagotables", "Energía generada por combustibles fósiles", "Energía nuclear"],
                    correct: 1
                },
                {
                    question: "¿Qué acción reduce el desperdicio de agua?",
                    options: ["Dejar el grifo abierto", "Reparar fugas", "Lavar el coche todos los días", "Regar el jardín al mediodía"],
                    correct: 1
                },
                {
                    question: "¿Qué es el reciclaje?",
                    options: ["Quemar residuos", "Reutilizar materiales para crear nuevos productos", "Enterrar residuos en vertederos", "Desechar residuos en el océano"],
                    correct: 1
                },
                {
                    question: "¿Qué podemos hacer para proteger los océanos?",
                    options: ["Tirar basura en las playas", "Reducir el uso de plásticos", "Pescar en exceso", "Usar productos químicos en el agua"],
                    correct: 1
                }
            ];

            let currentQuestion = 0;
            let correctAnswers = 0;

            function loadQuestion() {
                const quiz = document.getElementById("quiz");
                const question = questions[currentQuestion];
                quiz.innerHTML = `
                    <div class="question">${question.question}</div>
                    <ul class="options">
                        ${question.options.map((option, index) => `
                            <li><button onclick="checkAnswer(this, ${index === question.correct})">${option}</button></li>
                        `).join("")}
                    </ul>
                `;
            }

            function checkAnswer(button, isCorrect) {
                const result = document.getElementById("result");
                if (isCorrect) {
                    result.textContent = "¡Correcto!";
                    result.style.color = "green";
                    correctAnswers++;
                } else {
                    result.textContent = "Incorrecto.";
                    result.style.color = "red";
                }
                const buttons = document.querySelectorAll(".options button");
                buttons.forEach(btn => btn.disabled = true);

                setTimeout(() => {
                    currentQuestion++;
                    if (currentQuestion < questions.length) {
                        loadQuestion();
                        result.textContent = "";
                    } else {
                        result.textContent = `¡Has completado el quiz! Respuestas correctas: ${correctAnswers} de ${questions.length}`;
                    }
                }, 2000);
            }

            loadQuestion();
        </script>
        <footer class="footer">
            © 2025 Proyecto Medioambiental. Todos los derechos reservados.
    </body>
    </html>
    """)
 

if __name__ == "__main__":
    app.run(debug=True)
 