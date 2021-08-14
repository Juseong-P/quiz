import subprocess

p1 = subprocess.run('dir', shell=True, capture_output=True)
print(p1.args)
print(p1.returncode)
print(p1.stdout)

p2 = subprocess.run(['dir', 'dne'], stderr=subprocess.DEVNULL, shell=True)
print(p2.stderr)

# p3 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True)
# print(p3.stdout)
# p4 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p3.stdout)
# print(p4.stdout)

# p3 = subprocess.run('cat test.txt | grep -n test', capture_output=True, text=True, shell=True) <- same function

# with open('out.txt', 'wb') as f:
#     out = subprocess.run(['dir'], shell=True, capture_output=True)
#     f.write(out.stdout)