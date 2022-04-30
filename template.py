#The file.txt should contain the list of commands
#The script will create the required template of
#dropdown list as we are using in this repo.


print("<details><summary>Redhat Package Manager (RPM)</summary>")
print("<p>")
       
filepath = 'file.txt'
with open(filepath) as fp:
   line = fp.readline()
   while line:
        line = fp.readline()
        print("```bash")
        print(line)
        print("```")
print("</p>")
print("</details>")
