# Remove node given the key in a double linked list


def delete_node_with_key(keyName:str, linked_list_head:Node):
    working_node = linked_list_head
    # Assuming that the end node does not point back to the beginning
    # what if we need to remove the first or the last node
    while(True):
        if (working_node.val == keyName):
            if(working_node.prev == None):
                # First node, delete current node
                newHead = working_node.next
                newHead.prev = None
                remove(working_node)
                return newHead
            elif(working_node.next == None):
                # End node case
            else:
                # Middle node case
        # We did not match this iteration, set next node and continue
        working_node = linked_list_head.next
        if (working_node == None):
            return "Could not find the value"
