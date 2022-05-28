//en python no existe el switch

//compilar el archivo

//gcc swicht-nopython.c -o switch; 

//para ejecutar archivo
//./switch 
//warning con el main



#include <stdio.h>
main() {
char ch;
printf("Introduzca una vocal: ");
ch=getchar();
switch(ch) {
case 'a': puts("Se ha pulsado una a.");
break;
case 'e': puts("Se ha pulsado una e.");
break;
case 'i': puts("Se ha pulsado una i.");
break;
case 'o': puts("Se ha pulsado una o.");
break;
case 'u': puts("Se ha pulsado una u.");
break;
default: puts("Error");
}
}