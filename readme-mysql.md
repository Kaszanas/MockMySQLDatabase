# Installation

1. Download mysql zip from https://dev.mysql.com/downloads/mysql/.
2. Unpack to somewhere (ex. D:\programs\mysql\).
3. Create directory for database files (ex. D:\programs\mysql\data\).
4. Open terminal & cd to mysql directory (D:\programs\mysql\).
5. Initialize mysql data directory:

`bin\mysqld.exe --initialize --console --datadir=Y:\Projects\<YourProjectName>\data\`

6. Copy the temporary password for `root@localhost` user produced by the above command.
7. Start the database (see below).
8. Assign non-temporary password for `root@localhost` user (see below).


# Running the database server
1. Cd to mysql directory (ex. D:\programs\mysql\).
2. Run:

`bin\mysqld.exe --console --datadir=Y:\Projects\<YourProjectName>\data\`

3. Keep the terminal open until you are done with the server (ctrl+c to stop the server).

# Reassigning root password
1. Server must be running (see above).
2. Cd to mysql directory (ex. D:\programs\mysql\).
3. Run:

`bin\mysql.exe -u root -p`

4. When prompted for password, type in the temporary password from Installation section.
5. Run:

`ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';`

6. Disconnect from database (`\q`).

References:
- https://dev.mysql.com/doc/refman/8.0/en/windows-install-archive.html
- https://dev.mysql.com/doc/refman/8.0/en/data-directory-initialization.html
