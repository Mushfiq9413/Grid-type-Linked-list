
#Class Node creates the basic structure of Node
class Node:
   def __init__(self,data):
       self.data=data
       self.right = None
       self.left = None
       self.down = None

#Create_connection vertically and horizontally depending on
# parameter ('v' for vertical, 'h' for horizontal connection on both side)
def create_connection(first_node, second_node, type):
   if type == 'h':
       first_node.right = second_node
       second_node.left = first_node
   if type == 'v':
       first_node.down = second_node
       second_node.up = first_node

#create_node creatws the node, the value of the node is send as parameter

def create_node(i):
   node = Node(i)
   return node

##This display function was created for testing purpose
# def display(m):
#     a=m
#     while True:
#          if a is not None:
#             print(a.data,end=' ')
#             a = a.right
#          if a is None:
#             print("\n")
#             a=head_node.down
#          if a.right is None and a.down is None:
#             print(a.data)
#             break
#


#starting Node
head_node=create_node(1)

#Current Node will initially be the first node
current_node=head_node

#New Node  will create newnode horizontally
new_node=head_node

#
# horizontal_newnode = head_node
# horizontal_currentnode = head_node

##Vertical new node will be used for creating node downword
vertical_newnode=head_node

##Vertical current will keep the track of the current vertical node
vertical_current_node=head_node

##This head_connecting node wil traverse horizontally to connect bottom and top node
head_connecting_node=head_node

row_size=int(input("Please specify the row size"))

column_size=int(input("Please specify the column size"))

for i in range(0,row_size):

 # if current_node.right is None:

     new_node=Node(i+2)

     create_connection(current_node,new_node,'h')

     vertical_current_node=current_node

     for j in range(column_size):
         c = 10 * (j + 1) + current_node.data

         vertical_newnode=Node(c)


         create_connection(vertical_current_node,vertical_newnode,'v')

         # vertical_current_node=vertical_newnode


         if j < (column_size-1):
             vertical_current_node=vertical_newnode
         if j == (column_size-1):
             create_connection(vertical_current_node,head_connecting_node,'v')


     create_connection(vertical_current_node,head_connecting_node,'v')
     vertical_current_node.down=head_connecting_node
     head_connecting_node.up=vertical_current_node

     if i<(row_size-1):
         current_node=new_node
     if i==(row_size-1):
         current_node.right=head_node
     head_connecting_node=head_connecting_node.right


current_node.right=head_node

create_connection(current_node,head_node,'h')



def DISPLAY1():
   down_traverse = head_node
   right_traverse = head_node
    #right1 Creating right reference, update in every loop
   for i in range(row_size):
     down_traverse=right_traverse
     for j in range(column_size):
        print(down_traverse.data,end=' ')
        down_traverse=down_traverse.down
     print('****************')
     right_traverse=right_traverse.right


print("DISPLAY1() function")
DISPLAY1()

first = head_node
second = head_node.right

create_connection(first,second,'h')



loop_reference=head_node

temp1=Node(-99)
temp2=Node(-99)

f=open("values.txt","w")


for m in range(0,row_size):



  temp1 = first
  temp2 = second


  for n in range(0,column_size):

      temp1=temp1.down
      temp2=temp2.down
      create_connection(temp1, temp2, "h")
      create_connection(temp1.up, temp1, "v")
      create_connection(temp2.up, temp2, "v")



  first=first.right
  # first=second
  second=second.right
  create_connection(first,second,'h')


# DISPLAY1()



down_traverse_d2 = head_node
right_traverse_d2 = head_node

print("DISPLAY1() function")

def DISPLAY2():
   down_traverse_d2 = head_node
   right_traverse_d2 = head_node
    #right1 Creating right reference, update in every loop
   for i in range(row_size):
     right_traverse_d2=down_traverse_d2
     for j in range(column_size):
        print(right_traverse_d2.data,end=' ')
        right_traverse_d2=right_traverse_d2.right
     print('\n&&&&&&&&&&&&')

     down_traverse_d2=down_traverse_d2.down

DISPLAY2()


print("Press DELETE to enter the grid")


from pynput.keyboard import Key, Listener

monitor = head_node


def on_press(key):
   global monitor
   if key==Key.delete:

           monitor=head_node
           print("First Node is ",monitor.data,"\n")
           print(' ')


   elif key == Key.right:
       if monitor.right.down == head_node or monitor.down.right == head_node:
           print("Last Node")
           exit()

       print("RIGHT",end=' ')
       monitor = monitor.right
       print(monitor.data,"\n")
       print('\n')

   elif key == Key.left:
       print("LEFT",end=' ')
       monitor = monitor.left
       print(monitor.data,"\n")
       print('\n')


   elif key == Key.up:
       print("UP",end=' ')
       monitor = monitor.up
       print(monitor.data,"\n")
       print('\n')
   elif key == Key.down:

       print("DOWN",end=' ')
       monitor = monitor.down
       print(monitor.data,"\n")
       print('\n')




def on_release(key):
  # print('{0} release'.format(key))
   if key == Key.esc:
       # Stop listener
       return False

# Collect events until released
with Listener(
       on_press=on_press,
       on_release=on_release) as listener:
   listener.join()















































  # loop_reference=loop_reference.down
#
#
#



# for i in range(0,3):
#    temp1 = first
#    temp2 = second
#
#
#    for j in range(0,3):
#        if j==2:
#            create_connection(temp2,loop_reference,'h')
#
#        else:
#            create_connection(temp1,temp2,"h")
#
#        temp1=temp1.down
#        temp2=temp2.down
#
#
#    first=first.right
#    first=second
#    second=first.right
#    loop_reference=loop_reference.down
#
#





# for i in range(0,3):
#     new_node=create_node(i+2)
#     create_connection(current_node,new_node,'h')
#     for j in range(0,3):
#         c=10*i+1+1
#         horizontal_newnode=create_node(c+10)
#         create_connection(horizontal_currentnode,horizontal_newnode,'h')
#         create_connection(new_node,horizontal_newnode,'v')
#         horizontal_newnode=horizontal_currentnode
#
#     current_node = new_node
#
# display(head_node)


# for i in range(0,3):
#     new_node=create_node(i+2)
#     create_connection(current_node,new_node,'h')
#     for j in (0,3):
#         c = 10 * (i +1) + current_node.data
#         print("i=",i,c)
#         print('')
#         vertical_newnode=create_node(c)
#         create_connection(vertical_current_node,vertical_newnode,'v')
#         vertical_current_node=vertical_newnode
#     print("V cur node data",vertical_current_node.data)
#     create_connection(vertical_current_node,current_node,'v')
#     current_node = new_node
#
#
# print(head_node.down.data)






# for i in range(0,3):
#    # if current_node.right is None:
#       new_node.add_horizontal_right(i+2)
#       print(current_node.data)
#
#       current_node.right=new_node
#       new_node.left=current_node
#       current_node=new_node
#
#       vertical_current=current_node
#
#       for j in range(3):
#           c = 10 * (j + 1) + current_node.data
#           vertical_newnode=Node(c)
#           vertical_current.down=vertical_newnode
#           vertical_newnode.up=vertical_current
#           vertical_current=vertical_newnode
#   vertical_current.down=head_connecting_node
#   head_connecting_node.up=vertical_current
#   current_node=new_node
#   head_connecting_node=head_connecting_node.right








# class Node:
#   def __init__(self, data,up=None,left=None):
#       self.data = data
#       self.right = None
#       self.left = None
#       self.down = None
#       self.up = None
#   def add_down(self,value):
#       up=self
#       if self.left:
# #           left=self.left.down
# #
# #
# #
# #
# #
#
#
#
#
# #Creating first Node
# head_node=Node(1)
#
# #Here first node is current Node
# current_node=head_node
#
# #Initializing a new_node with a random value
# new_node=Node(-11)
#
# #head_connecting_node for vertical circular traversal
#
# for i in range(0,3):
#     pass


#
# class Node:
#     def __init__(self, data, up=None, left=None):
#         self.data = data
#         self.right = None
#         self.left = left
#         if left:
#             self.left.right = self
#         self.down = None
#         self.up = up
#         if up:
#             self.up.down = self
#
#     def add_vertical_down(self, value):
# #         up = self
# #         if self.left:
# #             left = self.left.down
#         else:
#             left = None
#         Node(value, up, left)
#
#     def add_horizontal_right(self, value):
#         left = self
#         if self.up:
#             up = self.up.right
#         else:
#             up = None
#         Node(value, up, left)
#
#
# head_node = Node(1)
#
# current_node = head_node
#
# head_connecting_node=head_node
#
# new_node = current_node
#
#
#
# for i in range(0,3):
#    # if current_node.right is None:
#       new_node.add_horizontal_right(i+2)
#       print(current_node.data)
#
#       current_node.right=new_node
#       new_node.left=current_node
#       current_node=new_node
#
#       vertical_current=current_node
#
#       for j in range(3):
#           c = 10 * (j + 1) + current_node.data
#           vertical_newnode=Node(c)
#           vertical_current.down=vertical_newnode
#           vertical_newnode.up=vertical_current
#           vertical_current=vertical_newnode
#   vertical_current.down=head_connecting_node
#   head_connecting_node.up=vertical_current
#   current_node=new_node
#   head_connecting_node=head_connecting_node.right
#
# current_node.right=head_node

# cnode=head_node
#
# while cnode is not None:
#     print(cnode.data)
#     cnode=cnode.right
#

# class Node:
#   def __init__(self, data):
#       self.data = data
#       self.right = None
#       self.left = None
#       self.down = None
#       self.up = None
#   def add_connection(self):
#       pass
#
# #
#
# class SLinkedList:
#   def __init__(self):
# #       self.head = None
# #       self.tail = None
# #       self.vhead = None
# #
# #   def listprint(self):
# #       printval = self.head
# #
# #       while printval is not None:
# #
# #           print(printval.data,end=' ')
# #           printval = printval.right
# #
# # head_node = Node(1)
# #
# # current_node = head_node
# #
# # head_connecting_node=head_node
# #
# # new_node = Node(-1)
# #
# # vertical1_newnode=Node(-11)
# # vertical2_newnode=Node(-11)
# #
#
#
#
# # for i in range(3):
# #     if current_node.right is None:
# #         new_node=i+2
# #         current_node.right = new_node
# #         new_node.left=current_node
# #         current_node=new_node
#


 #******************************

#
# # #*************************START
# list1 = SLinkedList()
#
# # creating first node
# head_node = Node(1)
#
# current_node = head_node
#
# head_connecting_node=head_node
#
# new_node = Node(-1)
#
# # creating vertical node
# vertical_newnode=Node(-11)
#
# head_node.down=vertical_newnode
#
# vertical_current = vertical_newnode
#
# list1.head = head_node
#
# #*****************
#
#
#
# #######################
# for i in range(0,3):
#   if current_node.right is None:
#       new_node=Node(i+2)
#
#       #print("****head connecting node*********",head_connecting_node.data)
#       current_node.right=new_node
#       new_node.left=current_node
#
#       vertical_current=current_node
#
#       for j in range(3):
#           c = 10 * (j + 1) + current_node.data
#           vertical_newnode=Node(c)
#           vertical_current.down=vertical_newnode
#           vertical_newnode.up=vertical_current
#           vertical_current=vertical_newnode
#   vertical_current.down=head_connecting_node
#   head_connecting_node.up=vertical_current
#   current_node=new_node
#   head_connecting_node=head_connecting_node.right
#
# current_node.right=head_node
#
# # first = head_node
# # second=head_node
# # second = head_node.right
# # first.right=second
# # second.left=first
# #
# first = head_node
# second=head_node
# second = head_node.right
# first.right=second
# second.left=first
#
#
#
# #test************
#
# for k in range(2):
#     print(k)
#
#
#     temp1 = first
#     temp2 = second
#
#     temp1.down.right=temp2
#     temp2.down.left=temp1
#
#
#
#     first = first.down
#     # first = second
#     second = second.down
#     print("temp2.down.down.left ttttttttttttttttt ", temp2.down.down.left)

#test************************


#####################################

#list1.listprint()
#
# first = head_node
# second=head_node
# second = head_node.right
# first.right=second
# second.left=first
#
#
# loop_reference=head_node
#
# new_loop_reference=head_node
# new_loop_reference=head_node.down
# new_loop_reference.up=head_node
# print("******* loop ref********", new_loop_reference.data)
#
# temp1=head_node
# temp2=head_node
# ctemp1=head_node
# ctemp2=head_node
#
# #**********************#
#
#
# for i in range(0,3):
#    temp1 = first
#    temp2 = second
#
#    print("temp1.data//////",temp1.data)
#    print("temp2.data//////", temp2.data)
#
#
#    print("*")
#
#
#    # temp1.down.right = temp2
#    # temp2.down.left = temp1
#
#
#
#    for j in range(0,3):
#
#
#       print("(i,j)=","(",i,j,")")
#       # temp1.down.right = temp2
#       # temp2.down.left = temp1
#
#       # temp1.right = temp2
#       # temp2.left = temp1
#       temp1.down=ctemp1
#       ctemp1.up=temp1
#       temp1=ctemp1
#       temp2.down=ctemp2
#       ctemp2.up=temp2
#       temp2=ctemp2
#
#       ctemp1.right=ctemp2
#       ctemp2.left=ctemp1
#
#       print("$$$",ctemp1.right.data)
#
#    first=first.right
#    first=second
#    second=first.right
#
#
#    loop_reference.down=new_loop_reference
#    new_loop_reference.up=loop_reference
#    new_loop_reference=loop_reference
#
#    loop_reference.left=temp2
#
#
# insert_current_node=head_node
# insert_new_node=head_node
#
# vinsert_current_node=head_node
# vinsert_new_node=head_node


# for i in range(0,4):
#     insert_current_node.data=i+1
#     insert_current_node.right=insert_new_node
#     insert_new_node.left=insert_current_node
#     insert_current_node=insert_new_node
#     current_node.down = vinsert_new_node
#     vinsert_new_node.up = current_node
#     vinsert_current_node=vinsert_new_node
#     for j in range(0,3):
#         vinsert_current_node.data=10+insert_current_node.data
#         vinsert_current_node.right=vinsert_new_node
#         vinsert_new_node.left=vinsert_current_node
#         vinsert_current_node=vinsert_new_node


# cnode=head_node
#
# while cnode is not None:
#     print(cnode.data)
#     cnode=cnode.right
#
#
#










