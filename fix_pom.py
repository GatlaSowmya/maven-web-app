
import subprocess
import os

# Path to your project directory
project_dir = "/home/ubuntu/maven-web-app"

# Maven commands to run
maven_clean_install_command = "mvn clean install"
maven_package_command = "mvn package"

# Change to the project directory
os.chdir(project_dir)

# Step 1: Clean and Install the Maven Project
def run_maven_command(command):
    try:
        # Run the command in the shell
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())  # Print the output
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during command execution: {e.stderr.decode()}")
        return False

# Execute Maven Clean Install (or Package)
if run_maven_command(maven_clean_install_command):
    print("Maven build successful!")
else:
    print("Maven build failed.")

# Step 2: If you want to deploy the WAR file, you can add deployment steps here
# For example, copying the WAR to a remote server using SCP
def deploy_war(war_file_path, destination_path):
    try:
        # Use scp (secure copy) to transfer the WAR file
        scp_command = f"scp {war_file_path} {destination_path}"
        result = subprocess.run(scp_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())  # Print output of scp command
        print("Deployment successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during deployment: {e.stderr.decode()}")
        return False

# Example deployment step (after successful build)
war_file = "/home/ubuntu/maven-web-app/target/maven-web-app.war"
remote_server_path = "user@http://65.2.140.154:8080/:/path/to/deploy/"
deploy_war(war_file, remote_server_path)
