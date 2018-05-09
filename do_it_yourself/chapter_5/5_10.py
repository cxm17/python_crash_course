current_users = ["cmack", "jbrooke", "sturner", "smaribelli", "jcashmere", "admin"]
new_users = ["Cmack", "bhoyle", "ktravis", "ctravis", "smack", "rreynolds"]

for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print("User name " + new_user + " in use.")
    else:
        print("Welcome " + new_user + "!")