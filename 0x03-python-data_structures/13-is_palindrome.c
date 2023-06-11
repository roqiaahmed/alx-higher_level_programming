#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */

int is_palindrome(listint_t **head)
{
listint_t *current = *head;
int count = 0, i;
int *list;
int is_palindrome = 1;
if (current == NULL) {
return 1;
}
while (current != NULL) {
count++;
current = current->next;
}
list = (int*)malloc(count * sizeof(int));
if (list == NULL) {
exit(0);
}
current = *head;
for (i = 0; i < count; i++)
{
list[i] = current->n;
current = current->next;
}
for (i = 0; i < count / 2; i++)
{
if (list[i] != list[count - i - 1])
{
is_palindrome = 0;
break;
}
}
free(list);
return is_palindrome;
}
