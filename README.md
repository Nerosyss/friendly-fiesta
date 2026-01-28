<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta name="description" content="Landing page de ventas lista para usar. Convierte visitas en clientes con un diseño limpio y profesional." />
  <title>VendeCon — Landing Page</title>

  <!-- Open Graph (cambia estos datos si la vas a compartir) -->
  <meta property="og:title" content="VendeCon — Aumenta tus ventas" />
  <meta property="og:description" content="Una landing page enfocada en conversión: clara, rápida y responsive." />
  <meta property="og:type" content="website" />

  <style>
    :root{
      --bg: #0b1020;
      --card: rgba(255,255,255,.06);
      --card2: rgba(255,255,255,.10);
      --text: rgba(255,255,255,.92);
      --muted: rgba(255,255,255,.70);
      --muted2: rgba(255,255,255,.55);
      --border: rgba(255,255,255,.14);
      --brand: #7c5cff;
      --brand2:#2ee59d;
      --shadow: 0 20px 60px rgba(0,0,0,.35);
      --radius: 18px;
      --radius2: 26px;
      --max: 1120px;
    }

    *{ box-sizing:border-box; }
    html{ scroll-behavior:smooth; }
    body{
      margin:0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, "Noto Sans", "Helvetica Neue", sans-serif;
      background:
        radial-gradient(1100px 600px at 20% -10%, rgba(124,92,255,.35), transparent 60%),
        radial-gradient(900px 520px at 90% 0%, rgba(46,229,157,.25), transparent 55%),
        radial-gradient(900px 520px at 50% 110%, rgba(124,92,255,.18), transparent 60%),
        var(--bg);
      color: var(--text);
      line-height:1.55;
    }

    a{ color:inherit; text-decoration:none; }
    img{ max-width:100%; display:block; }

    .container{ width:min(var(--max), calc(100% - 40px)); margin:0 auto; }

    /* Top bar */
    header{
      position:sticky; top:0; z-index:10;
      backdrop-filter: blur(14px);
      background: rgba(11,16,32,.55);
      border-bottom: 1px solid rgba(255,255,255,.08);
    }
    # Friendly Fiesta — Proyecto

    He organizado el proyecto para que el HTML, CSS y el servidor Python estén en su lugar.

    Archivos relevantes:

    - `index.html` — HTML principal de la landing.
    - `css/style.css` — estilos extraídos del HTML.
    - `server.py` — servidor Flask para pruebas locales (puerto 5500).
    - `requirements.txt` — dependencias para `server.py`.

    Cómo ejecutar:

    1) Usar Live Server (VS Code): abre la carpeta en VS Code y pulsa "Go Live" o clic derecho en `index.html` → "Open with Live Server".

    2) Servidor HTTP simple con Python (sin dependencias):

    ```bash
    cd "c:\Users\PC GAMER\OneDrive\Escritorio\friendly-fiesta-main\friendly-fiesta"
    python -m http.server 5500
    # luego abre http://127.0.0.1:5500
    ```

    3) Usar el servidor Flask incluido (necesita dependencias):

    ```bash
    cd "c:\Users\PC GAMER\OneDrive\Escritorio\friendly-fiesta-main\friendly-fiesta"
    python -m pip install -r requirements.txt
    python server.py
    # luego abre http://127.0.0.1:5500
    ```

    Notas:
    - Si tu ruta contiene espacios o está en OneDrive y Live Server falla, mueve el proyecto a una carpeta sin espacios (ej. `C:\projects\friendly-fiesta`) y vuelve a intentarlo.
    - El formulario en la landing es demo; conecta un backend real o servicios como Formspree para envío.
