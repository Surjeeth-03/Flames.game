from pydoc import source_synopsis

def mars_exploration(s):
    pattern = "sos"
    mismatches = 0
    for i in range(len(s)):
        if s[i] != pattern[i % 3]:
            mismatches += 1
    return mismatches

n=input()
print(mars_exploration(n))
