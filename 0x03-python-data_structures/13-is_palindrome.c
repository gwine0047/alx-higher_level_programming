#include "lists.h"
/**
 * listint_reverse - is a function that reverses a list.
 * @head: first node pointer.
 * Return: nothing
*/
void listint_reverse(listint_t **head)
{
/*(5, 4, 7, 8)*/
	listint_t *current = *head; /*Current pointing to the first node 5*/
/*Current is used to transverse the linked lists*/
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (current != NULL)
    {
		next = current->next; /*next points to the node after current(head->next) 4*/
		current->next = prev; /*current-> points to prev which is NULL*/
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 *is_palindrome - finds if a lists is a palindrome.
 *@head: is a pointer to the pointer to the head node
 *Return: 1 if successful and 0 if not.
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *temp = *head, *same = NULL;
	int status = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (status)
	{
		fast = fast->next->next;
		if (fast == NULL)
		{
			same = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	listint_reverse(&same);

	while (temp && same)
	{
		if (temp->n == same->n)
		{
			same = same->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (same == NULL)
		return (1);

	return (0);
}
