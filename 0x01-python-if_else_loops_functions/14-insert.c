#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node,*tmp,*n,*p;
	int i = 0;


	if(head == NULL)
	{
		return (NULL);
	}

	new_node = malloc(sizeof(listint_t));
	if(new_node == NULL)
	{
		return (NULL);
	}

	tmp = *(head);

	while(tmp)
	{
		i++;
		if(number == i-1)
		{
			p = tmp;
		}
		tmp = tmp -> next;
	}

	if(p)
	{
	n = p -> next;
	p -> next = new_node;
	new_node -> next = n;

	return (new_node);
	}
	return (NULL);
}
