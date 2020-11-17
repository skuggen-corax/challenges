#include <stdio.h>
#include <stdlib.h>

// solution for pseudo-pseudo-random chall of affinity ctf 2020

int main() {
   // output from chall: "message"
   unsigned char encoded_input[25] = { 0x63, 0x51, 0x48, 0x6A, 0x40,0x09, 0x1E, 0x7A, 0x7A, 0x0C, 0x0B, 0x02, 0x49, 0x48, 0x4D, 0x43, 0x71, 0x6B, 0x30, 0x5A, 0x12, 0x1B, 0x27, 0x39, 0x53};
   // byteshifter: got from reversing: "task"
   unsigned char jumbler[25] = { 0x17, 0x0e, 0x02, 0x15, 0x0B, 0x03, 0x04, 0x10,  0x16, 0x05, 0x12, 0x06, 0x0C, 0x07, 0x13, 0x01, 0x08, 0x14, 0x09, 0x0A, 0x0D, 0x18, 0x00, 0x11, 0x0F};
   
   int i = 0;
   int j = 0;

   // generate same key as chall
   srand(0x1548);
   int xor_key [8];
	int pseudorandom;
   printf("key: \t\t");
   while ((int)i <10) {
	   pseudorandom = rand();
	   if ((i & 1) == 0) {
		   xor_key[j] = pseudorandom % 0x7f;
         printf("%x", xor_key[j]);
		   j = j + 1;
	   }
	   i = i + 1;
   }

   // xor key with ciphertext
   printf("\nxor-ed: \t");
   unsigned char xored[25];
   i = 0;
   while (i < 25) {
	   xored[i] = (unsigned char) xor_key[(int)i / 5] ^ encoded_input[(int)i];
	   printf("%c ", xored[i]);
	   i++;
   }
   
   // shift bytes back to original order
   printf("\nshuffle: \t");
	unsigned char flag[25];
   i = 0;
   while (i < 25) {
	   j = jumbler[i];
	   printf("%d",j, " ");
	   flag[j] = xored[i];
	   printf(" ");
	   i++;
   }
   printf("\n");

   // print flag
   printf("flag: \t\t");
   i = 0;
   while (i <25) {
	   printf("%c",flag[i]);
	   i++;
   }
   printf("\n");

   return 0;
}
