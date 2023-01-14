# circularlinkedlist

The CircularLinkedList class keeps track of the head and tail pointers, as well as the size of the list.
The add method adds a new node to the list, and updates the head, tail, and size accordingly.
The str method returns a string representation of the list, which is useful for debugging and testing.
The size method returns the length of the list.
Also to add two  circular linked list, You can create an object of CircularLinkedList with the same length and then use the " + " to perform addition.

# Time and space complexity
Time Complexity:

Append : O(n) where n is the number of elements in the linked list, since we need to traverse the list to find the last node.

Space Complexity:

O(n) where n is the number of elements in the linked list, since we need to allocate memory for each node in the list.
