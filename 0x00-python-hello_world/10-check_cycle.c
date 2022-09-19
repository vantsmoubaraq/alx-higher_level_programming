#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list - first node of list
 * Return: 1 if cycle exists, 0 if it does not
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp,*first;

	first = list;
	tmp = list;
	while(tmp)
	{
		if(tmp->next == first)
		{
			return (1);
		}
		tmp = tmp->next;
	}
	return (0);
}
