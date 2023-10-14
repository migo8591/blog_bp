from flask import render_template, flash, redirect, url_for
from ..extensions import db
from flask_login import login_required, current_user
from ..model import Users
from . import admin_bp

@admin_bp.route("/admin")
@login_required
def admin():
    id=current_user.id
    usuarios=Users.query.order_by(Users.date_added)
    if id == 1:
        return render_template("admin/admin.html", users=usuarios)
    else:
        flash("Usted no tiene permisos de administrador")
        return redirect(url_for('public.dashboard'))

@admin_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    user_to_delete = Users.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User deleted successfully")
        return redirect(url_for('admin.admin'))
    except:
        flash("Whoop! There was a problem deleting user, try again..")
        return redirect(url_for('admin.admin'))
