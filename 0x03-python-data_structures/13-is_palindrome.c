#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * number_nodes - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t number_nodes(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	return (n);
}




/**
*is_palindrome - define if funtion is palindorme.
*@head: is pointer.
*Return: 0
*/

int is_palindrome(listint_t **head)
{
	int nd, j;
	int *temp;
	unsigned int n; /* number of nodes */
	const listint_t *current;

	current = *head;
	n = 0;
	nd = number_nodes(*head);
	if (nd == 0)
		return(1);
	temp = malloc(sizeof(int) * nd);
	while (current != NULL)
	{
		temp[n] = current->n;
		current = current->next;
		n++;
	}
	for (j = 0; j < (nd / 2); j++)
	{
		if (temp[j] != temp[nd - 1 - j])
			return (0);
	}
	printf("%i\n", nd);
	return (1);
}
