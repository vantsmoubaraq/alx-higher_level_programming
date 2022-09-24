#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


int is_palindrome(listint_t **head)
{
	listint_t *tmp,*current;
	int i = 0,j = 0,k = 0,m = 0,length,mid,data[1024];

	if( (*head) == NULL)
	{
		return (1);
	}

	tmp= (*head);

	while(tmp)
	{
		i++;
		(tmp) = (tmp) -> next;
	}

	if(i ==1)
	{
		return (1);
	}

	else
	{
		current = (*head);

		while(current)
		{
			data[j] = current -> n;
			current = current -> next;
		}

		for(k = 0; data[k]; k++)
		{
			;
		}

		length = k-1;

			mid = length/2;

			while(m < mid)
			{
				if(data[m] != data[mid])
				{
					break;
					return (0);
				}
				m++;
				mid++;
			}

			return (1);
	}
}










