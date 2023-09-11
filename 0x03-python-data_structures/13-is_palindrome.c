#include "lists.h"

/**
 * is_palindrome - cheks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int i, size = 0, array[2048];

	if (!head || !*head)
		return (1);
	tmp = *head;
	while (tmp)
	{
		size++;
		array[size - 1] = tmp->n;
		tmp = tmp->next;
	}

	for (i = 0; i < size / 2; i++)
	{
		if (array[i] != array[size - 1 - i])
			return (0);
	}
	return (1);
}
