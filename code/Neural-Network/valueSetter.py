#!usr/bin/python

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def delete_element_in_list(list_element):
	while True :
		try :
			list_element.remove('\n')
		except ValueError :
			break

def find_element_in_list(element,list_element):
        try:
            index_element=list_element.index(element)
            return index_element
        except ValueError:
            return -1

def movie_name_extraction():
	f = open('newdata.csv', 'r+')
	g = open('out2.csv', 'r')
	file_list = []
	file_list2 = []
	h = open('nayafile2.csv', 'a')

#get values from out.txt
	for value in g.readlines():
		file_list.append(value.split(' '))
	for each in file_list:
		for value in each:
			file_list2.append(value.strip("'"))
	delete_element_in_list(file_list2)
	print file_list2

	for line in f.readlines():
		director = line.split(' ')[2]
		index = find_element_in_list(director,file_list2)
		if index != -1 and not is_number(director):
			line = line.replace(director, file_list2[index+1])

		writer = line.split(' ')[5]
		index = find_element_in_list(writer,file_list2)
		if index != -1 and not is_number(writer):
			line = line.replace(writer, file_list2[index+1])

		Actor1 = line.split(' ')[6]
		index = find_element_in_list(Actor1,file_list2)
		if index != -1 and not is_number(Actor1):
			line = line.replace(Actor1, file_list2[index+1])

		Actor2 = line.split(' ')[7]
		index = find_element_in_list(Actor2,file_list2)
		if index != -1 and not is_number(Actor2):
			line = line.replace(Actor2, file_list2[index+1])

		Actor3 = line.split(' ')[8]
		index = find_element_in_list(Actor3,file_list2)
		if index != -1 and not is_number(Actor3):
			line = line.replace(Actor3, file_list2[index+1])
		
		Production = line.split(' ')[9]
		index = find_element_in_list(Production,file_list2)
		if index != -1 and not is_number(Production):
			line = line.replace(Production, file_list2[index+1])

		h.write(line)
		
		



movie_name_extraction()
