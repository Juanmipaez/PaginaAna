#include <stdio.h>
#include <string.h>

typedef struct
{
    char* name;
    char* number;
}
person;

int main (void)
{
    person people[2];
    
    people[0].name = "Carter";
    people[0].number = "+1 342-725-9712";

    people[1].name = "David";
    people[1].number = "+57 343-243-9253";

    int length = sizeof(people)/sizeof(people[0]);
    char ask_name[10];
    printf("Name to check in list: ");
    scanf("%s", &ask_name);

    for (int i=0; i<length;i++)
    {
        if (strcmp(people[i].name, ask_name) == 0)
        {
            printf("Found, phone number: %s", people[i].number);
            return 0;
        }
    }
    printf("Contact not found");
    return 1;
}

