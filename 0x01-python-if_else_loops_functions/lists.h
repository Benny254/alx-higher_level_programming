#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - the singly linked list
 * @n: an integer
 * @next: to points to the next node
 *
 * Description: the singly linked list node structure
 *
 */
typedef struct listint_s
{
    int a;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int a);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
