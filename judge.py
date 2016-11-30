import sys, subprocess

args = sys.argv
problem_name = args[1]

p = subprocess.Popen("python " + problem_name + "/solution.py", stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

out, err = p.communicate(b'2 3 7')
out = out.decode("utf-8").rstrip()
print(out)

with open('fizzbuzz/examplefiles/fizzbuzz-01.ans', 'r') as out_file:
    f_content = out_file.read().rstrip()
    print(f_content)

print(out == f_content)
