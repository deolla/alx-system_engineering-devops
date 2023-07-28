#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

void zombies()
{
	pid_t pop = fork();
	if (pop == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

int main()
{
	int m;

	for (m=0; m < 5; m++)
	{
		zombies();
	}

	while (1)
	{
		sleep(1);
	}
	return (0);
}
