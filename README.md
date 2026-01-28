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
# 🚀 VendeCon — Landing Page de Conversión

Una plantilla profesional de landing page diseñada para **convertir visitas en clientes**. Clara, rápida, responsive y lista para personalizar.

## ✨ Características

- 🎨 **Diseño moderno** — Degradados, glassmorphism y animaciones suaves
- 📱 **100% Responsive** — Se adapta automáticamente a móvil, tablet y desktop
- ⚡ **Sin dependencias frontend** — HTML5 puro + CSS + JavaScript vanilla
- 🎯 **Optimizada para conversión** — Hero claro, CTA intencionales, prueba social
- 🔧 **Fácil de editar** — Estructura simple, comentarios "EDITA AQUÍ"
- 🌙 **Dark theme profesional** — Colores degradados (púrpura → verde)

## 📂 Estructura del Proyecto

```
friendly-fiesta/
├── index.html              # Landing page completa (HTML + JS)
├── css/
│   └── style.css          # Estilos (separados, reutilizable)
├── server.py              # Servidor Flask (opcional)
├── requirements.txt       # Dependencias Python
├── README.md              # Este archivo
└── .vscode/
    └── extensions.json    # Configuración VS Code recomendada
```

## 🚀 Cómo Usar

### Opción 1: Live Server (Recomendado - Sin Python)

1. Abre la carpeta en **VS Code**
2. Instala la extensión **Live Server** (ritwickdey.LiveServer)
3. Haz clic derecho en `index.html` → **"Open with Live Server"**
4. Se abrirá en http://localhost:5500

**Ventaja:** Recarga automática al guardar cambios.

### Opción 2: Servidor HTTP de Python (Sin dependencias)

```bash
cd "ruta/del/proyecto"
python -m http.server 5500
```

Luego abre http://127.0.0.1:5500

### Opción 3: Servidor Flask (Con dependencias)

```bash
cd "ruta/del/proyecto"
pip install -r requirements.txt
python server.py
```

Luego abre http://127.0.0.1:5500

## ✏️ Personalización

### Cambiar el nombre de la marca
Busca `VendeCon` en `index.html` y reemplázalo por tu marca.

### Cambiar precios
En la sección `<!-- PRICING -->` del `index.html`, edita los valores:

```html
<span data-price="starter">19</span>  <!-- Cambiar 19 -->
```

Y en el bloque `pricing` del `<script>`:

```javascript
const pricing = {
  monthly: { starter: 19, pro: 39, team: 79, per: 'mes' },
  yearly:  { starter: 15, pro: 31, team: 63, per: 'mes (fact. anual)' }
};
```

### Conectar WhatsApp
En la sección **"EDITA AQUÍ"** del formulario, reemplaza el número:

```html
<a href="https://wa.me/TU_NUMERO?text=Hola%20quiero%20más%20info">
  Abrir WhatsApp
</a>
```

### Conectar el formulario
El formulario es demo. Para enviar datos reales, integra:

- **Formspree** — Copia `action="https://formspree.io/f/TU_ID"`
- **Backend propio** — Reemplaza el event listener en el `<script>`
- **Google Forms** — Incrusta un iframe

## 📋 Secciones Incluidas

✅ **Header** — Navegación sticky con menú móvil
✅ **Hero** — Propuesta de valor + CTA principal
✅ **Beneficios** — 3 razones clave por las que comprar
✅ **Características** — Qué incluye la oferta
✅ **Testimonios** — Prueba social (5 estrellas)
✅ **Precios** — Toggle mensual/anual con 3 planes
✅ **FAQ** — Preguntas frecuentes (colapsables)
✅ **Contacto** — Formulario + CTA WhatsApp
✅ **Footer** — Links y copyright

## 🎨 Personalización CSS

Edita las variables en `css/style.css`:

```css
:root {
  --bg: #0b1020;           /* Fondo oscuro */
  --brand: #7c5cff;        /* Color principal (púrpura) */
  --brand2: #2ee59d;       /* Color secundario (verde) */
  --text: rgba(255,255,255,.92);  /* Texto principal */
  --muted: rgba(255,255,255,.70); /* Texto secundario */
}
```

## 🔗 Deployment

### Netlify / Vercel (Gratis)

1. Sube el proyecto a GitHub
2. Conecta con Netlify o Vercel
3. Deploy automático en cada push

### Tu servidor / Hosting

1. Descarga los archivos
2. Sube `index.html`, `css/` a tu hosting
3. El formulario necesitará backend o un servicio como Formspree

## 📞 Soporte

- Los botones CTA llevan a secciones internas (#beneficios, #precios, etc.)
- El menú móvil se activa automáticamente en pantallas < 920px
- Toggle de precios funciona en tiempo real
- Validación básica del formulario (nombre, email, mensaje)

## 📝 Notas

- **Sin frameworks** — Funciona en navegadores modernos (últimos 2 años)
- **Accesible** — Etiquetas semánticas, ARIA, contrast ratios apropiados
- **Optimizada** — CSS crítico inline, carga rápida
- **Editable** — Busca `EDITA AQUÍ` para puntos principales

## 📄 Licencia

Libre para usar y modificar. ¡Éxito vendiendo! 🚀
