# Tool to generate Ansible Inventory from MySQL

Basic tool to generate by category from MySQL.

# Installation and Building

Requirements
```
Python 3+
mysql-connector-python
MySQL server
```
Import SQL file to your MySQL server. Also change credentials to MySQL in file generate.py

# Usage
Run python script, inventory will be printed as stdout, to create inventory file just redirect stdout to file.  
## Print output to stdout
```
python3 generate.py
```
## Print to file
```
python3 generate.py > inventory_file
```

# Graphical scheme of inventory
![scheme](https://i.imgur.com/kLXyYC7.jpg)

## Feel free to fork or create pull request :)