#!/bin/bash

# Define the command version
VERSION="v0.1.0"

# Function to display the help message
display_help(){
    echo "Usage: internsctl [OPTIONS]"
    echo "Custom Linux Command for Interns"
    echo
    echo "Options:"
    echo "  --help                Display this help message"
    echo "  --version             Display the command version"
    echo "  cpu getinfo           Display CPU information (similar to 'lscpu')"
    echo "  memory getinfo        Display memory information (similar to 'free')"
    echo "  user create <username>  Create a new user"
    echo "  user list              List all regular users"
    echo "  user list --sudo-only  List users with sudo permissions"
    echo "  file getinfo <file-name> Get information about a file"
    echo
}

# Rest of the script...

# Function to get CPU information
get_cpu_info() {
    lscpu
}

# Function to get memory information
get_memory_info() {
    free
}

# Rest of the script...

# Function to create a new user
create_user() {
    if [ $# -ne 2 ]; then
        echo "Usage: internsctl user create <username>"
        exit 1
    fi
    username="$2"
    useradd -m "$username"
}

# Function to list regular users
list_users() {
    getent passwd | cut -d: -f1
}

# Function to list users with sudo permissions
list_sudo_users() {
    getent group sudo | cut -d: -f4 | tr ',' '\n'
}

# Rest of the script...

# Function to get file information
get_file_info() {
    file="$1"
    if [ ! -e "$file" ]; then
        echo "File not found: $file"
        exit 1
    }
    echo "File: $file"
    echo "Access: $(stat -c %A "$file")"
    echo "Size(B): $(stat -c %s "$file")"
    echo "Owner: $(stat -c %U "$file")"
    echo "Modify: $(stat -c %y "$file")"
}

# Rest of the script...

# Function to get file information with options
get_file_info_options() {
    file="$2"
    if [ ! -e "$file" ]; then
        echo "File not found: $file"
        exit 1
    }

    case "$1" in
        --size | -s)
            stat -c %s "$file"
            ;;
        --permissions | -p)
            stat -c %A "$file"
            ;;
        --owner | -o)
            stat -c %U "$file"
            ;;
        --last-modified | -m)
            stat -c %y "$file"
            ;;
        *)
            echo "Invalid option: $1"
            exit 1
            ;;
    esac
}

# Rest of the script...

# Ensure the script is executable
chmod +x internsctl
