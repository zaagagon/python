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
case 'a': printf("Se ha pulsado una a.: %d\n", ch); //salto de linea
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