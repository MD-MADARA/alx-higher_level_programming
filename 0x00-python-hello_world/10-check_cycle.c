#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the list to check.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	slow = fast = list;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		/**
		 * move fast two steps forwards and slow one step so they will meet
		 * if there is a loop
		 */
		if (fast == slow)
			return (1);
	}
	return (0);
}
