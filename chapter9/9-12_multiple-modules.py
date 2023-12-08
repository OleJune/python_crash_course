from admin import Admin, User, Privileges

#import admin
#top_admin = admin.Admin('taylor', 'reeze', 40, 'iceland')

top_admin = Admin('taylor', 'reeze', 40, 'iceland')

top_admin.privileges.show_privileges()

top_admin.privileges.change_privileges(['can delete user', 'can report violations'])
top_admin.privileges.show_privileges()

top_admin.privileges.privileges = ['can do whatever they want']
top_admin.privileges.show_privileges()
