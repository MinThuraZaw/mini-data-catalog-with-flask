from flask import Blueprint, render_template, request, redirect, url_for

settings_bp = Blueprint('settings', __name__)


@settings_bp.route('/settings')
def settings():
    return render_template('settings.html')


@settings_bp.route('/save_settings', methods=['POST'])
def save_settings():
    # Handle settings saving logic here
    setting1 = request.form['setting1']
    setting2 = request.form['setting2']
    # Save settings logic
    return redirect(url_for('settings.settings'))