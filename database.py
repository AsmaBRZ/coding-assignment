import json


#!usr/bin/python
import warnings
# -*- coding: utf-8 -*-
import numpy as np
import anytree
from anytree import Node, RenderTree


class Database(object):
  def __init__(self,node):
    self.db = dict()
    if type(node) != str:
      raise TypeError("Node of a wrong type, please convert your node to string")
    self.root = Node(node)
    #the dictionary "update" save the nodes extended with new children 
    self.update={}
    #the init bool indicates if it is the first time we fill in the database in order not to take into account the update dict
    self.init = True
    self.status={0:'valid', 1:'granularity_staged', 2:'coverage_staged', 3:'invalid'}
    
  def add_nodes(self,nodes):   
      for n in nodes:
        #verify the dimension of the node
        if np.array(n).shape != (2,) : 
          raise TypeError("Shape mismatch, the node shoud be a tuple of dimension (2,)")

        #search for the node's parent
        p = anytree.search.findall(self.root, filter_=lambda node: node.name == (n[1]))

        #raise an error if the node's parent does not exist
        if len(p) == 0 :
          raise TypeError("The parent of node " + str(n[0]) + " does not exist")
        
        #search for the node whether it is already stored in the databse and make a warning if it is the case
        c = anytree.search.findall(self.root, filter_=lambda node: node.name == (n[0]))
        if len(c) != 0 :
          warnings.warn("The node " + str(n[0]) + " already exists")
        else :  
          #no error or anomaly occured, we can add the new nodde
          p = p[0]
          Node(n[0], parent=p)
          #in order to use it in extract status to check whether the node has new children
          if not self.init:
            self.update[p.name] = 1

      self.init=False
      self.show()

  
  def add_extract(self,d):
    #store the images in a dictionary
    for k, v in d.items(): 
        self.db[k] = v  

  def get_extract_status(self):
    result = {}
    for key,values in self.db.items():
      result[key]=[]
      #if the image has no label, lets consider it as valid
      if len(values) == 0 : 
        result[key].append(0)
      else:
        for label in values:
          #if the label does nont exist in the database => invalid label
          p = anytree.search.findall(self.root, filter_=lambda node: node.name == (label))
          if len(p) == 0 :
            result[key].append(3)
            continue

          #check the number of my parent's childs
          elif p[0].name != self.root.name and p[0].parent.name in self.update:
            result[key].append(2)
            continue
          
          #check if I have childrens
          elif p[0].name in  self.update:
            result[key].append(1)
            continue
          else:
            result[key].append(0)
      result[key]=self.status[np.max(np.array(result[key]))]
    print("Result",result)
    self.update={}
    return result

  def show(self):
    for pre, fill, node in RenderTree(self.root):
        print("%s%s" % (pre, node.name))
