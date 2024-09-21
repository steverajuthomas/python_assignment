#need help with comprehension
#{key_expr: value_expr for item in iterable}

l1=['Sam', 'Alice', 'Mona']
l2=['Commerce', 'Science', 'Computer']

# student_subject_dict={}
# for name in range(len(l1)):
#     for subject in range(len(l2)):
#         if name==subject:
#             student_subject_dict[l1[name]]=l2[subject]
#
# print(student_subject_dict)

student_subject_dict={l1[i]:l2[i] for i in range(len(l1))}
print(student_subject_dict)