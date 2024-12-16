from datetime import date

from flask import flash
from flask.ctx import RequestContext

from controller.IAuthController import IAuthController
from model.data_entities.permission import Permission
from model.data_entities.user import User
from model.services.auth.AuthService import AuthService


class AuthController(IAuthController):
    def __init__(self):
        self.auth_service = AuthService()

    def profileGet(self, email: str) -> User:
        return self.auth_service.authRepository.getUserByEmail(email)

    def register(self, email: str, password: str) -> bool:
        try:
            user = User(name="null", id="null", email=email, password=password, birthDate=date(2000, 1, 1), activityPermission=Permission.editor, componentPermission=Permission.editor)  # Предполагаем, что User имеет эти параметры
            success = self.auth_service.register(user)
            if success:
                flash("Registration successful!", "success")
                return True
            else:
                flash("Error during registration. Try again.", "error")
                return False
        except Exception as e:
            flash(f"Error: {str(e)}", "error")
            return False

    def login(self, email: str, password: str) -> bool:
        try:
            success = self.auth_service.login(email=email, password=password)
            if success:
                flash("Login successful!", "success")
                return True
            else:
                flash("Error during login. Try again.", "error")
                return False
        except Exception as e:
            flash(f"Error: {str(e)}", "error")
            return False


    def updateUser(self, email: str, password: str, email_new: str, password_new: str):
        success = self.auth_service.login(email, password)

        if success:
            print("success login")
            user = self.auth_service.authRepository.getUserByEmail(email)
            if email_new:
                user.email = email_new
                print("new email set")

            if password_new:
                user.password = password_new
                print("new password set")

            self.auth_service.updateUser(user)
        else:
            print("not success login")
            raise ValueError(f"Incorrect data.")

    def deleteUser(self, context: RequestContext, user: User):
        pass

    def validateEmail(self, context: RequestContext, email: str) -> bool:
        return "@" in email and "." in email

    def validatePassword(self, context: RequestContext, password: str) -> bool:
        return len(password) >= 6