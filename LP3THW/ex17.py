import sys
import os.path

script, from_file, to_file = sys.argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# Like this:
# indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {os.path.exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


# Before you can run this, create a test file named "test.txt" from bash: $ echo "This is a test file." > test.txt

# To run:
# $ python ex17.py test.txt new_file.txt

# Expected result should be contents of test.txt copied to new_file.txt. You'll of course have to change the content of test.txt to see any changes in new_file.txt.