set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
    python backend/manage.py createsuperuser --no-input
fi

