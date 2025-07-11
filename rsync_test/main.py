import subprocess


def rsync_file(local_path, remote_user, remote_host, remote_path):
    cmd = ["rsync", "-avz", local_path, f"{remote_user}@{remote_host}:{remote_path}"]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    rsync_file("my-text.txt", "inno", "172.16.10.30", "/home/inno/wally_test/")
