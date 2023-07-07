a = "Hello, World!"
print(a.upper())

# HELLO, WORLD!

b = "Hello, World!"
print(b.lower())

# hello, world!

c = " Hello, World! "
print(c.strip())

# Hello, World!

d = "Hello, World!"
print(d.replace("H", "J"))
e = "KSAP LAMAR"
print(e.replace("KSAP", "POISON"))
# Jello, World! replace("교체될 문자열", "교체할 문자열")
# POISON LAMAR

f = "Hello, World"
print(f.split(","))
# ['Hello', 'World'] split("나누게 될 기준이 되는 문자열")
# 해당 문자 기준으로 쪼개서 서브스트링 형태로 리턴