"""
Представления приложения
"""
from flask import render_template, render_template_string

from models import Example


def home_page_view():
    return render_template('home-page.html')


def show_table_view(row_count: int):
    if row_count < 1:
        return render_template_string('<p class="empty-data">Введите положительное число.</p>')

    members = Example.query.order_by(Example.id.asc()).limit(row_count).all()
    return render_template("show-table.html", members=members)
