/* list of keywords
1.  `auto`
2.  `break`
3.  `case`
4.  `char`
5.  `const`
6.  `continue`
7.  `default`
8.  `do`
9.  `double`
10. `else`
11. `enum`
12. `extern`
13. `float`
14. `for`
15. `goto`
16. `if`
17. `int`
18. `long`
19. `register`
20. `return`
21. `short`
22. `signed`
23. `sizeof`
24. `static`
25. `struct`
26. `switch`
27. `typedef`
28. `union`
29. `unsigned`
30. `while`
31. `_Bool` (C99)
32. `_Complex` (C99)
33. `_Generic`
34. `_Imaginary` (C99)
35. `restrict` (C99)
*/

#include <stdio.h>

int main(){
    int x;
        printf("tell me what option will you choose?");
        scanf("%d\n", x);
    
        switch(x)
        {
	  case 1:
	      char name[] = "ookami";
	      int age = 69;
	      char d = 'A';
	      float f = 0.5;
	      printf("hello world!, my name is %s and i'm %d years old\n", name, age);
	      printf("this is a char: %c and this is a float: %f and this is all.\n", d,f);
	      break;

	  case 2:
	      double c;
	      for (c=0; getchar()!=EOF; ++c);
	      printf("%.0f\n", c);
        }
};
