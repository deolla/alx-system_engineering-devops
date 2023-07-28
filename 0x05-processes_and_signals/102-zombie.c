#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - An infinite while loop function.
 * 
 * Return: Always (0) SUCCESS.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * zombies - Create a zombie process.
 *
 * Return: no return (void).
 */
void zombies()
{
	pid_t pop;

	pop = fork();
	if (pop == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * main - Start of function.
 * 
 * Return: Always (0) Success.
 */
int main()
{
	int m;

	for (m=0; m < 5; m++)
	{
		zombies();
	}
	infinite_while();

	return (0);
}
