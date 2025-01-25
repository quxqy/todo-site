Creating a project
```bash
git clone https://github.com/quxqy/todo-site.git
cd todo-server
python -m venv venv
```
for Windows:
```
  venv\Scripts\activate
```
for macOS/Linux:
```
  source venv/bin/activate
```

Install the dependencies:
```
pip install -r requirements.txt
```
Create the .env file in the root directory and add the following:
```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```
Apply migrations:
```
python manage.py migrate
```
Run the development server:
```
python manage.py runserver
```
