from passlib.hash import pbkdf2_sha256 as hashing
from csv import reader,writer
from sys import exit

def main():
    users_file="data/users.csv"
    try:
        with open(users_file,newline="",encoding="utf-8-sig") as csvfile:
            user_dict={int(uid):[name,passw] for uid,name,passw in reader(csvfile,delimiter=",")}
            print(f"\n{len(user_dict)} users found.\n")
            try:
                user_int=max(user_dict.keys())+1
            except:user_int=1
    except FileNotFoundError:
        user_dict={}
        user_int=1
        if not input(f"No '{users_file}' file found: enter 'y' to create new file. ")=="y":exit()

    while True:
        newname=input("Enter new user's name: ")
        newpass=hashing.hash(input("Enter password: "))
        user_dict[user_int]=[newname,newpass]
        user_int+=1
        if not input("Enter anything to add another user, or leave blank to finish."):break 
        
    with open(users_file,"w",newline="",encoding="utf-8-sig") as csvfile:
        csvwriter=writer(csvfile,delimiter=",")
        for key,value in user_dict.items():
            csvwriter.writerow([key,value[0],value[1]])

if __name__=="__main__":main()