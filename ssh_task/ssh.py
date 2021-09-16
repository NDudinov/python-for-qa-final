import logging
import sys

from paramiko import AutoAddPolicy
from paramiko import SSHClient


def ssh_task(loglevel, host, user, password=None):
    logging.basicConfig(format='%(levelname)s:%(message)s')
    logger = logging.getLogger()
    logger.setLevel(loglevel.upper())
    file_name = 'test.txt'
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(hostname=host, port=22, username=user, password=password, timeout = 20)
    stdin, stdout, stderr = client.exec_command(f'touch {file_name}')
    ftp = client.open_sftp()
    file = ftp.file(file_name, "a", -1)
    file.write('TEST_ME\n')
    file.flush()
    ftp.close()
    stdin.close()
    stdout.close()
    stderr.close()
    stdin, stdout, stderr = client.exec_command('ls -p | grep -v /')
    result = bytes.decode(stdout.read())
    logging.info(result)
    for s in result.split("\n"):
        print(s)
    logging.info(stdout)
    stdin.close()
    stdout.close()
    stderr.close()
    client.close


if __name__ == "__main__":
    host_c = sys.argv[2]
    user_c = sys.argv[3]
    passw_c = sys.argv[4]
    loglevel_c = sys.argv[1]
    ssh_task(loglevel_c, host_c, user_c, passw_c)



