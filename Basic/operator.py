# ------------> Augmented Operator
first_var = 100
# print(first_var) # 100
second_var = 200
# third_var = 300

# result = ((third_var*first_var)/second_var)
# print(result) # 150

# first_var = first_var +11
# print(first_var)

# second_var += 11
# print(second_var)

# third_var -= 10
# print(third_var)
# first_var *=2
# print(first_var)

# result /=10
# print(result)

first_var **= 2
print(first_var)

second_var //= 10
print(second_var)

# ------------> Logical Operator 
var1 = 5
var2 = 10

bitwiseand = (var1 & var2)
print(bitwiseand)

bitwiseor = (var1 | var2)
print(bitwiseor)

bitwisenot = ~var1
print(bitwisenot)

var3 = 25
bitwisenot = ~var3
print(bitwisenot)
# ------------> Membership Operator 

languages = ["C","CPP","JAVA","PYTHON","PERL","RUBY","SCRIPT"]

is_java_avail = "JAVA" in languages
print(is_java_avail)

is_pascal_avail = "PASCAL" in languages
print(is_pascal_avail)

is_script_avail= "SCRIPT" not in languages
print(is_script_avail)

is_cobol_avail = "COBOL" not in languages
print(is_cobol_avail)