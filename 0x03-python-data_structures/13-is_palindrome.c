#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - to reverses a singly-linked listint_t list.
 * @head: The  pointer to the starting node of the list to reverse.
 *
 * Return: The pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head) {
	listint_t *node = *head, *next, *prev = NULL;

	for (; node; node = next) 
	{
        	next = node->next;
		node->next = prev;
		prev = node;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - To check if a singly linked list is a palindrome.
 * @head: The pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (j = 0; j < (size / 2) - 1; j++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
