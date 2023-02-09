The purpose of this README is to describe the function of all the script file in the 0x01-shell_permissions
0-iam_betty: switches the current user to the betty user
1-who_am_i: prints the effective username of the current user
2-groups: prints all the groups the current user is part of
3-new_owner: changes the owner of the file hello to the user betty
4-empty: creates an empty file called hello
5-execute: adds execute permission to the owner of the file hello
6-multiple_permissions: adds execute permission to the owner and the groups owner, and read permission to other users. to the file hello
7-everybody: adds execution permission to the owner, the group owner and the other user, to the file hello
8-James_Bond: sets the permission to the file hello such that, the owner has no permission at all, the group has no permission at all and the other users has all the permissions
9-John_Doe: sets the mode of the file hello to -rwxr-x-wx julien julien 23 Sep 20 14
;15 hello
10-mirror_permissions:sets the mode of the file hello the same as olleh's mode
11-directories_permissions: adds the executr permission to all sundirectories of the current directory for the ownner, the group owner and all the other users
12-directory_permissions: creates a directory called my_dir with permissions 751 in the working directory
13-change_groups: changes the group owner to shoolfor the hello
