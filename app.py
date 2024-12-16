from datetime import date

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from controller.AuthController import AuthController
from controller.ActivityController import ActivityController
import os

from model.data_entities.exhibition import Exhibition
from model.data_entities.permission import Permission
from model.data_entities.user import User

app = Flask(__name__)
secret_key = os.urandom(24)  # Генерация случайного 24-байтного ключа
app.secret_key = secret_key
auth_controller = AuthController()
activity_controller = ActivityController()

@app.route("/")
def index():
    # Создаем HTML-страницу
    return redirect(url_for("login"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Получаем данные формы (email и password)

        email = request.form["email"]
        password = request.form["password"]

        # Здесь вы можете добавить свою логику регистрации

        success = auth_controller.register(email, password)

        if success:
            return redirect(url_for("login"))
        else:
            return redirect(url_for("signup"))

    # Отображаем страницу регистрации
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Получаем данные формы (email и password)

        email = request.form["email"]
        password = request.form["password"]

        success = auth_controller.login(email, password)

        if success:
            return redirect(url_for("main_window"))
        else:
            return redirect(url_for("login"))

    return render_template("start_page.html")

@app.route("/main", methods=["GET", "POST"])
def main_window():
    return render_template("main.html")

@app.route("/myaccount", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        # Получаем данные из формы
        current_email = request.form.get("current_email")
        current_password = request.form.get("current_password")
        new_email = request.form.get("new_email")
        new_password = request.form.get("new_password")

        try:
            # Обновление пользователя
            auth_controller.updateUser(current_email, current_password, new_email, new_password)
            flash("User data updated successfully.", "error")
        except ValueError as e:
            # Обработка ошибки, если данные некорректны
            flash(str(e), "error")
            return redirect(url_for("account"))

    return render_template("my_account.html")

@app.route("/activities", methods=["GET", "POST"])
def activities():
    if request.method == "POST":

        activity_name = request.form.get("activity-name")
        activity_description = request.form.get("activity-description")
        activity_events = request.form.get("activity-events")

        # Добавляем данные в список (можно использовать базу данных)
        if activity_name and activity_description and activity_events:
            exhibition = Exhibition(id=os.urandom(24).hex(), name=activity_name, theme="", description=activity_description, owner=User(name="", id="", email="", password="", birthDate=date(2000, 1, 1), activityPermission=Permission.editor, componentPermission=Permission.editor), dateTime=date(2000, 1, 1), participants=[], rating=0, reviewIdList=[], expositions=activity_events.split(','))
            activity_controller.createActivity(exhibition)

            if 'activities' not in session:
                session['activities'] = []

            session['activities'].append({
                'name': exhibition.name,
                'description': exhibition.description,
                'events': exhibition.expositions
            })
            flash("Activity added successfully!")
        else:
            flash("Please fill in all fields.")

        return redirect(url_for("activities"))

    activities = session.get('activities', [])
    return render_template("activities.html", activities=activities)

@app.route("/delete_exhibition/<activity_name>", methods=["POST"])
def delete_exhibition(activity_name):
    # Получаем список активностей из сессии
    activities = session.get('activities', [])

    # Находим выставку по имени
    exhibition_to_delete = None
    for activity in activities:
        if activity['name'] == activity_name:
            exhibition_to_delete = activity
            break

    if exhibition_to_delete:
        # Удаляем выставку из списка в сессии
        updated_activities = [a for a in activities if a['name'] != activity_name]
        session['activities'] = updated_activities

        activity_controller.deleteActivity(exhibition_to_delete['name'])   #exhibition_to_delete['name'] -- это возвращает строку, содержащую имя объекта

        flash("Exhibition deleted successfully!", "success")
    else:
        flash("Exhibition not found.", "error")

    return redirect(url_for("activities"))

if __name__ == "__main__":
    app.run(debug=True)