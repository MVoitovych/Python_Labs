import re
from zipfile import ZipFile

counter = 0
regex = re.compile("((72\.30\.79\.46)|(90\.7\.158\.134)).+\"GET /images.+HTTP/.+\" 200.+$")

with ZipFile('access.log.zip', 'r') as zip_:
    zip_.extractall()
    zip_.close()
    with open('filtered_logs.txt', 'a') as final_file:

        with open('access.log.txt', 'r') as logs:
            for log in logs:
                if regex.search(log):
                    counter += 1
                    final_file.write(log)
            final_file.close()


print(counter)
