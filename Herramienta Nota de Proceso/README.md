# Nota de Proceso (Flask)

## Ejecutar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abrir: http://127.0.0.1:5000

## Deploy en Railway (recomendado)

1. Sube esta carpeta a un repositorio en **GitHub**.
2. En [railway.app](https://railway.app), crea un nuevo proyecto → **Deploy from GitHub repo**.
3. Conecta el repositorio.
4. Agrega un plugin **PostgreSQL** al proyecto (clic en **+ New** → **Database** → **PostgreSQL**).
   - `DATABASE_URL` se configura automáticamente.
5. En la pestaña **Variables** del servicio web, agrega:

| Variable | Valor |
|---|---|
| `SECRET_KEY` | Clave secreta Flask (generar una segura) |
| `GOOGLE_CLIENT_ID` | OAuth Client ID de Google |
| `GOOGLE_CLIENT_SECRET` | OAuth Client Secret de Google |
| `ADMIN_EMAIL` | Correo Google del administrador |
| `ADMIN_NAME` | Nombre del administrador (opcional) |
| `COLLAB_EMAIL` | Correo(s) de colaboradores (separados por coma) |
| `COLLAB_NAME` | Nombre(s) de colaboradores (opcional) |

6. Deploy automático. Railway genera una URL pública (`*.up.railway.app`).

> **Nota:** En Google Cloud Console, agrega la URL de Railway como redirect URI autorizado en tu OAuth Client:
> `https://TU-APP.up.railway.app/auth/google/callback`

## Uso en iPad

- Una vez desplegada, abre la URL pública en Safari.
- Puedes agregarla a pantalla de inicio para uso más cómodo.

## Nota importante sobre datos

- Si existe `DATABASE_URL`, la app guarda estado en PostgreSQL (tabla `user_state` por usuario).
- Si no existe `DATABASE_URL`, usa `data.json` local como respaldo.
- Recomendado: usar **Exportar JSON** regularmente como backup adicional.

### Migración segura (usuarios)

- Al iniciar con la nueva versión, se crean tablas `app_users` y `user_state`.
- El contenido histórico de `app_state` se copia automáticamente al usuario `ADMIN_EMAIL` la primera vez.
- No se elimina `app_state`, por lo que los datos previos no se pierden.

## Incluye

- Cursos, estudiantes, periodos y clases
- Marcas C/I/S por clase
- Cálculo de nota 1.0 a 7.0 con exigencia configurable
- PDF individual y grupal desde backend Python
- Importar Excel (primera columna = nombre estudiante)
- Exportar/Importar JSON
