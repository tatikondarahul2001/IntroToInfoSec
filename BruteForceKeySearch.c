#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/aes.h>
#include <openssl/evp.h>

int main() {

  // Known plaintext, ciphertext and IV
  unsigned char plaintext[21] = "This is a secret tool";
  unsigned char ciphertext[32] = {0xec, 0xe6, 0x75, 0x3e, 0x93, 0x8f, 0x8f, 0x90, 0x3c, 0xab, 0xbb, 0xe1, 0x2d, 0x39, 0x5b, 0xf5, 0xf7, 0xea, 0xe3, 0x8a, 0xd9, 0x18, 0xa2, 0xd3, 0xe1, 0xc3, 0xa8, 0x32, 0x47, 0x6d, 0x5c, 0x7a};

  unsigned char iv[16] = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x00, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f};
 
  // Try each key from the wordlist
  FILE *fp = fopen("words.txt", "r");
  char key[17];

  while (fgets(key, 17, fp)) {
	key[strlen(key) - 1] = '\0'; // Remove newline

	// Pad key to 16 bytes
	int pad = 16 - strlen(key);
	for (int i=0; i<pad; i++) {
  	strcat(key, "#");
	}

	// Decrypt using this key
	unsigned char dec_plaintext[21];
	AES_KEY aes_key;
	AES_set_decrypt_key(key, 128, &aes_key);
	AES_cbc_encrypt(ciphertext, dec_plaintext, sizeof(ciphertext), &aes_key, iv, AES_DECRYPT);

	// Compare to known plaintext
	if (memcmp(dec_plaintext, plaintext, 21) == 0) {
  	printf("Found key: %s\n", key);
  	break;
	}
  }

  fclose(fp);

  return 0;
}
