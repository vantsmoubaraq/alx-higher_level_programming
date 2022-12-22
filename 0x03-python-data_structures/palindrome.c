#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int length = 0,i = 0,j = 0,data[10240];
	
	if(head == NULL)
	{
		return (1);
	}

	tmp = (*head);

	while(tmp)
	{
		length++;
		tmp = tmp->next;
	}

	if(length == 1)
	{
		return (1);
	}

	tmp = (*head);

	while(tmp)
	{
		data[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}

	for(j = 0; j < length/2; j++)
	{
		if(data[j] != data[length-1-j])
		{
			break;
			return (0);
		}
	}
	return (1);

}
