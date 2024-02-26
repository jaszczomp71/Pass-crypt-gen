import subprocess
import secrets
import base64


def generate_password(length=26): # Generuje 26cio znakowe hasło.
    
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    return ''.join(secrets.choice(alphabet) for i in range(length))

def encrypt_with_ansible_vault(password, name): # Szyfrowanie przez ansible-vault.
    
    cmd = f'ansible-vault encrypt_string --stdin-name "{name}"'
    process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=password)
    if process.returncode == 0:
        return stdout.strip()
    else:
        raise Exception(f"Error encrypting password: {stderr}")

def main(instance): # Generowanie i szyfrowanie
    passwords = {
        'vault_xxx_admin_password': generate_password(),
        'vault_xxx_proxysql_monitor_user_pass': generate_password(),
        'vault_xxx_rabbitmq_envs_pass': generate_password(),
        'vault_xxx_db_envs_pass': generate_password(),
        'vault_xxx_xxx_envs_pass': generate_password(),
        'vault_xxx_oauth_envs_pass': generate_password(),
        'vault_xxx_dotenv_app_secret': generate_password(52),
        'vault_xxx_dotenv_app1_password': generate_password(),
        'vault_xxx_dotenv_app2_password': generate_password(),
        'vault_xxx_mailer_envs_pass': generate_password(),
        'vault_xxx_oauth2_encryption_key': base64.b64encode(generate_password().encode()).decode(),
        'vault_xxxp_sources_pass': generate_password()
    }

    # Przykład użycia
    for name, password in passwords.items():
        encrypted = encrypt_with_ansible_vault(password, name)
        print(encrypted)

if __name__ == "__main__":
    instance = 'example_instance'  # Możesz pobrać to z argumentów linii poleceń lub innej logiki
    main(instance)
