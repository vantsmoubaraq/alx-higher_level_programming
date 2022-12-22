#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node,*tmp;


	new_node = malloc(sizeof(listint_t));

	if(new_node == NULL)
	{
		return (NULL);
	}    

	new_node->n = number;
	tmp = (*head);

	if(*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
	}


	while(tmp->next != NULL)
	{
		if(tmp->next->n >= number)
		{
		new_node->next = tmp->next;
		tmp->next = new_node;
		return (new_node);
		}
		tmp = tmp->next;
	}

	new_node->next = NULL;
	tmp->next = new_node;
	
	return (new_node);
}
