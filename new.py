# def Hernan(a):
#     my_lst = []
#     for z in range(a):
# 	    my_lst.append(z)
#     return my_lst

# print(Hernan(5))

# def Issac():
# 	my_dic = []
#     	for y in range(10):
#         	my_dic.append({'Awesome': y})
#     	return my_dic

# print(Issac())

# def Issac(a,b):
#     my_dic = {}
#     for y in range(10):
#         my_dic.[a] = b
#     return my_dic

# print(Issac('Awesome'+ str(y),b))


# x = '''
# <html>
# <head></head>
# <body>
# <ul>
#     <li> {{ Hernan.name }}  </li>
# </ul>
# </body>
# </html>
# '''

lst = ['python'+str(x) for x in range(11)]

def turn_into_html():
    html_lst = []
    for x in lst:
        html_lst.append('<li><h1>' + x + '</h1></li>')

    # to_string = ''
    # for x in html_lst:
    #     to_string = to_string + x
    
    to_string = ''.join(html_lst)  #same thing as the above
    return to_string

bob = turn_into_html()
x = """
    <html>
        <head></head>
        <body>
            <ul>
                {0}
            </ul>
        </body>
    </html>"""

print(x.format(bob))
print(', '.join(lst)) # concatonates a list of strings