# your_app/templatetags/user_filters.py

from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter(name='addclass')
def addclass(field, css_class):
    """
    Добавляет CSS класс к полю формы.
    Используется в вашем шаблоне: {{ field|addclass:'form-control' }}
    
    Пример: поле input получает класс 'form-control'
    """
    return field.as_widget(attrs={'class': css_class})


@register.filter(name='add_placeholder')
def add_placeholder(field, placeholder_text):
    """
    Добавляет placeholder к полю формы.
    
    Использование: {{ field|add_placeholder:'Введите username' }}
    """
    return field.as_widget(attrs={'placeholder': placeholder_text})


@register.filter(name='add_attrs')
def add_attrs(field, attrs_string):
    """
    Добавляет произвольные атрибуты к полю формы.
    
    Использование: {{ field|add_attrs:'data-toggle:tooltip,title:Подсказка' }}
    """
    attrs = {}
    for attr in attrs_string.split(','):
        if ':' in attr:
            key, value = attr.split(':', 1)
            attrs[key.strip()] = value.strip()
    return field.as_widget(attrs=attrs)


@register.filter(name='field_type')
def field_type(field):
    """
    Возвращает тип поля формы (text, password, email и т.д.).
    
    Использование: {{ field|field_type }}
    """
    return field.field.widget.__class__.__name__.lower()


@register.filter(name='is_checkbox')
def is_checkbox(field):
    """
    Проверяет, является ли поле чекбоксом.
    
    Использование: {% if field|is_checkbox %}...{% endif %}
    """
    return field.field.widget.__class__.__name__ == 'CheckboxInput'


# user_filters.py

@register.filter(name='error_class')
def error_class(field, css_class='is-invalid'):
    """
    Добавляет класс ошибки, если поле содержит ошибки.
    
    ВНИМАНИЕ: Этот фильтр должен применяться ТОЛЬКО к объекту поля,
    а не к результату других фильтров!
    
    Использование: {{ field|error_class:'is-invalid' }}
    """
    # Проверяем, что передан именно объект поля, а не строка
    if hasattr(field, 'errors') and field.errors:
        return field.as_widget(attrs={'class': css_class})
    elif hasattr(field, 'field') and hasattr(field.field, 'widget'):
        # Если это bound field
        return field
    else:
        # Если это уже строка, возвращаем как есть
        return field

@register.filter(name='show_errors')
def show_errors(field):
    """
    Отображает ошибки поля в виде HTML списка.
    
    Использование: {{ field|show_errors }}
    """
    if field.errors:
        errors_html = '<div class="invalid-feedback d-block">'
        for error in field.errors:
            errors_html += f'<small>{error}</small><br>'
        errors_html += '</div>'
        return mark_safe(errors_html)
    return ''


@register.filter(name='field_icon')
def field_icon(field):
    """
    Возвращает иконку для поля на основе его типа.
    
    Использование: {{ field|field_icon }}
    """
    field_type_map = {
        'username': '👤',
        'email': '📧',
        'password': '🔒',
        'text': '📝',
        'default': '📄'
    }
    
    field_name = field.name.lower()
    if 'username' in field_name:
        return mark_safe('<i class="bi bi-person"></i>')
    elif 'email' in field_name:
        return mark_safe('<i class="bi bi-envelope"></i>')
    elif 'password' in field_name:
        return mark_safe('<i class="bi bi-lock"></i>')
    return ''


@register.filter(name='toggle_password')
def toggle_password(field):
    """
    Добавляет кнопку для переключения видимости пароля.
    Используется с JavaScript.
    
    Использование: {{ field|toggle_password }}
    """
    if field_type(field) == 'passwordinput':
        html = field.as_widget(attrs={'id': f'{field.name}_input'})
        html += '''
        <button type="button" 
                class="btn btn-outline-secondary toggle-password" 
                data-target="#{0}_input"
                style="position: absolute; right: 10px; top: 0;">
            👁️
        </button>
        '''.format(field.name)
        return mark_safe(html)
    return field


@register.filter(name='auto_label')
def auto_label(field, label_text=None):
    """
    Добавляет красивую метку к полю с возможностью иконки.
    
    Использование: {{ field|auto_label:'Ваше имя' }}
    """
    icon = field_icon(field)
    label = label_text or field.label
    
    if icon:
        label_html = f'{icon} {label}'
    else:
        label_html = label
    
    return mark_safe(f'<label for="{field.id_for_label}">{label_html}</label>')


@register.filter(name='field_group')
def field_group(field, extra_classes=''):
    """
    Создает группу полей с меткой, полем ввода и ошибками.
    
    Использование: {{ field|field_group:'mb-3' }}
    """
    wrapper_class = f'form-group {extra_classes}'
    label = auto_label(field)
    
    # Добавляем класс для ошибок
    error_class = 'is-invalid' if field.errors else ''
    field_html = field.as_widget(attrs={'class': f'form-control {error_class}'})
    
    errors_html = show_errors(field)
    
    html = f'''
    <div class="{wrapper_class}">
        {label}
        {field_html}
        {errors_html}
        {field.help_text if field.help_text else ''}
    </div>
    '''
    return mark_safe(html)


@register.filter(name='format_errors')
def format_errors(form):
    """
    Форматирует все ошибки формы в единый блок.
    
    Использование: {{ form|format_errors }}
    """
    if not form.errors:
        return ''
    
    errors_html = '<div class="alert alert-danger">'
    errors_html += '<strong>Пожалуйста, исправьте следующие ошибки:</strong><ul>'
    
    for field, errors in form.errors.items():
        field_label = form.fields[field].label if field in form.fields else field
        for error in errors:
            errors_html += f'<li>{field_label}: {error}</li>'
    
    errors_html += '</ul></div>'
    return mark_safe(errors_html)


@register.filter(name='success_message')
def success_message(message, dismissible=True):
    """
    Создает сообщение об успехе с Bootstrap стилями.
    
    Использование: {{ 'Вы успешно вошли'|success_message }}
    """
    close_button = ''
    if dismissible:
        close_button = '<button type="button" class="btn-close" data-bs-dismiss="alert"></button>'
    
    html = f'''
    <div class="alert alert-success alert-dismissible fade show" role="alert">
        {close_button}
        {message}
    </div>
    '''
    return mark_safe(html)


@register.filter(name='remember_me_checkbox')
def remember_me_checkbox(field):
    """
    Создает красивый чекбокс "Запомнить меня".
    
    Использование: {{ remember_me_field|remember_me_checkbox }}
    """
    html = f'''
    <div class="form-check">
        {field.as_widget(attrs={'class': 'form-check-input'})}
        <label class="form-check-label" for="{field.id_for_label}">
            {field.label}
        </label>
    </div>
    '''
    return mark_safe(html)


@register.filter(name='csrf_token_meta')
def csrf_token_meta():
    """
    Добавляет CSRF токен в мета-тег для AJAX запросов.
    
    Использование: {{ request|csrf_token_meta }}
    """
    from django.middleware.csrf import get_token
    from django.template.context import RequestContext
    
    if hasattr(request, 'csrf_token'):
        token = request.csrf_token
    else:
        token = get_token(request)
    
    return mark_safe(f'<meta name="csrf-token" content="{token}">')