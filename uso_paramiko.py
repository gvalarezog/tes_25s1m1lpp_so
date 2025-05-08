import paramiko
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='192.168.100.225', username='kali', password='kali', port=22)
    # stdin, stdout, stderr = ssh.exec_command('ls -a')
    # print(stdout.read())
    # print(ssh)
    # stdin, stdout, stderr = ssh.exec_command('whoami')
    # print(stdout.read())
    # print(stderr.read())
    # stdin, stdout, stderr = ssh.exec_command('pwd')
    # print(stdout.read())
    # print(stderr.read())
    # stdin, stdout, stderr = ssh.exec_command('mkdir Test19_27')
    # print(stderr.read())
    # stdin, stdout, stderr = ssh.exec_command('dir')
    # print(stdout.read())
    # stdin, stdout, stderr = ssh.exec_command('nmap -sS tes.edu.ec')
    # print(stdout.read())
    sftp_client = ssh.open_sftp()
    print(sftp_client.listdir())
    print(sftp_client.chdir('Documents'))
    print(sftp_client.getcwd())
    sftp_client.put('index2.html', '/var/www/html/index2.html')

except Exception as e:
    print(f'Se ha producido un error en la conexión: {e}')
else:
    print(f'La ejecución fue exitosa.')
finally:
    if sftp_client:
        sftp_client.close()
    if ssh:
        ssh.close()