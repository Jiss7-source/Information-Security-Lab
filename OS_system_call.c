#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <dirent.h>

int main() {
    pid_t pid = fork();  // Create child process

    if (pid == 0) {  // CHILD
        printf("Child PID: %d\n", getpid());

        // Get file size
        struct stat info;
        stat("sample.txt", &info);
        printf("File size: %ld bytes\n", info.st_size);

        // List directory
        DIR *dir = opendir(".");
        struct dirent *entry;
        while ((entry = readdir(dir)) != NULL)
            printf("Found: %s\n", entry->d_name);
        closedir(dir);

        execlp("date", "date", NULL);  // Run date command

    } else {  // PARENT
        printf("Parent PID: %d\n", getpid());
        wait(NULL);  // Wait for child
    }
    return 0;
}