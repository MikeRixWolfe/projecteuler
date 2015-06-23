from glob import glob
from os import path
from re import match
from subprocess import call

problems = set(glob(path.basename(path.join(".", "e*.py"))))

for problem in sorted(problems):
    abspath = path.abspath(problem)
    num = match(r'e0*(\d+).*', problem).group(1)
    print "Euler %s %s" % (num, '-'*(25-len(num)))
    call(['python', abspath])
    print "-"*32
    wait = raw_input("<press ENTER to continue>")

call("rm *.pyc 2>/dev/null", shell=True)
