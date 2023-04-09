import re


email_regex = re.compile('\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}')

texto = 'sandeski47@gmail.com.br'
print(email_regex.search(texto).group())
if email_regex.match(texto):
    print("Deu certo")
else:
    print("Deu merda")
