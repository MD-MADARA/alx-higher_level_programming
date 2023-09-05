#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: double pointer to the head of the list.
 * @number: the value of the node.
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *tmp2;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head)
	{
		*head = new;
		return (*head);
	}
	/* add node at the begining */
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	/* add node in the middle */
	tmp = *head;
	tmp2 = (*head)->next;
	while (tmp2)
	{
		if (tmp2->n > number)
		{
			tmp->next = new;
			new->next = tmp2;
			return (new);
		}
		tmp = tmp2;
		tmp2 = tmp2->next;
	}
	/* add node at the end */
	tmp->next = new;
	return (new);
}
