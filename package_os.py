import os
from datetime import *

# print(os.getcwd())
# print(os.listdir()

# try:
#     os.mkdir('package_os')
#     print('폴더를 만들었습니다.')
# except FileExistsError as e:
#     print(e)
# try:
#     os.rmdir('package_os')
#     print('폴더를 삭제했습니다.')
# except FileNotFoundError as nf:
#     print(nf)
#
# print('프로그램을 종료합니다.')

# mod_time = os.stat('package_os').st_mtime
# print(datetime.fromtimestamp(mod_time))

print(os.environ['HOME'])
print(os.getcwd())
