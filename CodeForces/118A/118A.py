import sys


vowels = "aeiouyAEIOUY"

for line in sys.stdin:
	final_str = ""
	for ch in str(line).strip():
		if ch in vowels:
			continue
		final_str += "." +  ch.lower()

	print(final_str)

		
