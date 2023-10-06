#Yashodip Beldar
#15/9/2023
#Menu Driven program for Linked list ,Stack and Queue Operations

linked_list = []
stack = []
queue = []

while True:
    print("\nMenu:")
    print("1. Linked List Operations")
    print("2. Stack Operations")
    print("3. Queue Operations")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            print("\nLinked List Operations:")
            print("1. Insert")
            print("2. Display")
            print("3. Delete all")
            print("4. Back")
            
            linked_list_choice = input("Enter your choice for Linked List: ")

            if linked_list_choice == '1':
                data = input("Enter data to insert: ")
                linked_list.append(data)
                print("Data inserted to the linked list.")
                continue
            elif linked_list_choice == '2':
                print("Linked List:", linked_list)
                continue
            elif linked_list_choice == '3':
                linked_list.clear()
                print("Linked List cleared.")
                continue
            elif linked_list_choice == '4':
                print("Main Menu.")
                break
            else:
                print("Invalid choice for Linked List. Please try again.")

    elif choice == '2':
        while True:
            print("\nStack Operations:")
            print("1. Push")
            print("2. Pop")
            print("3. Display")
            print("4. Back")
            
            stack_choice = input("Enter your choice for Stack: ")

            if stack_choice == '1':
                item = input("Enter item to push onto the stack: ")
                stack.append(item)
                print("Item pushed onto the stack.")
                continue
            elif stack_choice == '2':
                if stack:
                    item = stack.pop()
                    print(f"Popped item: {item}")
                else:
                    print("Stack is empty.")
                continue
            elif stack_choice == '3':
                if stack:
                    print(f"Stack is: {stack}")
                else:
                    print("Stack is empty.")
                continue
            elif stack_choice == '4':
                    print("Main Menu.")
                    break
            else:
                print("Invalid choice for Stack. Please try again.")

    elif choice == '3':
        while True:
            print("\nQueue Operations:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Display")
            print("4. Back")
            
            queue_choice = input("Enter your choice for Queue: ")

            if queue_choice == '1':
                item = input("Enter item to enqueue: ")
                queue.append(item)
                print("Item enqueued.")
                continue
            elif queue_choice == '2':
                if queue:
                    item = queue.pop(0)
                    print(f"Dequeued item: {item}")
                else:
                    print("Queue is empty.")
                continue
            elif queue_choice == '3':
                if queue:
                    print(f"Queue is {queue}\n")
                else:
                    print("Queue is empty.")
                continue
            elif queue_choice == '4':
                print("Main Menu.")
                break
            else:
                print("Invalid choice for Queue. Please try again.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again")