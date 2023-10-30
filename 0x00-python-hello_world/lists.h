#ifndef MAIN_H
#define MAIN_H

#include <stdlib.h>

/**
 * struct listint_s - The singly linked list
 * @n:an an integer
 * @next: To points to the next node
 *
 * Description: The singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int r;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int r);

#endif /* LISTS_H */
