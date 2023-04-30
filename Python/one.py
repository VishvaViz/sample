# import os
# def check_file_exists(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         if isinstance(result,str):
#             if os.path.isfile(result):
#                 size=os.path.getsize(result)
#                 return f"{result} exists on disk{size}" 
#             else:
#                 return f"{result}does not exists "
#         else:
#             return "error:ou"
#         return wrapper
# check_file_exists()

def lists(list1,list2):
    for i in range(min(len(list1,len(list2)))):
        yield(list1[i],list2[i])
        list1=[1,2,3]
        list2=['a','b','c']
        for item in list(list1,list2):
            print(item)
list()