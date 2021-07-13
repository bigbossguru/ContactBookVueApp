# VueApp
Django REST and Vue JS application

## Use Python 3.8.10

## Manual step by step
### Backend
- install and activate environment
```
python -m venv venv
```
```
source venv/Script/activate
```
- install python packages
```
pip install -r requirements.txt
```
- move to backend directory
```
cd backend
```
- migrate database
```
python manage.py migrate
```
- create super user
```
python manage.py createsuperuser
```
```
username: "admin"
password: "admin"
```
- run server
```
python manage.py runserver
```

### Frontend
- move to frontend directory
```
cd frontend/vueapp/
```
- install nodejs packages
```
npm install
```
- run server
```
npm run serve
```