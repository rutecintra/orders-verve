#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for MySQL to be ready..."
    
    while ! mysqladmin ping -h"$DB_HOST" -u"${DB_USER}" -p"${DB_PASSWORD}" --silent; do
      sleep 2
    done

    echo "MySQL is available!"
fi

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"