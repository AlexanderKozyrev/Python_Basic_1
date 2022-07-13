import functools
from typing import Callable

user_permissions = ['admin']


def check_permission(user_name: str):
    """Декоратор для проверки прав пользователя.
    Возвращает ошибку или право доступа к функции"""

    def check_permission_2(func: Callable):

        @functools.wraps(func)
        def wrapped_check(*args, **kwargs):
            if user_name not in user_permissions:
                raise ValueError("У пользователя недостаточно прав, "
                                 "чтобы выполнить функцию {func}".format(
                    func=func.__name__)
                )
            return wrapped_check

        return check_permission_2


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()