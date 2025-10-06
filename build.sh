set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

if [ "$CREATE_SUPERUSER" = "true" ]; then
    echo "Creating Django superuser..."
    python backend/manage.py createsuperuser
fi
