import os
import subprocess

def ping_host(hostname):
    """VULNERABLE: OS command injection."""
    os.system("ping -c 3 " + hostname)

def list_files(directory):
    """VULNERABLE: Command injection via subprocess."""
    result = subprocess.check_output("ls -la " + directory, shell=True)
    return result.decode()

def backup_db(db_name):
    """VULNERABLE: Command injection."""
    os.popen(f"mysqldump {db_name} > /tmp/backup.sql")
