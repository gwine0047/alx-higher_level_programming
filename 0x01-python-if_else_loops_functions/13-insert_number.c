#include "lists.h"
/**
 * insert_list - puts a number at the biegginer of a sorted list.
 * @head: A pointer to the head node.
 * @number: The number to be alloted.
 * Return: 0 if unsuccessful
 */
listint_t *insert_node(listint_t **head, int number):
{
	listint_t *node = *first, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL)

	new_node->n = number;
	if (node->n >= number || !node)
	{
		new_node->next = node;
		*first = new_node;
		return (new_node);
	}
	while (node->next->n < number && node && node->next)
		node = node->next;

	new_node->next = node->next;
	node-> = new_node;

	return (new);
}	
