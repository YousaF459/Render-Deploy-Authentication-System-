set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate


# Debug: Show what environment variables are available
# echo "=== Environment Variables ==="
# echo "CREATE_SUPERUSER: $CREATE_SUPERUSER"
# echo "DJANGO_SUPERUSER_EMAIL: $DJANGO_SUPERUSER_EMAIL"
# echo "DJANGO_SUPERUSER_USERNAME: $DJANGO_SUPERUSER_USERNAME"
# echo "DJANGO_SUPERUSER_PASSWORD: $(if [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then echo "***set***"; else echo "NOT SET"; fi)"

# # Create superuser if enabled

# if [[ $CREATE_SUPERUSER == "True" || $CREATE_SUPERUSER == "true" ]]; then
#     echo "=== Creating Superuser ==="
    
#     python manage.py shell << 'EOF'
# import os
# from django.contrib.auth import get_user_model

# User = get_user_model()
# email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
# username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
# password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

# print(f"Email: {email}")
# print(f"Username: {username}")
# print(f"Password: {'***' if password else 'NOT SET'}")

# # Validate required fields
# if not email:
#     print("❌ ERROR: DJANGO_SUPERUSER_EMAIL is not set")
#     exit(1)
    
# if not password:
#     print("❌ ERROR: DJANGO_SUPERUSER_PASSWORD is not set")
#     exit(1)

# if not username:
#     username = email.split('@')[0]
#     print(f"Using generated username: {username}")

# # Check if superuser already exists
# if User.objects.filter(email=email).exists():
#     print("✅ Superuser already exists")
# else:
#     try:
#         user = User.objects.create_superuser(
#             email=email,
#             username=username,
#             password=password,
#             full_name='Admin User',
#             phone='',
#             is_verified=True
#         )
#         print("✅ Superuser created successfully!")
#         print(f"✅ Email: {email}")
#         print(f"✅ Username: {username}")
#     except Exception as e:
#         print(f"❌ ERROR creating superuser: {str(e)}")
#         # Try to get more detailed error
#         import traceback
#         traceback.print_exc()
# EOF
# else
#     echo "=== Skipping superuser creation ==="
#     echo "CREATE_SUPERUSER is not set to 'True'"
# fi

# echo "=== Build Process Complete ==="

