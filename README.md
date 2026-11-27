# Aplicación web base — Django + Vite + Docker

Proyecto inicial genérico para la tarea. Incluye autenticación, cuatro roles, Django Admin, plantillas y una interfaz preparada con Vite.

## Requisitos para ejecutarlo localmente
- Docker Desktop instalado y abierto.
- Git instalado (opcional para trabajar con GitHub).
- Node.js y npm solo si deseas ejecutar Vite fuera de Docker.

## Ejecutar con Docker
Desde la carpeta que contiene este README, abre una terminal y ejecuta:

```powershell
docker compose up --build
```

Cuando termine, abre http://localhost:8000

Para crear el usuario administrador, abre otra terminal en la misma carpeta:

```powershell
docker compose exec web python manage.py createsuperuser
```

Sigue las preguntas de la terminal. Luego entra en http://localhost:8000/admin/

Para detener el proyecto:
```powershell
docker compose down
```

## Ejecutar sin Docker (alternativa)
Necesitas Python 3.12 o compatible y Node.js LTS.

Terminal 1 — backend:
```powershell
cd backend
py -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Terminal 2 — construir los archivos de Vite:
```powershell
cd frontend
npm install
npm run build
```

Abre http://127.0.0.1:8000

## Roles incluidos
- Administrador: superusuario de Django; puede entrar a `/admin/` y administrar cuentas.
- Gestor: accede al panel de gestión básico.
- Usuario: accede al panel de usuario.
- Visitante: puede consultar la página pública sin iniciar sesión.

Los nuevos registros reciben el rol `Usuario`. El administrador puede cambiar el rol desde Django Admin.

## Estructura
- `backend/`: proyecto Django, autenticación, modelos, vistas y plantillas.
- `frontend/`: proyecto Vite (JavaScript y CSS).
- `docker-compose.yml`: servicio para ejecutar el proyecto en Docker.

## Importante
Esta es una base técnica genérica porque las instrucciones compartidas no especifican la temática de la aplicación. Antes de añadir módulos de negocio (por ejemplo, inventario, cursos o citas), hay que confirmar qué aplicación se desea construir y qué exige el profesor.
