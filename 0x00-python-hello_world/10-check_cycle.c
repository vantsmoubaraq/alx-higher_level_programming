#include "lists.h"

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
